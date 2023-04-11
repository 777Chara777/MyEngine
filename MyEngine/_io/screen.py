import pygame as pg
from .._utils.BaseModule.BaseModule import misfile
from .._utils.BaseModule.LogError import logerror
from .._utils.ResourceManager import Font
from .._utils.Time import Time

from .._math.vectors import Vector2D
from .._math.triangle import Triangle2D

logerror.load_core("Engine")

class Screen:

    def __init__(self, width: int, height: int, fps: int=60, title: str=None, icon: str=None):
        logerror.info(f"__init__::Screen create (width={width}, height={height})")
        self.__fps = fps
        self.__size = (width, height)
        self.__app_title = title if title is not None else __file__
        self.__app_icon  = icon

        self.GameTicks = Time()
        self.clock = pg.time.Clock()

        self.__setup()

    def __setup(self):
        pg.init()
        pg.display.set_caption(self.__app_title)
        if self.__app_icon is not None and misfile(self.__app_icon):
            app_icon = pg.image.load(self.__app_icon)
            pg.display.set_icon(app_icon)

        self.Screen = pg.display.set_mode(self.__size)

    def update_title(self, title: str):
        pg.display.set_caption(title)

    def DrawLine(self, vec1: Vector2D, vec2: Vector2D, c: int, color: tuple=(255,255,255)):
        pg.draw.line(self.Screen, color, (vec1.x,vec1.y), (vec2.x, vec2.y), c)

    def DrawTriangle(self, triangle: Triangle2D, c, color: tuple[int,int,int]):
        _vec1, _vec2, _vec3 = triangle.getpoints()
        
        self.DrawLine(_vec1, _vec2, c, color)
        self.DrawLine(_vec2, _vec3, c, color)
        self.DrawLine(_vec3, _vec1, c, color)
    
    def drawtext(self, fount: Font, text: str, color: tuple[int,int,int], positions = Vector2D(1,1)):
        img = fount.render(text, True, color)
        self.Screen.blit(img, positions.totuple())

    @property
    def get_title(self) -> str:
        return self.__app_title

    def on_update(self) -> None: ...

    @logerror.catch
    def _updateframe(self):
        # self.GameTicks.startTimer("d all")
        
        [exit(0) for x in pg.event.get() if x.type == pg.QUIT]

        # self.GameTicks.startTimer("d on_update")
        self.on_update()
        # self.GameTicks.stopTimer("d on_update")

        pg.display.flip()
        pg.display.update()

        self.GameTicks.update_tick(self.__fps)

        self.Screen.fill((0, 0, 0))

        # self.GameTicks.stopTimer("d all")