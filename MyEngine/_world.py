from ._object import ObjectNameTag, Object

from ._math.vectors import Vector3D
from ._math.triangle import Triangle3D
from ._math.mash import Mash

from ._utils.BaseModule.LogError import logerror

from ._physics import RigidBody

logerror.load_core("Engine")


class World:
    def __init__(self):
        self.__objects: "dict[int, Object]" = {}
        self.__namelist: "list[ObjectNameTag]" = []

        logerror.info("__init__::World")

    def __len__(self):
        return len(self.__objects)

    @property
    def get_objects(self):
        return self.__objects.copy()

    def importBody(self, tag: ObjectNameTag ) -> "Object | None":
        if not isinstance(tag, ObjectNameTag):
            return None

        if tag not in self.__namelist:
            logerror.error(f"Don't find body '{tag.gettag()}'")
            return None
        
        return self.__objects[tag]

    def loadBody(self, tag: ObjectNameTag, path: str, position: Vector3D=Vector3D(), angle: Vector3D=Vector3D()) -> "Object | None":

        if not isinstance(tag, ObjectNameTag):
            return
        
        if tag in self.__namelist:
            logerror.warn("This tag (%s) is already in use, please try another one." % tag.gettag())
            return
        
        self.__namelist.append(
            tag
        )

        mash = Mash()
        list_points    = []
        list_triangles = []
        
        with open(path, "r") as obj:
            for line in obj.readlines():
                if line.startswith("v"): # v это буфер тут хронятся точки  
                    list_points.append(Vector3D(
                        *[float(x) for x in line.split()[1:]]
                    ))
                elif line.startswith("f"): # f это точки из буфера
                    list_triangles.append(Vector3D(
                        *[int(x)-1 for x in line.split()[1:]]
                    ))
        
        for triangle in list_triangles:
            mash.add(Triangle3D(*[ list_points[p] for p in triangle]))


        self.__objects[hash(tag)] = Object( position, angle, mash, hash(tag) )
        return self.__objects[hash(tag)]

    def removeBody(self, tag: ObjectNameTag ):
        if tag.get_hash in self.__objects:
            logerror.info("Removed body '%s'" % tag.get_tag)
            del self.__objects[tag.get_hash]
        else:
            logerror.warn("Cannot remove body '%s': body does not exist." % tag.get_tag)


    def checkBody(self, tag: ObjectNameTag ) -> bool:
        return tag.get_hash in self.__objects


    # def checkCollision(self, tag: ObjectNameTag) -> bool:
    #     pass