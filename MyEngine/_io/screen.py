import pygame as pg
from .._utils.BaseModule.BaseModule import misfile
from .._utils.BaseModule.LogError import logerror

from .._math.vectors import Vector2D


class _clock:
    def __init__(self) -> None:
        self.clock = pg.time.Clock()
        pass

    def __repr__ (self) -> str:
        return "<screen.clock fps=%.2f>" % self.clock.get_fps()

    def get_fps(self) -> float:
        return self.clock.get_fps()

    def update_tick(self, FPS: int):
        self.clock.tick(FPS)

class Screen:
    def __init__(self, width: int, height: int, fps: int=60, title: str=None, icon: str=None):
        self.size = (width, height)
        self.FPS = fps
        self.app_title = title if title is not None else __file__
        self.app_icon  = icon

        self.clock = _clock()

        self.setup()

    def DrawLine(self, vec1: Vector2D, vec2: Vector2D, c: int, color: tuple=(255,255,255)):
        pg.draw.line(self.screen, color, (vec1.x,vec1.y), (vec2.x, vec2.y), c)
    
    def setup(self):
        pg.init()
        pg.display.set_caption(self.app_title)
        if self.app_icon is not None and misfile(self.app_icon):
            app_icon = pg.image.load(self.app_icon)
            pg.display.set_icon(app_icon)

        self.screen = pg.display.set_mode(self.size)

    def update_title(self, title: str):
        pg.display.set_caption(title)

    def on_update(self): pass
        
    def frame_update(self):
        [exit(0) for x in pg.event.get() if x.type == pg.QUIT]

        self.on_update()

        pg.display.flip()
        pg.display.update()
        self.clock.update_tick(self.FPS)


