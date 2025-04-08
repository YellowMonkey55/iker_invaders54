from pyray import *
from raylib import *
from texture import taco_texture

class projectile:
    def __init__(self, pos):
        self.pos = pos
        self.texture = taco_texture
        self.active = True
        self.rectangle = None

    def update(self):

        # draw_rectangle(int(self.pos.x), int(self.pos.y), 70, 50, (0, 0, 0, 100))

        dt = get_frame_time()

        self.pos.y -= int(get_monitor_height(get_current_monitor()) * 0.86 * dt)

        if self.pos.y < get_monitor_height(get_current_monitor()) * 0.05: 
            self.active = False

    def draw(self):
        # draw_texture_v(self.texture, self.pos, WHITE)

        self.rectangle = Rectangle(self.pos.x, 
                      self.pos.y, 
                      get_monitor_width(get_current_monitor()) * 0.06, 
                      get_monitor_height(get_current_monitor()) * 0.05)

        draw_texture_pro(

            self.texture,

            Rectangle(0, 0, self.texture.width, self.texture.height),

            self.rectangle,

            Vector2(get_monitor_width(get_current_monitor()) * 0.06 / 2, get_monitor_height(get_current_monitor()) * 0.05 / 2),

            0,

            WHITE
        )
    
        