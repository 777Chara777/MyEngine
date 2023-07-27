from ._utils.BaseModule.LogError import logerror

from ._math.vectors import Vector3D


logerror.load_core("Engine")


class Camera:
    def __init__(self, width: int, height: int, position: Vector3D=Vector3D(), fov=90, angle: Vector3D=Vector3D()) -> None:
        logerror.info("__init__::Camera")
        
        self.width    = width
        self.height   = height
        self.fov      = fov

        self.position = position
        self.angle    = angle

    @property
    def get_fov(self) -> "int":
        return self.fov

    @property
    def get_position(self) -> "Vector3D":
        return self.position.copy()

    @property
    def get_angle(self) -> "Vector3D":
        return self.angle.copy()

    def translate(self, pos: Vector3D):
        if not isinstance(pos, Vector3D):
            raise TypeError(f"pos is {pos.__class__.__name__} but this is most Vector3D")
        self.position = pos
    
    def rotate(self, angle: Vector3D):
        if not isinstance(angle, Vector3D):
            raise TypeError(f"angle is {angle.__class__.__name__} but this is most Vector3D")
        self.angle = angle

