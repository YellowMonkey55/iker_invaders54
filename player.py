from raylib import *
from pyray import * 

class player:
    def __init__(self, pos, texture):
        self.pos = pos
        self.texture = texture
        self.speed = int(get_monitor_width(get_current_monitor()) * 0.35)
        self.direction = Vector2()
        self.rectangle = None
        self.hitbox = None
        self.stamina = 100

    def update(self):
        self.direction.x = int(is_key_down(KEY_D)) - int(is_key_down(KEY_A))
        self.direction = Vector2Normalize(self.direction)

        dt_player = get_frame_time()
        

        if is_key_down(KEY_LEFT_SHIFT):
            self.speed = int(get_monitor_width(get_current_monitor()) * 0.70)
        
        elif is_key_released(KEY_LEFT_SHIFT):
            self.speed = int(get_monitor_width(get_current_monitor()) * 0.35)


        


        if get_monitor_width(get_current_monitor()) * 0.05 < self.pos.x < get_monitor_width(get_current_monitor()) * 0.90:
            self.pos.x += self.direction.x * self.speed * dt_player

        elif self.pos.x < get_monitor_width(get_current_monitor()) * 0.90 and self.direction.x == 1:
            self.pos.x += self.direction.x * self.speed * dt_player

        elif get_monitor_width(get_current_monitor()) * 0.05 < self.pos.x and self.direction.x == -1:
            self.pos.x += self.direction.x * self.speed * dt_player

        # self.hitbox = draw_rectangle(int(self.pos.x - get_monitor_width(get_current_monitor()) * 0.025), 
        #                int(self.pos.y - get_monitor_height(get_current_monitor()) * 0.02), 
        #                int(get_monitor_width(get_current_monitor()) * 0.10), 
        #                int(get_monitor_height(get_current_monitor()) * 0.08), 
        #                (0, 0, 0, 255))
        



    def draw(self):

        self.rectangle = Rectangle(
                self.pos.x, 
                self.pos.y, 
                get_monitor_width(get_current_monitor()) * 0.12, 
                get_monitor_height(get_current_monitor()) * 0.0924)
        
        draw_texture_pro(
            self.texture,

            Rectangle(0, 0, self.texture.width, self.texture.height),

            self.rectangle,

            Vector2(0, 0),
            
            0,
            
            WHITE
        )

        # draw_texture_ex(self.texture, self.pos, 0, 0.30, WHITE)

