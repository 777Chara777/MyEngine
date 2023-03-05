import time

from .._utils.BaseModule.LogError import logerror

logerror.load_core("Engine")

class NotFindTimer(Exception): pass

class Timer:
    def __init__(self, tag) -> None:
        
        logerror.info(f"__init__::Timer {tag=}")

        self._isRunning: bool  = False
        self._startTime: float = None
        self._endTime:   float = None
    
    def start(self):
        self._isRunning = True
        self._startTime = time.time()

    def stop(self):
        self._isRunning = False
        self._endTime   = time.time()

    @property
    def elapsedSeconds(self) -> float:

        if self._isRunning:
            endtime = time.time()
        else:
            endtime = self._endTime

        return (endtime - self._startTime) if self._startTime is not None else None
    
    @property
    def elapsedMilliseconds(self) -> float:
        return self.elapsedSeconds*1000