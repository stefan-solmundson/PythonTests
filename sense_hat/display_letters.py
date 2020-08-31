# https://trinket.io/sense-hat

from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True
s.set_rotation(270)

letters = ['S', 't', 'e', 'f']
count = 0

while True:
    # s.show_letter('A')
    # s.show_letter('B')
    s.set_pixels(letters[count % len(letters)]())
    time.sleep(1.50)
    count += 1
