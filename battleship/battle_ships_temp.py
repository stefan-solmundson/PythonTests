# pip install blessed
# pip install colorama

import blessed
# import psutil
import time

if __name__ == '__main__':
    term = blessed.Terminal()
    print(term.home + term.clear)
    with term.location(y=0):
        print(f"Screen width: {term.width}")
        print(f"Screen Height: {term.height}")
        print(f"Screen Colors: {term.number_of_colors}")

    while True:
        the_time = time.asctime()  # string time
        print(term.center(f"{the_time}", width=36), end="---")

        print(term.red + term.on_black + "Press any key to exit " + term.home, end="")
        # with term.location():
        if term.inkey(1):  # loops every 1 second, waiting for an input
            print(term.clear + term.home)
            term.clear()
            break


# ---

# term.home
# term.clear
# term.width
# term.height
# term.number_of_colours
# term.location : does NOT work with normal print statements
# term.inkey
# term.center

