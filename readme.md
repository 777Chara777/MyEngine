![Logo](icons/MyEngine.png)

## MyEngine

- use python module [BaseModule](https://github.com/777Chara777/BaseModule)
- use python module [PyGame](https://pypi.org/project/pygame/)
- create 2D or 3D games in Windows

### How to create a Window and create Triangle
```py
# python 3.9 => 3.11
import MyEngine as mycore

from MyEngine._math.triangle import Triangle2D
from MyEngine._math.vectors import Vector2D

class myapp(mycore.Aplication):
    def __init__(self, width: int, height: int, fps: int = 60, title: str = "Test game", icon: str = None):
        super().__init__(width, height, fps, title, icon)

    def start(self):
        # first call
        self.FPS = 20 # I edit fps with 60 to 20

    def on_update(self):
        # update window title
        self.update_title("FPS: %.2f" % (self.clock.get_fps())) 

        # draw a triangle on the window
        self.DrawTriangle( Triangle2D(
                Vector2D(200,100), 
                Vector2D(400,100), 
                Vector2D(200,200)
            ), 1, (255,255,255) ) 
        
if __name__ == "__main__":
    myapp(600, 600).run()
```

![Window](icons/window.png)

# Plan how it will work


## Create Project
```
[input]: python MyEngine --create [path] 
[out]  : create settings.yml wait
[out]  : Done
```
## Build Project
```
[input]: python MyEngine --build [main skript] -name [name]
[out]  : Done create [name].exe
```

## Source.py
```python
import MyEngine as core

from core.types import ObjectNameTag
from core.math.vectors import Vector3D

class BackRooms(core.Engine):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.Camera.translate(Vector3D(1,1,1))


        self.loadScript(name="/scripts/test.py", tag="testfunc") # -> return script pointer
        fun_test = self.getFunction["testfunc"]
        fun_test.test_func("test message") # call function in 'test.py' script


        cube = self.World.loadBody( tag=ObjectNameTag("Cube"), path="/objects/cube.obj", position=Vector3D(0,0,0) ) # load in world cube, return object pointer

        # Test with monkey
        monkey = self.World.importBody( tag=ObjectNameTag("monkey") ) # import with world monkey, return object pointer
        fun_test.move_object( pos3d=Vector3D(1,4,5), object=monkey ) # return False

        monkey = self.World.loadBody( tag=ObjectNameTag("monkey"), path="/objects/monkey.obj",  position=Vector3D(0,0,0) ) # load in world monkey, return object pointer
        fun_test.move_object( pos3d=Vector3D(1,4,5), object=monkey ) # return True

        # translate - set new position for cube
        cube.translate(Vector3D(0,0,3))

        fun_test.newpos()  # call function in 'test.py' script
    
    def debug(self, *args):
        pass

    def update(self):
        self.update_title("%s FPS %.2f" % (self.get_title, self.clock.get_fps))

        self.keybord.on_press(key="exit", fun=exit)
        self.keybord.on_press(key="F1",   fun=self.debug, args=())
    

if __name__ == "__main__":
    BackRooms.run()

```

## scripts/test.py
```python

from MyEngine.core import Engine

class Test:
    def __init__(self, core: Engine):
        self._core: Engine = core

    def test_func(self, ctx):
        print(ctx)
    
    def move_object(self, pos3d, object) -> bool:
        if object is not None:
            object.translate( pos3d )
            return True
        return False


    def newpos(self):
        cube = self._core.World.importBody( tag=ObjectNameTag("Cube") ) # import from world cube, return object pointer
        # translate - set new position for object
        cube.translate( cube.position+Vector3D(5,4,3) )

def setup(core):
    core.add_Script(Test)

```

## settings.yml
```yml
# author lick
author_link: "https://github.com/777Chara777"

# name project
title: "My Game :)"
description: "Test description"

# version project
version: 1.0.0
# icon project
icon: "./assets/game_icon5_64x64.png"
# build path project
build: "./.build/"
# os list project
os: 
- "Windows 32-64"

# fps project
fps: 60
# size project
width: 900
height: 700
```