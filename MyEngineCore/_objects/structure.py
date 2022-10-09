from MyEngineCore._math.triangle import Triangle3D
from MyEngineCore._math.vectors import Vector3D

from BaseModule.BaseModule import mjoin

class structur_object:
    def __init__(self, position: Vector3D, angle: Vector3D, *triangles: Triangle3D):
        self.object_position = position
        self.object_angle = angle
        self.object_triangles = triangles
    
    def __repr__(self) -> str:
        return "<_obects.structur_object position=%s, angle=%s, triangles=%s>" % ( 
            0,0,0
        )