from pyray import *

class Textures:
    def load(self):
        self.player_texture = load_texture('graphics/spaceship2.png')
        self.guacamole_texture = load_texture('graphics/guacamole.png')
        self.cheese_texture = load_texture('graphics/cheese.png')
        self.sourcream_texture = load_texture('graphics/sourcream.png')
        self.pico_texture = load_texture('graphics/pico.png')
        self.taco_texture = load_texture('graphics/taco.png')
        self.iker_texture = load_texture('graphics/iker.jpg')
        self.salsa_texture = load_texture('graphics/salsa.png')

    def unload(self):
        unload_texture(self.player_texture)
        unload_texture(self.guacamole_texture)
        unload_texture(self.cheese_texture)
        unload_texture(self.sourcream_texture)
        unload_texture(self.pico_texture)
        unload_texture(self.taco_texture)
        unload_texture(self.iker_texture)
        unload_texture(self.salsa_texture)

