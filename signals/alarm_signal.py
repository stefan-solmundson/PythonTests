'''
https://www.askpython.com/python-modules/python-signal
https://stackabuse.com/handling-unix-signals-in-python/ 

## Stack Frame Objects
A stack frame object is an object that tracks the runtime stack of the main program
'''

import signal
import time
 
def alarm_handler(signum, frame):
    print('Alarm at:    ', time.ctime())
 
# Register the alarm signal with a handler
signal.signal(signal.SIGALRM, alarm_handler)

print('Current time:', time.ctime())
print("    An alarm signal has been set to trigger in 3 seconds.")

# Create a an alarm signal that will trigger after 3 seconds 
signal.alarm(3)

# Wait 6 seconds, so that the program doesn't close before the alarm is signal occurs
time.sleep(6)