from raylib import *
from pyray import *

class entity:
    def __init__(self, pos, texture):
        self.pos = pos
        self.texture = texture
        self.speed = int(get_monitor_width(get_current_monitor()) * 0.35)
        self.direction = 1
        self.alive = True
        self.rectangle = None
        self.cooldown = True
        self.timer = get_time()

    def update(self):

        dt = get_frame_time()

        # draw_rectangle(int(self.pos.x), int(self.pos.y), 70, 50, WHITE)
        if self.pos.x < get_monitor_width(get_current_monitor()) * 0.05:
            self.direction *= - 1
            self.pos.x += get_monitor_width(get_current_monitor()) * 0.003
    
        if self.pos.x  > get_monitor_width(get_current_monitor()) * 0.85:
            self.direction *= -1
            self.pos.x -= get_monitor_width(get_current_monitor()) * 0.003

        self.pos.x += self.speed * dt * self.direction    

    def draw(self):

        self.rectangle = Rectangle(self.pos.x, 
                      self.pos.y, 
                      get_monitor_width(get_current_monitor()) * 0.10, 
                      get_monitor_height(get_current_monitor()) * 0.10)
        
        draw_texture_pro(

            self.texture,

            Rectangle(0, 0, self.texture.width, self.texture.height),

            self.rectangle,

            Vector2(0, 0),
            
            0,

            WHITE

        )

class entity_projectile:
    def __init__(self, pos, texture):
        self.pos = pos
        self.texture = texture
        self.active = True
        self.rectangle = None

    def update(self):

        # draw_rectangle(int(self.pos.x), int(self.pos.y), 70, 50, (0, 0, 0, 100))

        dt = get_frame_time()

        self.pos.y += int(get_monitor_height(get_current_monitor()) * 0.86 * dt)

        if self.pos.y > get_monitor_height(get_current_monitor()) * 0.95: 
            self.active = False

    def draw(self):
        # draw_texture_v(self.texture, self.pos, WHITE)

        self.rectangle = Rectangle(self.pos.x, 
                      self.pos.y, 
                      get_monitor_width(get_current_monitor()) * 0.02, 
                      get_monitor_height(get_current_monitor()) * 0.08)

        draw_texture_pro(

            self.texture,

            Rectangle(0, 0, self.texture.width, self.texture.height),

            self.rectangle,

            Vector2(0, 0),

            0,

            WHITE
        )


