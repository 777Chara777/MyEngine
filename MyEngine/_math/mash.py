from .triangle import Triangle2D, Triangle3D


class typeMash: 

    def __repr__(self) -> str:
        return "<_math.mash.type_mash it's how dict format >"

    def __len__(self):
        return len(self.__dict__)

    def __setitem__(self, __name, __value): 
        self.__dict__[__name] = __value
    
    def __getitem__(self, __name):
        return self.__dict__[__name]

    def __delitem__(self, __name):
        del self.__dict__[__name]

    def __contains__(self, item):
        if item in self.__dict__: return True
        return False
    
    def __iter__(self):
        return iter(self.__dict__)

    def keys(self):
        return self.__dict__.keys()

class Mash:
    def __init__(self) -> None:
        self.objects: "list[Triangle3D | Triangle2D]" = []

    def add(self, *list_triangle: list["Triangle3D | Triangle2D"]):
        self.objects += list_triangle
    
    def free(self):
        del self


class Mash2:
    def __init__(self):
        self.obecks = typeMash()

    def add(self, caption: str , *list_triangle: list["Triangle3D | Triangle2D"]):
        if caption not in self.obecks:
            self.obecks[caption] = list_triangle if len( list_triangle ) != 1 else list_triangle[0]
            return 
        raise Exception(f"This name is already taken -> '{caption}' use another!")
    
    def remove(self, caption: str):
        del self.obecks[caption]
    
    def __len__(self):
        return len(self.obecks)

    def __repr__(self) -> str:
        return "<_math.mash len=%s obecks=%s>" % (len(self.obecks), [str(mash) for mash in self.obecks])
    
    def __iter__(self):
        return iter(self.obecks.keys())

    def __getitem__(self, __value):
        return self.obecks[__value]
    
    def __setitem__(self, __value, __new_value):
        self.obecks[__value] = __new_value