from pyray import *
from raylib import *
from player import player
from settings import *
from projectile import *
import random
from entity import *
from powerups import *
from textures import Textures


def loading():
    init_window(int(get_monitor_width(get_current_monitor())), 
               int(get_monitor_height(get_current_monitor())), 
               "Iker Invaders")
    set_target_fps(60)

    main_menu()
    close_window()

def main_menu():
    
    # Colors
    background_color = BLACK
    title_color = WHITE
    button_color = DARKGRAY
    button_hover_color = GRAY
    text_color = WHITE
    
    # Button dimensions
    button_width = int(get_monitor_width(get_current_monitor()) * 0.3)  # 30% of screen width
    button_height = int(get_monitor_height(get_current_monitor()) * 0.1)  # 10% of screen height
    
    # Buttons with relative positioning
    play_button = Rectangle(
        int(get_monitor_width(get_current_monitor()) * 0.35),
        int(get_monitor_height(get_current_monitor()) * 0.4),
        button_width,
        button_height
    )
    
    controls_button = Rectangle(
        int(get_monitor_width(get_current_monitor()) * 0.35),
        int(get_monitor_height(get_current_monitor()) * 0.55),
        button_width,
        button_height
    )
    
    exit_button = Rectangle(
        int(get_monitor_width(get_current_monitor()) * 0.35),
        int(get_monitor_height(get_current_monitor()) * 0.7),
        button_width,
        button_height
    )
    
    show_controls = False
    
    while not window_should_close():
        mouse_pos = get_mouse_position()
        
        # Check button hover states
        play_hover = check_collision_point_rec(mouse_pos, play_button)
        controls_hover = check_collision_point_rec(mouse_pos, controls_button)
        exit_hover = check_collision_point_rec(mouse_pos, exit_button)
        
        # Handle button clicks
        if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
            if play_hover:
                main()
                break
            elif controls_hover:
                show_controls = not show_controls
            elif exit_hover:
                break
        
        begin_drawing()
        clear_background(background_color)
        
        # Draw title
        title_size = int(get_monitor_height(get_current_monitor()) * 0.1)  # 10% of screen height
        draw_text("IKER INVADERS", 
                 int(get_monitor_width(get_current_monitor()) * 0.5 - measure_text("IKER INVADERS", title_size)/2), 
                 int(get_monitor_height(get_current_monitor()) * 0.2), 
                 title_size, 
                 title_color)
        
        if not show_controls:
            # Draw buttons
            draw_rectangle_rec(play_button, button_hover_color if play_hover else button_color)
            draw_rectangle_rec(controls_button, button_hover_color if controls_hover else button_color)
            draw_rectangle_rec(exit_button, button_hover_color if exit_hover else button_color)
            
            # Draw button text
            button_text_size = int(get_monitor_height(get_current_monitor()) * 0.05)  # 5% of screen height
            draw_text("PLAY", 
                     int(play_button.x + play_button.width/2 - measure_text("PLAY", button_text_size)/2), 
                     int(play_button.y + play_button.height/2 - button_text_size/2), 
                     button_text_size, 
                     text_color)
            
            draw_text("CONTROLS", 
                     int(controls_button.x + controls_button.width/2 - measure_text("CONTROLS", button_text_size)/2), 
                     int(controls_button.y + controls_button.height/2 - button_text_size/2), 
                     button_text_size, 
                     text_color)
            
            draw_text("EXIT", 
                     int(exit_button.x + exit_button.width/2 - measure_text("EXIT", button_text_size)/2), 
                     int(exit_button.y + exit_button.height/2 - button_text_size/2), 
                     button_text_size, 
                     text_color)
        else:
            # Draw controls screen
            controls_panel = Rectangle(
                int(get_monitor_width(get_current_monitor()) * 0.2),
                int(get_monitor_height(get_current_monitor()) * 0.2),
                int(get_monitor_width(get_current_monitor()) * 0.6),
                int(get_monitor_height(get_current_monitor()) * 0.6)
            )
            
            draw_rectangle_rec(controls_panel, DARKGRAY)
            
            controls_text = [
                "CONTROLS:", 
                "",
                "Move: A and D Keys",
                "Shoot: SPACEBAR",
                "",
                "Avoid enemy projectiles",
                "Shoot enemies to score points",
                "",
                "Click to return: RETURN"
            ]
            
            text_size = int(get_monitor_height(get_current_monitor()) * 0.03)  # 3% of screen height
            for i, line in enumerate(controls_text):
                draw_text(line, 
                         int(controls_panel.x + controls_panel.width * 0.1),
                         int(controls_panel.y + controls_panel.height * 0.1 + i * text_size * 1.5),
                         text_size,
                         WHITE)
        
        end_drawing()

