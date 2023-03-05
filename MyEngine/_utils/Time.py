import time
from .. import Consts

from .._utils.Timer import Timer, NotFindTimer
from .._utils.BaseModule.LogError import logerror


logerror.load_core("Engine")

class ticks:
    tickslist: dict[str, ] = {} 

    def add_Short_tick(self, function): pass
    def add_Second_tick(self, function): pass
    def add_Long_tick(self, function): pass
    def add_Extreame_tick(self, function): pass


class Time:
    def __init__(self) -> None:        
        logerror.info("__init__::Time")

        self._timers: dict[str, Timer] = {}

        self._start        = time.time()
        self._last         = self._start

        self._fpsStart     = self._start
        self._fpsCountTime = 0.001
        # self._fpsCountTime = 1
        self._fpsCounter   = 0
        self._fpsControler = None
        self._lastFps      = 0.0

        self._time         = 0
        self._deltaTime    = 0
    
    @property
    def time(self):
        return self._time

    @property
    def deltaTime(self):
        return self._deltaTime

    @property
    def fps(self) -> float:
        return self._lastFps

    def update_tick(self, fps: "int | None"=None):
        self._fpsControler = fps
        
        t = time.time()

        self._deltaTime = (t - self._last)
        self._time = (t - self._start)
        if (self._deltaTime > Consts.LARGEST_TIME_STEP):
            self._deltaTime = Consts.LARGEST_TIME_STEP

        self._last = t

        if (self._deltaTime > 10): return

        
        if self._fpsControler is not None:
            time.sleep(1/ self._fpsControler)

        self._fpsCounter += 1
        if t - self._fpsStart > self._fpsCountTime:
            self._lastFps = self._fpsCounter / (t - self._fpsStart)
            self._fpsCounter = 0
            self._fpsStart = t
        



    def startTimer(self, tag: str):
        if tag not in self._timers:
            self._timers[tag] = Timer(f"{self.__class__.__name__}: {tag}")
        self._timers[tag].start()

    def stopTimer(self, tag: str):
        if tag not in self._timers:
            raise NotFindTimer("not find '%s' timer" % tag)
        self._timers[tag].stop()


    def elapsedTimerMilliseconds(self, tag: str) -> float:
        if tag not in self._timers:
            raise NotFindTimer("not find '%s' timer" % tag)
        return self._timers[tag].elapsedMilliseconds

    def elapsedTimerSeconds(self, tag: str)  -> float:
        if tag not in self._timers:
            raise NotFindTimer("not find '%s' timer" % tag)
        return self._timers[tag].elapsedSeconds
    
    def free(self):
        self._timers.clear()
        del self