from .types.type_world import ObjectNameTag

from ._utils.BaseModule.LogError import logerror

logerror.load_core("Engine")

class World:
    def __init__(self):
        self._objects: dict = {}

    def addBody(self, tag: ObjectNameTag ):
        pass

    def removeBody(self, tag: ObjectNameTag):
        if tag in self._objects:
            logerror.info("removed body '%s'" % tag)
        else:
            logerror.warn("cannot remove body '%s': body does not exist." % tag)

    def loadBody(self, tag: ObjectNameTag, filename):
        self._objects

    def checkCollision(self, tag: ObjectNameTag):
        pass