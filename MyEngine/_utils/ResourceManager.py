from .._utils.BaseModule.LogError import logerror
from .._utils.BaseModule import BaseModule as bm

from pygame.font import SysFont, Font

logerror.load_core("Engine")


class Resource:
    def __init__(self, name: str, quantity):
        self.name     = name
        
        self.quantity = quantity
        self.size     = quantity.__sizeof__()

    def __str__(self) -> str:
        return "< %s name=%s, quantity=%s, size=%s >" % (
            self.__class__.__name__,
            self.name,
            self.quantity,
            self.size
        )

class ResourceManager:
    def __init__(self):
        
        self._soundBuffers = {}
        self._textures     = {}
        self._objects      = {}
        self._fonts        = {}

        logerror.info("__init__::ResourceManager")


    def loadTextures(self, file: str): pass

    def loadSoundBuffers(self, file: str): pass

    def loadFonts(self, file: str, size) -> str:
        if file not in self._fonts:
            self._fonts[file] = SysFont(file, size)
        return self._fonts[file]


    def unloadTextures(self, file: str): pass

    def unloadSoundBuffers(self, file: str): pass

    def unloadFonts(self, file: str): pass