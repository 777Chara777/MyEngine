from ._utils.BaseModule import BaseModule as bm
from ._utils.BaseModule.LogError import logerror as logger
from ._utils.ResourceManager import ResourceManager
from ._utils.Script import Script
from ._utils.Timer import Timer


from ._object import Object
from ._camera import Camera 
from ._world import World
from ._render import Render


from ._io import Screen
from ._io import Keyboard

from ._math.matrix import Matrix
from ._math.triangle import Triangle2D
from ._math.vectors import *

import time as sys_time
import psutil


__all__ = (
    "Aplication",
)


logger.load_core("Engine")
logger.setformat("[{lencalls}\t {time3}] [{level}\t]-{coretype}] &[{function}] -> {message}")
logger.setlevel("DEBUG")


class Aplication( Screen ):
    _start = sys_time.time()

    def __init__(self, 
                 width: int, 
                 height: int, 
                 fps: int = 60, 
                 title: str = None, 
                 icon: str = None
                 ):
        
        logger.info("__init__::Engine (w=%s, h=%s, fps=%.1f, title='%s', icon='%s')" % ( width, height, fps, title, icon ))

        self._width  = width
        self._height = height
        self._fps    = fps
        self._title  = title

        self._showDebugInfo = False
        self._showDebugInfo_time = sys_time.time()
        
        super().__init__(width, height, fps, title, icon)

        # Inits

        self._ResourceManager = ResourceManager()
        
        self.Camera   = Camera(width, height)
        self.Scripts  = Script(self)
        self.keyboard = Keyboard()
        self.World    = World()
        self.Render   = Render(self)

        # call start function
        logger.info("Call start function")
        self.setup()

    def _on_update_system(self) -> None:
        def switch_Debug():
            if (sys_time.time() - self._showDebugInfo_time) > 0.5:
                self._showDebugInfo_time = sys_time.time()
                self._showDebugInfo = not self._showDebugInfo
        self.keyboard.on_press("f12", switch_Debug )
        
        self._printDebugInfo()


    def _printDebugInfo(self) -> None:

        if not self._showDebugInfo:
            return

        self.drawtext( 
            self._ResourceManager.loadFonts("./_founts/Roboto-Regular.ttf", 23), 
            # f"Camera: {', '.join([(f'{x:.2f}') for x in self.Camera.get_position])}, fps: {self.GameTicks.fps:.2f}, width/height: {self._width}/{self._height}, Objects: {len(self.World._objects)}, Scripts: {self.Scripts.lenScripts()}",
            f"Camera: {', '.join([(f'{x:.2f}') for x in self.Camera.get_position])}, fps: {self.GameTicks.fps:.2f}",
            (255,255,255),
            Vector2D(0,  0) )
        
        self.drawtext( 
            self._ResourceManager.loadFonts("./_founts/Roboto-Regular.ttf", 23), 
            f" width/height: {self._width}/{self._height}, Objects: {len(self.World._objects)}, Scripts: {self.Scripts.lenScripts()}",
            (255,255,255),
            Vector2D(270,0) )
        

        #  TODO: don't work
        # "up", "down", "west", "east", "north", "south"
        # angle = self.Camera.position-self.Camera.get_angle
        # if angle.x >= angle.y and angle.x >= angle.z:
        #     sight = "north"
        # elif -angle.x >= angle.y and -angle.x >= angle.z:
        #     sight = "south"
        # elif angle.z >= angle.y and angle.z >= angle.x:
        #     sight = "west"
        # elif -angle.z >= angle.y and -angle.z >= angle.x:
        #     sight = "east"
        # elif angle.y >= angle.z and angle.y >= angle.x:
        #     sight = "up"
        # elif -angle.y >= angle.z and -angle.y >= angle.x:
        #     sight = "down"
        
        sight = None

        self.drawtext(
            self._ResourceManager.loadFonts("./_founts/Roboto-Regular.ttf", 23), 
            f"angle: {', '.join([(f'{x:.2f}') for x in self.Camera.get_angle])}, sight: {sight}",
            (255,255,255),
            Vector2D(0,23 )
        )

        process = psutil.Process()
        memory_info = process.memory_info()
        memory_usage = memory_info.rss
        memory_usage_mb = memory_usage / 1024 / 1024
        self.drawtext(
                self._ResourceManager.loadFonts("./_founts/Roboto-Regular.ttf", 22), 
                f"Memory: {memory_usage_mb:.2f} MB",
                (242, 255, 0),
                Vector2D(0, int(self._height-60))
            )
        
        work_time = "%s-%02d-%02d-%02d" % bm.SecTimeformat(sys_time.time()-self._start)

        self.drawtext(
                self._ResourceManager.loadFonts("./_founts/Roboto-Regular.ttf", 22), 
                f"Name-Project: '{self.get_title}' Time-Work: {work_time}'",
                (255, 255, 255),
                Vector2D(0, int(self._height-40))
            )

        timers = self.GameTicks.get_timers
        del timers["d all"]

        all_work = self.GameTicks.elapsedTimerMilliseconds("d all")
        if int(all_work) == 0: all_work == 1

        top_list: dict[float, tuple[str, float]] = {}

        for number, timer in enumerate(timers):
            if number > 5:
                break
            time = timers[timer][0].elapsedMilliseconds
            top_list[time] = (timer, time*100 / all_work, timers[timer][1])
        
        list_top_list = sorted(top_list, reverse=True)
        for number, value in enumerate(list_top_list):
            
            path = top_list[value][2] if len(top_list[value][2])<=15 else "..."+top_list[value][2][ (len(top_list[value][2])//2-4): ]
            
            self.drawtext(
                self._ResourceManager.loadFonts("./_founts/Roboto-Regular.ttf", 22), 
                f"{number} {path}: {top_list[value][0]}, time: {value:.02f}, {top_list[value][1]:.01f}%",
                (255,255,255),
                Vector2D(0, int(60+number*15) )
            )


    def start(self) -> None: ...

    @logger.catch
    def run(self):
        while True:
            with self.GameTicks.stopwatch("d all"):

                with self.GameTicks.stopwatch("d on_update"):
                    self._updateframe()

                with self.GameTicks.stopwatch("d on_render"):
                    self.Render.render()

            self._on_update_system()
