from pyray import *
from raylib import *


player_texture = None
guacamole_texture = None
cheese_texture = None
sourcream_texture = None
taco_texture = None
iker_texture = None
pico_texture = None
salsa_texture = None


def game_load_textures():
    global player_texture, guacamole_texture, cheese_texture, sourcream_texture, pico_texture, taco_texture, iker_texture, salsa_texture
    player_texture = load_texture('graphics/spaceship2.png')
    guacamole_texture = load_texture('graphics/guacamole.png')
    cheese_texture = load_texture('graphics/cheese.png')
    sourcream_texture = load_texture('graphics/sourcream.png')
    pico_texture = load_texture('graphics/pico.png')
    taco_texture = load_texture('graphics/taco.png')
    iker_texture = load_texture('graphics/iker.jpg')
    salsa_texture = load_texture('graphics/salsa.png')

    assert iker_texture is not None
