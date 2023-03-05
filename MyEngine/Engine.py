from ._utils.BaseModule import BaseModule as bm
from ._utils.BaseModule.LogError import logerror as logger
from ._utils.ResourceManager import ResourceManager
from ._utils.Timer import Timer

from ._object import Object
from ._camera import Camera 
from ._world import World


from ._io import Screen
from ._io import Keyboard

from ._math.matrix import Matrix
from ._math.triangle import Triangle2D
from ._math.vectors import *







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
        
        logger.info("__init__::Engine start (%s %s %.2f '%s' '%s')" % ( width, height, fps, title, icon ))

        self._width  = width
        self._height = height
        self._fps    = fps
        self._title  = title

        self._showDebugInfo = False
        
        super().__init__(width, height, fps, title, icon)

        # Inits

        self._ResourceManager = ResourceManager()
        
        self.Camera   = Camera(width, height)
        self.keyboard = Keyboard()
        self.World    = World()

        # call start function
        logger.info("call start function")
        self.start()

    def _on_update_system(self) -> None:
        def switch_Debug():
            self._showDebugInfo = not self._showDebugInfo
        self.keyboard.on_press("f12", switch_Debug )
        
        self._printDebugInfo()


    def _printDebugInfo(self) -> None:

        if self._showDebugInfo:
            text = f"Camera: {self.Camera.get_position} fps: {self.GameTicks.fps:.2f}, width/height: {self._width}/{self._height} Objects: {len(self.World._objects)}"

            self.drawtext( 
                self._ResourceManager.loadFonts("./_founts/Roboto-Regular.ttf", 24), 
                text, (255,255,255), 
                Vector2D(0,0) )




    def start(self) -> None: ...

    @logger.catch
    def run(self):
        while True:
            self._on_update_system()
            self._updateframe()
