from ._utils import BaseModule as bm
# from ._network.server import socket_server
# from ._network.client import socket_client
from ._utils._LogError import logerror as logger
from ._math.mash import mash_list
from ._math.matrix import Matrix
from ._math.triangle import Triangle2D
from ._math.vectors import *
from ._screen import Screen


class Aplication(Screen):
    def __init__(self, width: int, height: int, fps: int = 60, title: str = "Test game", icon: str = None):
        super().__init__(width, height, fps, title, icon)
    
    def DrawTriangle(self, triangle: Triangle2D, c, color):
        _vec1, _vec2, _vec3 = triangle.getpoints()
        
        self.DrawLine(_vec1, _vec2, c, color)
        self.DrawLine(_vec2, _vec3, c, color)
        self.DrawLine(_vec3, _vec1, c, color)

        

    @logger.catch
    def run(self):
        while True:
            self.frame_update()