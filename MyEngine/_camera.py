from ._utils.BaseModule.LogError import logerror

from ._math.vectors import Vector3D

logerror.load_core("Engine")


class Camera:
    def __init__(self, width: int, height: int) -> None:
        logerror.info("__init__::Camera")
        
        self.width  = width
        self.height = height

        self.position = Vector3D()
    
    @property
    def get_position(self):
        return self.position

    def translate(self, pos: Vector3D):
        if not isinstance(pos, Vector3D):
            raise TypeError("pos is {pos.__class__.__name__} but this is most Vector3D")
        self.position = pos