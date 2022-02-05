import serial
import time

def link(arduino,key):
    value=b''
    print("key is: ",key) 
    print("value is ",value)
    # while (value==b''):
    value = write_read(key,arduino)
    print(value) # printing the value
        

def write_read(x,arduino):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


if __name__ == "__main__":
    import tkinter as tk

    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

    root = tk.Tk()
    root.title('TEST')
    page = tk.Frame(root) # to create a Frame
    page.pack() 

    text = tk.Label(page,text="Plz put any numbers here: ")
    text.grid(row=0,stick='W',pady=10,padx=10)

    string = tk.StringVar()
    key = tk.Entry(page, textvariable=string,show=None)
    key.grid(row=1,column=0,stick='W',pady=10,padx=10)

    b_run = tk.Button(page,text="Run",command=lambda:link(arduino,string.get()))
    b_run.grid(row=2,column=0,stick="W",pady=10,padx=10)
    root.mainloop()

