'''
https://www.askpython.com/python-modules/python-signal
https://stackabuse.com/handling-unix-signals-in-python/ 

## Stack Frame Objects
A stack frame object is an object that tracks the runtime stack of the main program
'''

import signal  
import time  
 
# Our signal handler
def signal_handler(signum, frame):  
    print()
    print("Signal Name:", signal.Signals(signum).name)
    print("  Signal Number:", signum)
    print("  Frame: ", frame)  # the frame from which the signal was received
 
def exit_handler(signum, frame):
    print()
    print("Signal Name:", signal.Signals(signum).name)
    print("  Signal Number:", signum)
    print("  Frame: ", frame)  # the frame from which the signal was received
    print("Exiting....")
    exit(0)
 
# Register a signal handler with `SIGINT`(CTRL + C)
signal.signal(signal.SIGINT, signal_handler)
 
# Register the exit handler with `SIGTSTP` (Ctrl + Z)
signal.signal(signal.SIGTSTP, exit_handler)

# While Loop
while True: 
    print("Press Ctrl + C OR Ctrl + Z") 
    time.sleep(5) 
