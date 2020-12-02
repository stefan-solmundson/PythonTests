'''
Each OS has different available signals
  // Linux has many, windows has few
'''

import signal

valid_signals = signal.valid_signals()
print(valid_signals)
