from datetime import datetime
from time import sleep
from cpu_load import get_maximum_cpu_load
from db import Database


def main(delay):
    db = Database('cpu_loads.db')
    db.create()
    while True:
        load = get_maximum_cpu_load()
        db.store(load)
        print(f"{datetime.now()} CPU Load: {load}")
        sleep(delay)


if __name__ == '__main__':
    delay = 5.0  # delay in seconds
    main(delay)  # runs the main method
