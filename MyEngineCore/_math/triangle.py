from .vectors import Vector3D, Vector2D

class Triangle3D:
    def __init__(self, point1: Vector3D, point2: Vector3D, point3: Vector3D) -> None:
        self.points: tuple = (point1, point2, point3)
    
    def getpoints(self) -> "tuple[Vector3D, Vector3D, Vector3D]":
        return self.points

    def __repr__(self) -> str:
        vec_str = ", ".join([ f"{vec.__class__.__name__}="+"{x=%s, y=%s, z=%s}" % (vec.x, vec.y, vec.z) for vec in self.points ])
        return "<_math.Triangle3D points=[%s]>" % vec_str

class Triangle2D:
    def __init__(self, point1: Vector2D, point2: Vector2D, point3: Vector2D) -> None:
        self.points: tuple = (point1, point2, point3)
    
    def getpoints(self) -> "tuple[Vector2D, Vector2D, Vector2D]":
        return self.points

    def __repr__(self) -> str:
        vec_str = ", ".join([ f"{vec.__class__.__name__}="+"{x=%s, y=%s}" % (vec.x, vec.y) for vec in self.points ])
        return "<_math.Triangle2D points=[%s]>" % vec_str