from pyray import *
from raylib import *
import random

class powerup:
    def __init__(self, pos, texture_list):
        self.pos = pos
        list_of_powerups = texture_list
        self.type = random.randint(0, 3)
        self.texture = list_of_powerups[self.type]
        self.speed = int(get_monitor_height(get_current_monitor()) * 0.45)
        self.active = True
        self.rectangle = None

    def update(self):

        dt = get_frame_time()

        self.pos.y += self.speed * dt

        if self.pos.y > get_monitor_height(get_current_monitor()) * 0.95:
            self.active = False

    def draw(self):
        
        self.rectangle = Rectangle(self.pos.x, 
                      self.pos.y, 
                      get_monitor_width(get_current_monitor()) * 0.06, 
                      get_monitor_height(get_current_monitor()) * 0.05)


        draw_texture_pro(

            self.texture,

            Rectangle(0, 0, self.texture.width, self.texture.height),

            self.rectangle,

            Vector2(0, 0),

            0,

            WHITE
        )
    

