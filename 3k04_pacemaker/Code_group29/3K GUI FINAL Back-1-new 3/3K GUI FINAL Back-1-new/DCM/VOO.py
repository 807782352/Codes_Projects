import tkinter.messagebox
from DCM.functions import *
import csv
from tkinter import *
import tkinter as pk
from DCM.serial_comm import writePara

from DCM.functions import Lower_Rate_Limit_Error, Ventricular_Amplitude_Error, Ventricular_Pulse_Width_Error,\
    Upper_Rate_Limit_Error

row_VOO = []


def VOO_window():
    global e1
    global e3
    global e4

    root_VOO = Tk()
    root_VOO.title('VOO')
    root_VOO.geometry('420x200')

    with open("user.txt", 'r') as s_file:
        content = s_file.read()
        print(content)
    s_file.close()

    with open('{}.csv'.format(content), 'r+') as user_file:
        lines1 = user_file.readlines()
        user_file.truncate()
    user_file.close()

    for line1 in lines1:
        row_VOO.append(line1.split(','))
        while ['"\n'] in row_VOO:
            row_VOO.remove(['"\n'])
    for element in row_VOO:
        if '\n' in element:
            element.pop()

    print(row_VOO)

    Label(root_VOO, text=' Lower Rate Limit:').grid(row=0, column=0)
    Label(root_VOO, text=' Upper Rate Limit:').grid(row=1, column=0)
    Label(root_VOO, text=' Atrial Amplitude:').grid(row=2, column=0)
    Label(root_VOO, text=' Atrial Pulse Width:').grid(row=3, column=0)

    v1 = pk.StringVar()
    v1.set(row_VOO[2][1])
    v2 = pk.StringVar()
    v2.set(row_VOO[2][2])
    v3 = pk.StringVar()
    v3.set(row_VOO[2][8])
    v4 = pk.StringVar()
    v4.set(row_VOO[2][10])

    e1 = Entry(root_VOO, textvariable=v1)
    e2 = Entry(root_VOO, textvariable=v2)
    e3 = Entry(root_VOO, textvariable=v3)
    e4 = Entry(root_VOO, textvariable=v4)

    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)
    e3.grid(row=2, column=1, padx=10, pady=5)
    e4.grid(row=3, column=1, padx=10, pady=5)


    print("Lower Rate Limit:%s" % e1.get())
    print("Upper Rate Limit:%s" % e2.get())
    print("Atrial Amplitude:%s" % e3.get())
    print("Atrial Pulse Width:%s" % e4.get())

        # LRL input detecting
    def show_VOO_LRL():
        try:
            if isinstance(int(e1.get()), int):
                if int(int(row_VOO[2][2]) == 0):
                    if int(e1.get()) < 30:
                        Lower_Rate_Limit_Error()
                    if 30 <= int(e1.get()) < 50:
                        if int(e1.get()) % 5 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_VOO[2][1] = str(e1.get())
                            success()

                    if 50 <= int(e1.get()) < 90:
                        if int(e1.get()) % 1 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_VOO[2][1] = str(e1.get())
                            success()

                    if 90 <= int(e1.get()) <= 175:
                        if int(e1.get()) % 5 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_VOO[2][1] = str(e1.get())
                            success()

                    if int(e1.get()) > 175:
                        Lower_Rate_Limit_Error()
                else:
                    if int(e1.get()) >= int(row_VOO[2][2]):
                        tkinter.messagebox.showerror('Error', "LRL can not be greater than URL!")
                    else:
                        if int(e1.get()) < 30:
                            Lower_Rate_Limit_Error()
                        if 30 <= int(e1.get()) < 50:
                            if int(e1.get()) % 5 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_VOO[2][1] = str(e1.get())
                                success()

                        if 50 <= int(e1.get()) < 90:
                            if int(e1.get()) % 1 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_VOO[2][1] = str(e1.get())
                                success()

                        if 90 <= int(e1.get()) <= 175:
                            if int(e1.get()) % 5 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_VOO[2][1] = str(e1.get())
                                success()

                        if int(e1.get()) > 175:
                            Lower_Rate_Limit_Error()


        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VOO)
        csv_file.close()



        # URL input detecting
    def show_VOO_URL():

        try:
            if isinstance(int(e2.get()), int):
                if int(int(row_VOO[2][1]) == 0):
                    if int(e2.get()) < 50:
                        Upper_Rate_Limit_Error()


                    if int(e2.get()) > 175:
                        Upper_Rate_Limit_Error()


                    if 50 <= int(e2.get()) <= 175:
                        if int(e2.get()) % 5 != 0:
                            Upper_Rate_Limit_Error()

                        else:
                            row_VOO[2][2] = str(e2.get())
                            success()
                else:
                    if int(e2.get()) <= int(row_VOO[2][1]):
                        tkinter.messagebox.showerror('Error', "LRL can not be greater than URL!")
                    else:
                        if int(e2.get()) < 50:
                            Upper_Rate_Limit_Error()

                        if int(e2.get()) > 175:
                            Upper_Rate_Limit_Error()

                        if 50 <= int(e2.get()) <= 175:
                            if int(e2.get()) % 5 != 0:
                                Upper_Rate_Limit_Error()

                            else:
                                row_VOO[2][2] = str(e2.get())
                                success()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VOO)
        csv_file.close()


        # VA input detecting
        # AA input detecting

    def show_VOO_VA():
        try:
            if isinstance(int(e3.get()), int):
                if 0 <= int(e3.get()) <= 100:
                    row_VOO[2][8] = str(e3.get())
                    success()
                else:
                    Ventricular_Amplitude_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VOO)
        csv_file.close()

    def show_VOO_VPW():
        try:
            if isinstance(int(e4.get()), int):
                if 0 <= int(e4.get()) <= 20:
                    row_VOO[2][10] = str(e4.get())
                    success()
                else:
                    Ventricular_Pulse_Width_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VOO)
        csv_file.close()


    Button(root_VOO, text='Cancel', width=5, command=root_VOO.destroy).place(x=205, y=165)
    Button(root_VOO, text='Fire', width=5, command=trans).place(x=143, y=165)

    Button(root_VOO, text='Save', width=5, command=show_VOO_LRL).grid(row=0, column=2, padx=10, pady=5)
    Button(root_VOO, text='Save', width=5, command=show_VOO_URL).grid(row=1, column=2, padx=10, pady=5)
    Button(root_VOO, text='Save', width=5, command=show_VOO_VA).grid(row=2, column=2, padx=10, pady=5)
    Button(root_VOO, text='Save', width=5, command=show_VOO_VPW).grid(row=3, column=2, padx=10, pady=5)


    mainloop()

def trans():
    writePara(mode=2, Lower_Rate=int(e1.get()), VENT_Amplitude=int(e3.get()), VENT_Width=int(e4.get())),
    successFire()
