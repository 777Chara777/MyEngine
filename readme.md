### MyEngin V1.0

- have
- network
- BaseModule
- base math

### how use?
```py
import MyEngineCore as mycore

from MyEngineCore._math.triangle import Triangle2D
from MyEngineCore._math.vectors import Vector2D

class myapp(mycore.Aplication):
    def __init__(self, width: int, height: int, fps: int = 60, title: str = "Test game", icon: str = None):
        super().__init__(width, height, fps, title, icon)

    def on_update(self):
        self.update_title("FPS: %.2f" % (self.clock.get_fps()))

        self.DrawTriangle( Triangle2D(Vector2D(200,100), Vector2D(400,100), Vector2D(200,200)), 1, (255,255,255) )
        
if __name__ == "__main__":
    myapp(600, 600).run()
```

![Logo](icons/window.png)