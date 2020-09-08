'''
Task:
1) Search "the Net" for ways to monitor temperature on Windows, Linux, Mac, Raspian,
'''

# pip3 install psutil --user
import psutil

if __name__ == '__main__':
    temperatures = psutil.sensors_temperatures()
    print(temperatures)