#!/usr/bin/env python3
try:
    import pyfirmata 
    import time
except:
    import pip
    pip.main(['install','pyfirmata'])
    import pyfirmata 
    import time

import tkinter
from tkinter import messagebox

board = pyfirmata.Arduino('COM3')
print("Communication Successfully started")

## below is the trial 1
# while True:
#     board.digital[13].write(1)
#     time.sleep(1)
#     board.digital[13].write(0)
#     time.sleep(1)

# # next trial 2
# it = pyfirmata.util.Iterator(board)       # assigns an iterator that will be used to read the status of the inputs of the circuit.
# it.start()

# board.digital[10].mode = pyfirmata.INPUT   # we need to change digital[10] as input because default: the digitals are OUTPUT

# while True:
#     sw = board.digital[10].read()
#     if sw is True:
#         board.digital[13].write(1)
#     else:
#         board.digital[13].write(0)
#     time.sleep(1)

# trail 2, another complex written way
# it = pyfirmata.util.Iterator(board)
# it.start()

# digital_input = board.get_pin('d:10:i') # 'digital: pin 10: input"
# led = board.get_pin('d:13:o')

# while True:
#     sw = digital_input.read()
#     if sw is True:
#         led.write(1)
#     else:
#         led.write(0)
#     time.sleep(0.1)

# it = pyfirmata.util.Iterator(board)
# it.start()

# trail 3

# it = pyfirmata.util.Iterator(board)     # these two lines are very important
# it.start()

# analog_input = board.get_pin('a:0:i')
# led = board.get_pin('d:13:o')

# while True:
#     analog_value = analog_input.read()
#     print(analog_value)     # range from 0 to 1 ---> more closer to 1 means voltage increases ---> resistor decreases
#     if analog_value is not None:
#         delay = analog_value + 0.01 # to make sure the delay is not 0
#         led.write(1)
#         time.sleep(delay)
#         led.write(0)
#         time.sleep(delay)
#     else:
#         time.sleep(0.1)


# trail 4 -In this section, you’ll use PWM to control the brightness of an LED, according to the value of an analog input given by a potentiometer.
# it = pyfirmata.util.Iterator(board)     # these two lines are very important
# it.start()

# analog_input = board.get_pin('a:0:i')
# led = board.get_pin('d:11:p')   # digital pin 11 as PWM ---> get the duty cycle 

# while True:
#     analog_value = analog_input.read()
#     print(analog_value)     # range from 0 to 1 ---> more closer to 1 means voltage increases ---> resistor decreases
#                             # for example, if the analog_value is 0.1 means in one cycle(10s for example), there is only 1s has the high voltage
#     if analog_value is not None:
#         led.write(analog_value)
#     else:
#         time.sleep(0.1)

# trail 5 - use GUI
# root = tkinter.Tk()
# root.withdraw()

# it = pyfirmata.util.Iterator(board)
# it.start()

# digital_input = board.get_pin('d:10:i')
# led = board.get_pin('d:13:o')

# while True:
#     sw = digital_input.read()
#     if sw is True:
#         led.write(1)
#         messagebox.showinfo("Notification", "Button was pressed")
#         root.update()
#         led.write(0)
#     time.sleep(0.1)

board.digital[13].write(1)

it = pyfirmata.util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
board.analog[0].read()

analog_0 = board.get_pin('a:0:i')
analog_0.read()

pin3 = board.get_pin('d:3:p')
pin3.write(0.6)