from ._math.mash import Mash
from ._math.matrix import Matrix
from ._math.vectors import Vector3D

class ObjectNameTag:
    def __init__(self, tag) -> None:
        self._name = tag

    # def 

class Object:
    def __init__(self, position: Vector3D, angle: Vector3D, mash: Mash):
        self.object_position: Vector3D = position
        self.object_angle:    Vector3D = angle
        self.object_mash:         Mash = mash
    
    def __repr__(self) -> str:
        return "<object position=%s, angle=%s, mash=%s>" % ( 
            self.object_position, self.object_angle, self.object_mash
        )
    
    def translate(self, pos: Vector3D):
        if not isinstance(pos, Vector3D):
            raise TypeError("pos is {pos.__class__.__name__} but this is most Vector3D")
        self.position = pos

