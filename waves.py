from entity import *

width = get_monitor_width(get_current_monitor())
height = get_monitor_height(get_current_monitor())

entity_width = get_monitor_width(get_current_monitor()) * 0.12
entity_height = get_monitor_height(get_current_monitor()) * 0.0924

spacing_width = entity_width + get_monitor_width(get_current_monitor()) * 0.05
spacing_height = entity_height + get_monitor_width(get_current_monitor()) * 0.05


wave_one = []

for i in range(0, 2):
    wave_one.append(entity(Vector2(width * 0.40 + spacing_width * i, height * 0.105)))

wave_two = []

for i in range(0, 8):
    wave_two.append(entity(Vector2(width * 0.30 + spacing_width * i)))

wave_three = []

