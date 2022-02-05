import serial
import time
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    # time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    flag= input("Enter 1 if you want to change parameter: ")
    print(flag)
    if (flag=='1'):
        value=b''
        num = input("Enter a number: ") # Taking input from user
        while (value==b''):
            value = write_read(num)
            print(value) # printing the value
    flag=0
