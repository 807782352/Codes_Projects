import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600,timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    # time.sleep(0.05)
    data = arduino.readline()
    return data
    
while True:
    # mode = input("Enter a number: ") # Taking input from user
    mode = "A"
    value = write_read(mode)
    print(value) # printing the value