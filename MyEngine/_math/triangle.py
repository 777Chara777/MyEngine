from .vectors import Vector2D, Vector3D

__all__ = (
    "Triangle3D",
    "Triangle2D",
)

class Triangle3D:
    def __init__(self, point1: Vector3D, point2: Vector3D, point3: Vector3D) -> None:
        self.points: "tuple[Vector3D, Vector3D, Vector3D]" = (point1, point2, point3,)
    
    def getpoints(self) -> "tuple[Vector3D, Vector3D, Vector3D]":
        return self.points
    
    def __add__(self, other: Vector3D):
        if not isinstance(other, Vector3D):
            raise ValueError(f"type `{other}` is not `Vector3D`!")
        return self.__class__(*[vec + other for vec in self.points ])

    def __iadd__(self, other: Vector3D):
        return self.__add__(other)

    def __sub__(self, other: Vector3D):
        if not isinstance(other, Vector3D):
            raise ValueError(f"type `{other}` is not `Vector3D`!")
        return self.__class__(*[vec - other for vec in self.points ])
            

        
    
    def __isub__(self, other: Vector3D):
        return self.__sub__(other)
    

    def __iter__(self):
        return iter(self.points)

    def __repr__(self) -> str:
        vec_str = ", ".join([ f"{vec.__class__.__name__}="+"{x=%s, y=%s, z=%s}" % (vec.x, vec.y, vec.z) for vec in self.points ])
        return "<_math.Triangle3D points=[%s]>" % vec_str

class Triangle2D:
    def __init__(self, point1: Vector2D, point2: Vector2D, point3: Vector2D) -> None:
        self.points: tuple = (point1, point2, point3)
    
    def getpoints(self) -> "tuple[Vector2D, Vector2D, Vector2D]":
        return self.points

    
    def __add__(self, other: Vector2D):
        if not isinstance(other, Vector2D):
            raise ValueError(f"type `{other}` is not `Vector2D`!")
        return self.__class__(*[vec + other for vec in self.points ])
    
    def __iadd__(self, other: Vector2D):
        return self.__add__(other)

    def __sub__(self, other: Vector2D):
        if not isinstance(other, Vector2D):
            raise ValueError(f"type `{other}` is not `Vector2D`!")
        return self.__class__(*[vec - other for vec in self.points ])
    
    def __isub__(self, other: Vector2D):
        return self.__sub__(other)
    

    def __iter__(self):
        return iter(self.points)

    def __repr__(self) -> str:
        vec_str = ", ".join([ f"{vec.__class__.__name__}="+"{x=%s, y=%s}" % (vec.x, vec.y) for vec in self.points ])
        return "<_math.Triangle2D points=[%s]>" % vec_str