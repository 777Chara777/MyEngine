![Logo](icons/MyEngine.png)

## MyEngine

- use python module [BaseModule](https://github.com/777Chara777/BaseModule)
- use python module [PyGame](https://pypi.org/project/pygame/)
- create 2D or 3D games in Windows

### How to create a Window and render Cube
```py
# python 3.9 => 3.11
import MyEngine as mycore

from MyEngine._math.vectors import Vector3D as vec3


mycore.logger.load_core("Engine")

class TestCube(core.Aplication):
    def __init__(self, width: int, height: int, fps: int = 60, title: str = None, icon: str = None):
        super().__init__(width, height, fps, title, icon)

    def setup(self):
        self.object_1 = self.World.loadBody( mycore.ObjectNameTag("Object"), "./obj/cube.obj")
        self.Camera.translate(vec3(0,0,-10))

        self.player = self.Scripts.loadScripts("scripts.player_controller", "PlayerController")


    @mycore.logger.catch( message="Error in Engine while :(", ignore_exceptions=(SystemExit, KeyboardInterrupt,), onerror=lambda _: exit(0) )
    def on_update(self):
        self.player.move()


if __name__ == "__main__":
    TestCube(900,700, title="Test Cube").run()
```

scripts.player_controller
```py
from MyEngine._math.vectors import Vector3D as vec3
from MyEngine._world import ObjectNameTag

from Source import TestCube

class Test:
    def __init__(self, core) -> None:
        self._core: "TestCube" = core

    def move(self):

        if self._core.keyboard.on_press("w"):
            self._core.Camera.position += vec3(0, 0, 0.1)

        if self._core.keyboard.on_press("s"):
            self._core.Camera.position -= vec3(0, 0, 0.1)

        if self._core.keyboard.on_press("a"):
            self._core.Camera.position -= vec3(0.1, 0, 0)

        if self._core.keyboard.on_press("d"):
            self._core.Camera.position += vec3(0.1, 0, 0)


        if self._core.keyboard.on_press("space"):
            self._core.Camera.position -= vec3(0, 0.1, 0)

        if self._core.keyboard.on_press("left shift"):
            self._core.Camera.position += vec3(0, 0.1, 0)


        if self._core.keyboard.on_press("right"):
            self._core.Camera.angle += vec3(0.1, 0, 0)

        if self._core.keyboard.on_press("left"):
            self._core.Camera.angle -= vec3(0.1, 0, 0)

        if self._core.keyboard.on_press("up"):
            self._core.Camera.angle -= vec3(0, 0.1, 0)

        if self._core.keyboard.on_press("down"):
            self._core.Camera.angle += vec3(0, 0.1, 0)

def setup(core):
    core.add_Script(Test)

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