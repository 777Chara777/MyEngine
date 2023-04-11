from ._object import ObjectNameTag, Object

from ._math.vectors import Vector3D
from ._math.triangle import Triangle3D
from ._math.mash import Mash

from ._utils.BaseModule.LogError import logerror

logerror.load_core("Engine")

class WorldObjectBody:
    def __init__(self, position: Vector3D=Vector3D()) -> None:
        self._position: Vector3D = position

    @property
    def position(self) -> Vector3D:
        return self._position

    def translate(self, position: Vector3D):
        self._position = position
        pass

class World:
    def __init__(self):
        self._objects: "dict[str, Object]" = {}

        logerror.info("__init__::World")

    def importBody(self, tag: ObjectNameTag ) -> "Object | None":
        if not isinstance(tag, ObjectNameTag):
            return None

        if tag.get_tag not in self._objects:
            logerror.error(f"Don't find body '{tag.get_tag}'")
            return None
        
        return self._objects[tag.get_tag]

    def loadBody(self, tag: ObjectNameTag, path: str, position: Vector3D=Vector3D(), angle: Vector3D=Vector3D()) -> "Object | None":

        if not isinstance(tag, ObjectNameTag):
            return None
        
        if tag.get_tag is self._objects:
            logerror.warn("This tag (%s) is already in use, please try another one." % tag.get_tag)
            return

        mash = Mash()
        list_points    = []
        list_triangles = []
        
        with open(path, "r") as obj:
            for line in obj.readlines():
                if line.startswith("v"):
                    list_points.append(Vector3D(
                        *[float(x) for x in line.split()[1:]]
                    ))
                elif line.startswith("f"):
                    list_triangles.append(Vector3D(
                        *[int(x)-1 for x in line.split()[1:]]
                    ))
        
        for triangle in list_triangles:
            mash.add(Triangle3D(*[ list_points[p] for p in triangle]))


        self._objects[tag.get_tag] = Object( position, angle, mash )
        return self._objects[tag.get_tag]

    def removeBody(self, tag: ObjectNameTag ):
        if tag.get_tag in self._objects:
            logerror.info("removed body '%s'" % tag.get_tag)
            del self._objects[tag.get_tag]
        else:
            logerror.warn("cannot remove body '%s': body does not exist." % tag.get_tag)

    def checkBody(self, tag: ObjectNameTag ) -> bool:
        return tag.get_tag in self._objects


    def checkCollision(self, tag: ObjectNameTag) -> bool:
        pass