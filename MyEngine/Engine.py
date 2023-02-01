from ._utils import BaseModule as bm
# from ._network.server import socket_server
# from ._network.client import socket_client
from ._utils.BaseModule.LogError import logerror as logger
from ._object import Object
from ._math.matrix import Matrix
from ._math.triangle import Triangle2D
from ._math.vectors import *
from ._io import Screen


logger.load_core("Engine")
logger.setformat("[{lencalls} {time3}] [{level}]-{CoreType}] &[{function}] -> {message}")


class Aplication( Screen ):
    def __init__(self, 
                 width: int, 
                 height: int, 
                 fps: int = 60, 
                 title: str = None, 
                 icon: str = None
                 ):
        super().__init__(width, height, fps, title, icon) 

        logger.info("__init__ Engine start (width=%s height=%s fps=%.2f title='%s' icon='%s')" % ( width, height, fps, title, icon ))
        self._world: Object = []

        self.__logick()

    def start(self) -> None: ...

    def __logick(self):
        
        logger.info("open start function")
        self.start()

        pass


    def DrawTriangle(self, triangle: Triangle2D, c, color):
        _vec1, _vec2, _vec3 = triangle.getpoints()
        
        self.DrawLine(_vec1, _vec2, c, color)
        self.DrawLine(_vec2, _vec3, c, color)
        self.DrawLine(_vec3, _vec1, c, color)

    @logger.catch
    def run(self):
        while True:
            self.frame_update()