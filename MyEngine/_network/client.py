import pickle
import socket
import time
from threading import Thread

import BaseModule.BaseModule as bm
from BaseModule._LogError_V3 import logerror

from .module import Dopmodule as dm

# import modules.Dopmodule as dm


list_new_functions = {}

logerror.add('./Logger/last.log', format="[{time3}] ~{level}\t {function}  -: {message}", color=True)

def add_function(**kargs):
    def wrepper(funk: "function"):
        
        if "name" in kargs:
            list_new_functions[kargs['name']] = funk
        else:
            list_new_functions[funk.__name__] = funk
            
        logerror.debug('%s has successfully been registered as an command' % funk.__name__)
    return wrepper

class call_info:
    def __init__(self, self_server: "SocketClient", type, data):
        self.self_server: "SocketClient" = self_server
        self.type_data: str = type
        self.data: dict = data

    def __str__(self) -> str:
        return "<client.call_info type=%s, data=%s>" % (self.type_data, self.data)
    
    def __repr__(self) -> str:
        return "<client.call_info type=%s, data=%s>" % (self.type_data, self.data)

class SocketClient:

    def __init__(self, ip: str='localhost', port: int=8888) -> None:
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        logerror.debug("__init__ client.")

        self.server_info = (ip, int(port))

        self.connects = []

    def __str__(self) -> str:

        list_connects = [ f'({x["nick"]}, {x["time"]})' for x in self.connects ]

        return f"<SocketClient: [len={len(list_connects)}, user={', '.join(list_connects )}]>"

    def listen_server(self):
        """
        listen_server: Стушает сервер
        """

        while True:
            try:
                data = self.__socket.recv(2048)
                data_decode = pickle.loads(data)
            except (ConnectionResetError, ConnectionAbortedError, EOFError, OSError):
                logerror.error(f"[Connect]: Server close")
                self.__socket.close()
                break

            else:
                data_type = data_decode["Type"] if "Type" in data_decode else None
                data_time = data_decode["Time"] if "Time" in data_decode else None
                data_info = data_decode["Info"] if "Info" in data_decode else None

                

                if data_type == "Send":
                    logerror.info(f"server: {data_info['Message']}")
                
                elif data_type in list_new_functions:
                    Thread(target=list_new_functions[data_type], args=(self, call_info(self, data_type, data_info)), daemon=True).start()

                elif data_type == "Error":
                    logerror.warn(f"error server: {data_info['Message']}")
                
                else:
                    logerror.error(f"Server {data_info}")

    def get_send(self, type):
        get_sockey = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        get_sockey.connect(self.server_info)

        data_send = pickle.dumps({
            "Type": str(type),
            "Time": bm.mutcnow().timestamp() })

        get_sockey.send(data_send)

        data = get_sockey.recv(2048)
        data_decode = pickle.loads(data)
        get_sockey.close()

        return data_decode

    def send(self, type: str, value: dict = {}) -> tuple:
        "send dict to server"
        error_mess:str = None
        resaute: bool = False

        if isinstance( value, dict ):
            try:
                data = {
                    "Type": str(type),
                    "Time": bm.mutcnow().timestamp(),
                    "Info": value
                }
                self.__socket.send( pickle.dumps(data) )
            except Exception as ex: error_mess = str(ex)
    
            else: resaute = True

        else: error_mess = "value not is dict"

        return (resaute, error_mess)

    
    def setup_connect_server(self):
        logerror.debug("Setup client")
        acc: int= 5 
        while True:
            try:
                self.__socket.connect(self.server_info) 
            except (ConnectionRefusedError, TimeoutError):
                logerror.warn(f"connect to: {self.server_info} error, {acc}")
                if acc == 0:
                    return False 
                acc -= 1
            else:
                return True

    
    def run(self):
        logerror.debug(f"Run client: {self.server_info}")

        if self.setup_connect_server():
            Thread(target=self.listen_server, daemon=True).start()
            pass
    