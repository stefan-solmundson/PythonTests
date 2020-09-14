import random

try:
    import psutil
except:
    psutil = None


def get_random_cpu_load():
    """
    This function returns a random CPU load
    which may be used to simulate a load
    when no actual CPU load can be determined

    :return: random CPU load between 0% and 100%
    """
    load = random.gauss(55, 10)
    if load < 0:
        load = 0.0
    elif load > 100:
        load = 100.0
    else:
        load = round(load, 1)
    return load


def get_maximum_cpu_load():
    if psutil is not None:
        load = max(psutil.cpu_percent(percpu=True))
    else:
        load = get_random_cpu_load()
    return load
