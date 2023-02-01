from ._math.mash import Mash
from ._math.matrix import Matrix
from ._math.vectors import Vector3D


class Object:
    def __init__(self, position: Vector3D, angle: Vector3D, *mash: Mash):
        self.object_position = position
        self.object_angle = angle
        self.object_mashs = mash
    
    def __repr__(self) -> str:
        return "<object position=%s, angle=%s, mashs=%s>" % ( 
            self.object_position, self.object_angle, len(self.object_mashs)
        )