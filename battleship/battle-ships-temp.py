import blessed
import psutil
import time


if __name__ == '__main__':
    term = blessed.Terminal()
    print(term.home + term.clear)
    with term.location(y=0):
        print(f"Screen width: {term.width}")
        print(f"Screen Height: {term.height}")
        print(f"Screen Colours: {term.number_of_colours}")

while True:
    the_time = time.asctime()
    with term.location(term.width // 2 - 18, term.height // 2):
        print(term.center(f"{the_time}", width=36), end=“”)

    with term.location(y=term.height - 1):
        print(term.red + term.on_black + "Press any key to "
        "exit" + term.home,
        end = "")
        if term.inkey(1):
            print(term.clear + term.home)
            break

term.home
term.clear
term.width
term.height
term.number_of_colours