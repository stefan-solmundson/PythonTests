# https://trinket.io/sense-hat

from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True
s.set_rotation(270)

message = "Hello World"
scroll_speed = 0.4
text_color = [0, 0, 0]
back_color = [255, 255, 0]

s.show_message(
    "Hello World",
    scroll_speed=scroll_speed,
    text_colour=text_colour,
    back_colour=back_colour
)