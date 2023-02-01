![Logo](icons/MyEngine.png)

## MyEngin

### install

<!-- - `git clone https://github.com/777Chara777/MyEngine.git` -->
- `import MyEngine as mycore`

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