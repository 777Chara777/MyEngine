from ._math.vectors import Vector3D
from ._math.mash import Mash

from ._utils.BaseModule.LogError import logerror

logerror.load_core("Engine")

class ObjectNameTag:
    def __init__(self, tag: str) -> None:
        self.__TAG = tag

    def __repr__(self) -> str:
        return "<ObjectNameTag tag=%s, hash=%i, id=%i>" % self.gettag(), self.__hash__(), id(self.__hash__())

    def __str__(self) -> str:
        return "<ObjectNameTag tag=%s>" % self.gettag()

    def __hash__(self) -> int:
        return hash(self.gettag())

    def gettag(self) -> str:
        return self.__TAG


class Object:
    def __init__(self, position: Vector3D, angle: Vector3D, mash: Mash, _hash: str):
        self.object_position: Vector3D = position
        self.object_angle:    Vector3D = angle
        self.object_mash:         Mash = mash
        self.object_hash:          str = _hash
    
    def __repr__(self) -> str:
        return "<Object name=%s, hash=%i, id=%i, position=%s, angle=%s, mash=%s>" % ( 
            self.object_hash, 
            self.__hash__(),
            id(self.__hash__()),
            self.object_position, 
            self.object_angle, 
            self.object_mash
        )
    
    @property
    def name(self) -> int:
        return self.object_hash
    
    def translate(self, pos: Vector3D):
        if not isinstance(pos, Vector3D):
            raise TypeError(f"Position is {pos.__class__.__name__} but this is most Vector3D")
        self.object_position = pos

    def scale(self, angle: Vector3D):
        if not isinstance(angle, Vector3D):
            raise TypeError(f"scale is {angle.__class__.__name__} but this is most Vector3D")
        self.object_angle = angle


    def __hash__(self) -> int:
        return hash(
            tuple(self.object_hash, self.object_mash)
        )
    
    
