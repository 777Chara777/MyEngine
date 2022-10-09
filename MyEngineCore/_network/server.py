import socket
import asyncio
import pickle

from time import sleep

import BaseModule.BaseModule as bm
from .module import Dopmodule as dm


from BaseModule._LogError_V3 import logerror

list_new_functions = {}

logerror.add("./Logger/last.log", format="[{time3}] ~{level}\t {function}  -: {message}", color=True)

def add_function(**kargs):
    def wrepper(funk: "function"):
        if not asyncio.iscoroutinefunction(funk):
            raise TypeError('command registered must be a coroutine function')
        
        if "name" in kargs:
            list_new_functions[kargs['name']] = funk
        else:
            list_new_functions[funk.__name__] = funk
            
        logerror.debug('%s has successfully been registered as an command' % funk.__name__)
    return wrepper

class call_info:
    def __init__(self, self_server: "socket_server", type, data, connect):
        self.self_server: "socket_server" = self_server
        self.type_data: str = type
        self.data: dict = data
        self.connect: socket.socket = connect
    
    def __str__(self) -> str:
        return "<server.call_info type=%s, data=%s>" % (self.type_data, self.data)
    
    def __repr__(self) -> str:
        return "<server.call_info type=%s, data=%s, connect=%s>" % (self.type_data, self.data, self.self_server.netlist[self.connect])

    async def send(self, type: str, value: dict={}) -> tuple:
        return await self.self_server.add_task ( self.self_server.send_to(self.connect, type, value) )

    async def send_all(self, type: str, value: dict={}) -> tuple:
        return await self.self_server.add_task ( self.self_server.send_all(type, value) )

class socket_server():
    def __init__(self, ip: str='localhost', port: int=8888, settings=None) -> None:

        logerror.debug("Create __init__ file")

        self.__main_loop = asyncio.new_event_loop()
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.settings_ = (ip, int(port))
        
        self.add_task = lambda function : self.__main_loop.create_task(function)
        self.netlist = {}
        self.list_players = []
    

    async def add_user(self, connect: socket.socket):
        pass
        # await self.add_task( self.send_all("Send", {"Message": f"осталось игрово до начало: {player_max-len(self.netlist)}"}) )

    async def remove_user(self):
        pass
        # await self.add_task( self.send_all("Send", {"Message": f"осталось игрово до начало: {player_max-len(self.netlist)}"}) )

    
    def server_setup(self) -> bool:
        logerror.debug("Server setup")
        acc = 5
        while True:
            try:
                self.__socket.bind(self.settings_)
                self.__socket.listen(0)  
            except Exception as ex:
                logerror.warn(f"Server Fail. {ex} > {acc}")
                if acc == 0:
                    return False
                acc-=1
                sleep(30)

            else:
                self.__socket.setblocking(False)
                return True

    async def send_to(self, connect: socket.socket, type: str, value: dict={}) -> tuple:
        "send dict to client"
        error_mess:str = None
        resaute: bool = False

        if connect not in self.netlist:
            error_mess = f"connect user {connect} not find."

        elif isinstance( value, dict ):
            try:
                data = {
                    "Type": str(type),
                    "Time": bm.Time(3),
                    "Info": value
                }
                await self.__main_loop.sock_sendall(connect, pickle.dumps(data)) 

            except ConnectionResetError as cre:
                nick = self.netlist[connect]['nick']
                timejoin = self.netlist[connect]["time_join"]
                timestamp = self.netlist[connect]["time_stamp"]
                time_session = dm.TimeFormat(bm.mutcnow().timestamp() - timestamp)

                logerror.debug(f"Error {cre} - delite user \nname :- {nick}\ntime connect :- {timejoin}\nconnect sessin :- {dm.TimeFormat(time_session)}\nconnect :- {connect}")
                del self.netlist[connect]
                await self.remove_user()
            except Exception as ex: error_mess = str(ex)
    
            else: resaute = True

        else: error_mess = "value not is dict"

        return (resaute, error_mess)

    async def send_all(self, type: str, value: dict={}):
        "send dict to all client"
        error_mess: str = None
        resaute: bool = False

        if isinstance( value, dict ):
            try:
                for connect in self.netlist:
                    await self.add_task(self.send_to( connect, str(type), value ))
            except Exception as ex: error_mess = str(ex)
    
            else: resaute = True

        else: error_mess = "value not is dict"

        return (resaute, error_mess)

    async def lisen_user(self, connect):
        
        while True:
            try:
                data = await self.__main_loop.sock_recv(connect, 2048) 
                data_decode = pickle.loads(data)

            except (ConnectionResetError, ConnectionAbortedError, EOFError):
                logerror.info(f'Server remove user')
                del self.netlist[connect]
                await self.remove_user()
                break

            else:
                data_type = data_decode["Type"] if "Type" in data_decode else None
                data_time = data_decode["Time"] if "Time" in data_decode else None
                data_info = data_decode["Info"] if "Info" in data_decode else None

                ip_connect = self.netlist[connect]["ip"]
                time_join = self.netlist[connect]["time_join"]

                logerror.info( f"[{ip_connect}] [{data_type}] [{data_time}] > {data_info}" )

                
                if data_type in list_new_functions:
                    self.add_task( list_new_functions[data_type](self, call_info(self, data_type, data_info, connect)) )

                else:
                    self.add_task( self.send_to(connect, "Error", {"Message": f"No find type {data_type}"}) )

    def run(self):

        async def server():

            while True:
            
                connect, addres = await self.__main_loop.sock_accept(self.__socket)

                logerror.info(f"Connect user {addres}")

                self.netlist[connect] = {
                    "nick": f"User-{len(self.netlist)} XD", 
                    "time_join": bm.Time(3), 
                    "time_stamp": bm.mutcnow().timestamp(), 
                    "ip": addres[0],
                    "port": addres[1]
                }

                await self.add_user(connect)
                self.add_task( self.lisen_user( connect ) )
        
        async def terminal(): 
            while True:
                line = await self.__main_loop.run_in_executor(None, input, '')
                line = str(line).strip()
                if line == 'stop':
                    for connect in self.netlist:
                        connect: socket.socket
                        connect.close()
                    exit(0)
                
                elif line == "list":
                    
                    list_connects = []

                    for connect in self.netlist:
                        nick = self.netlist[connect]["nick"]
                        timejoin = self.netlist[connect]["time_join"]
                        timestamp = self.netlist[connect]["time_stamp"]
                        ip_user = self.netlist[connect]["ip"]

                        time_session = dm.TimeFormat(bm.mutcnow().timestamp() - timestamp)


                        list_connects.append(
                            f"[{ip_user} / `{nick}`] {timejoin} > { '%dd %dh %dm %ds' % time_session.get_time() } {'is play' if str(connect) in self.list_players else 'is not play' }"
                        )
                        logerror.info(f"list users {len(list_connects)}\n"+"\n".join(list_connects))
                else:
                    logerror.warn(f"Not find command: `{line}`")
            
        if self.server_setup():
            logerror.info("OK. Start Server %s-%s" % self.settings_)

            self.add_task(terminal())
            self.__main_loop.run_until_complete(server())

# if __name__ == "__main__":
#     socket_server (port = 25565 ).run()
    