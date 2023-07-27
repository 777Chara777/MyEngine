from .._utils.BaseModule.LogError import logerror
from .._utils.Timer import Timer
from .._utils.Time import Time

from .._math.vectors import Vector3D, Vector2D, GetTriangleNormal, dot
from .._math.triangle import Triangle2D, Triangle3D

from .._world import ObjectNameTag

from .._camera import Camera
from .._world import World

from ctypes import cdll, c_int, byref, c_double, POINTER

import math

logerror.load_core("Engine")



__all__ = (
    "Render",
)

class Render:
    def __init__(self, core) -> None:
        self._core             = core
        self._World:  "World"  = core.World 
        self._Camera: "Camera" = core.Camera

        logerror.info("__init__::Render")

        # TODO: remake
        # self.mylib = cdll.LoadLibrary('.\MyEngine\_render\dll\project.dll')
        # self.mylib.project.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double)]

        # self.width, self.height = self._Camera.width, self._Camera.height

    def project(self, point: Vector3D):

        def rotate2d(pos, angle):
            x, y = pos # 0 1
            s, c = math.sin(angle), math.cos(angle)

            return x*c - y*s, y*c + x*s
        
        
        x, y, z = point.x - self._Camera.get_position.x, point.y - self._Camera.get_position.y, point.z - self._Camera.get_position.z
        
        x, z = rotate2d((x, z), self._Camera.get_angle.x)
        y, z = rotate2d((y, z), self._Camera.get_angle.y)
        
        f = 200 / z
        x, y = x * f, y * f
        return (int(x + self._Camera.width/2), int(y + self._Camera.height/2))

    # def project(self, point: Vector3D):
    #     x, y = c_double(), c_double()

    #     pos_cam = self._Camera.get_position
    #     angle_cam = self._Camera.get_angle

    #     self.mylib.project(*pos_cam, self.width, self.height, angle_cam.x, angle_cam.y, *point, byref(x), byref(y))
    #     return (x.value, y.value)

    def render(self):
        # for object in self._World.get_objects:
        object_ = self._World.importBody(ObjectNameTag("Object"))
        if object_ is None:
            return

        object_position: "Vector3D"             = object_.object_position
        object_angle:    "Vector3D"             = object_.object_angle

        object_mash_triangles: list[Triangle3D] = object_.object_mash.objects

        for edge in object_mash_triangles:
            triangle = list(edge)
            p1 = Triangle2D( *[Vector2D(*self.project(object_position + pos)) for pos in triangle] ) 

            if dot(self._Camera.get_position, GetTriangleNormal( *triangle )) > 0:
                self._core.DrawTriangle(p1, 1, (255, 255, 255))