def main():
    monitor = get_current_monitor()
    screen_width = get_monitor_width(monitor)
    screen_height = get_monitor_height(monitor)
    print("reached here")
    cooldown = False
    spawn_cooldown = False
    powerup_cooldown = False

    health = 10
    shoot_cooldown = 1.25
    
    textures = Textures()
    textures.load_textures()

    heart_texture = load_texture('graphics/heart.png')
    map = load_render_texture(screen_width, screen_height)

    score = 0

    wario = player(Vector2((get_monitor_width(monitor)/2), (get_monitor_height(monitor)/1.2)), textures.player_texture)

    projectiles = []
    entities = []
    entities_projectiles = []
    powerups = []

    while not window_should_close():

        if powerup_cooldown == False:
            powerup_cooldown_timer = get_time()
            powerup_cooldown = True
            powerups.append(powerup(Vector2(
                int(random.randint(1,10) * get_monitor_width(get_current_monitor()) * 0.075),
                int(get_monitor_height(get_current_monitor()) * 0.05),
            ),
            [textures.guacamole_texture, textures.cheese_texture, textures.sourcream_texture, textures.pico_texture]
            ))


        elif powerup_cooldown == True:
            if get_time() - powerup_cooldown_timer > random.randint(10, 20):
                powerup_cooldown = False

            
        if spawn_cooldown == False:

            cooldown_timer = get_time()
            spawn_cooldown = True
            entities.append(entity(Vector2(int(random.randint(1,10) * get_monitor_width(get_current_monitor()) * 0.075), 
                                        int(random.randint(1, 3) * get_monitor_height(get_current_monitor()) * 0.105)),
                                        textures.iker_texture))

        elif spawn_cooldown == True:

            if get_time() - cooldown_timer > (5 / (get_time() * 0.24)):
                spawn_cooldown = False


        # fullscreen = game_set_fullscreen(fullscreen)

        if is_key_down(KEY_SPACE):

            if cooldown == False:

                previous_time = get_time()
                cooldown = True
                projectiles.append(projectile(Vector2(wario.pos.x, wario.pos.y), textures.taco_texture))   

            elif cooldown == True:
                
                if get_time() - previous_time > shoot_cooldown:
                    cooldown = False

        for enti in entities:

            if enti.cooldown == False:
                enti.timer = get_time()
                entities_projectiles.append(entity_projectile(Vector2(enti.pos.x, enti.pos.y), textures.salsa_texture))
                enti.cooldown = True

            elif enti.cooldown == True:
                if get_time() - enti.timer > 0.01:
                    enti.cooldown = False
                
                
        for enti_proj in entities_projectiles:
            try:
                if check_collision_recs(enti_proj.rectangle, wario.rectangle):
                    enti_proj.active = False

                    for enti_proj in entities_projectiles:
                        enti_proj.update()

                    health -= 0

                    if health < 1:
                        close_window()
                        main_menu()
            except:
                pass

        for proj in projectiles:
            for enti in entities:
                try:
                    if check_collision_recs(proj.rectangle, enti.rectangle):
                        proj.active = False
                        enti.alive = False
                        score += 100
                except:
                    pass    

        for enti_proj in entities_projectiles:
            enti_proj.update()

        for proj in projectiles:
            proj.update()
        
        for enti in entities:
            enti.update()

        for pwrup in powerups:
            pwrup.update()

        

        entities = [enti for enti in entities if enti.alive]

        projectiles = [proj for proj in projectiles if proj.active]
        
        entities_projectiles = [proj for proj in entities_projectiles if proj.active]

        powerups = [pwrup for pwrup in powerups if pwrup.active]

        wario.update()

        heart_pos = Vector2(get_monitor_width(get_current_monitor()) * 0.815, 
                            get_monitor_height(get_current_monitor()) * 0.025)
        

        # start of drawing

        begin_drawing()

        for proj in entities_projectiles:
            proj.draw()

        for enti in entities:
            enti.draw()

        for proj in projectiles:
            proj.draw()

        for pwrup in powerups:
            pwrup.draw()

        wario.draw()

        for i in range(health):

            draw_texture_pro(
            heart_texture,

            Rectangle(0, 0, heart_texture.width, heart_texture.height),

            Rectangle(heart_pos.x, 
                      heart_pos.y, 
                      get_monitor_width(get_current_monitor()) * 0.055, 
                      get_monitor_height(get_current_monitor()) * 0.06),

            Vector2(0, 0),
            
            0,
            
            WHITE)

            heart_pos.x += get_monitor_width(get_current_monitor()) * 0.06

        draw_text(
                "Score:", 
                int(get_monitor_width(get_current_monitor()) * 0.025),
                int(get_monitor_height(get_current_monitor()) * 0.025),
                64,
                WHITE)

        draw_text(
                str(score), 
                int(get_monitor_width(get_current_monitor()) * 0.20),
                int(get_monitor_height(get_current_monitor()) * 0.025),
                64,
                WHITE)
        
        draw_text(
                str(wario.stamina), 
                int(get_monitor_width(get_current_monitor()) * 0.5),
                int(get_monitor_height(get_current_monitor()) * 0.5),
                64,
                WHITE)
        
        

        clear_background(BACKGROUND_COLOUR)


        end_drawing()

    # close_window()


if __name__ == '__main__':
    loading()

