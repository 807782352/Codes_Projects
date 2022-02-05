import tkinter.messagebox
from DCM.functions import *
import csv
from tkinter import *
import tkinter as pk
from DCM.serial_comm import writePara

from DCM.functions import Lower_Rate_Limit_Error, Atrial_Pulse_Width_Error, Atrial_Amplitude_Error, \
    Upper_Rate_Limit_Error

row_AOO = []


def AOO_window():
    global e1
    global e3
    global e4

    root_AOO = Tk()
    root_AOO.title('AOO')
    root_AOO.geometry('420x200')

    with open("user.txt", 'r') as s_file:
        content = s_file.read()
        print(content)
    s_file.close()

    with open('{}.csv'.format(content), 'r+') as user_file:
        lines1 = user_file.readlines()
        user_file.truncate()
    user_file.close()

    for line1 in lines1:
        row_AOO.append(line1.split(','))
        while ['"\n'] in row_AOO:
            row_AOO.remove(['"\n'])
    for element in row_AOO:
        if '\n' in element:
            element.pop()

    print(row_AOO)

    Label(root_AOO, text=' Lower Rate Limit:').grid(row=0, column=0)
    Label(root_AOO, text=' Upper Rate Limit:').grid(row=1, column=0)
    Label(root_AOO, text=' Atrial Amplitude:').grid(row=2, column=0)
    Label(root_AOO, text=' Atrial Pulse Width:').grid(row=3, column=0)

    v1 = pk.StringVar()
    v1.set(row_AOO[1][1])
    v2 = pk.StringVar()
    v2.set(row_AOO[1][2])
    v3 = pk.StringVar()
    v3.set(row_AOO[1][7])
    v4 = pk.StringVar()
    v4.set(row_AOO[1][9])

    e1 = Entry(root_AOO, textvariable=v1)
    e2 = Entry(root_AOO, textvariable=v2)
    e3 = Entry(root_AOO, textvariable=v3)
    e4 = Entry(root_AOO, textvariable=v4)

    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)
    e3.grid(row=2, column=1, padx=10, pady=5)
    e4.grid(row=3, column=1, padx=10, pady=5)

    print("Lower Rate Limit:%s" % e1.get())
    print("Upper Rate Limit:%s" % e2.get())
    print("Atrial Amplitude:%s" % e3.get())
    print("Atrial Pulse Width:%s" % e4.get())

    # LRL input detecting
    def show_AOO_LRL():
        try:
            if isinstance(int(e1.get()), int):

                if int(int(row_AOO[1][2]) == 0):
                    if int(e1.get()) < 30:
                        Lower_Rate_Limit_Error()
                    if 30 <= int(e1.get()) < 50:
                        if int(e1.get()) % 5 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_AOO[1][1] = str(e1.get())
                            success()

                    if 50 <= int(e1.get()) < 90:
                        if int(e1.get()) % 1 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_AOO[1][1] = str(e1.get())
                            success()

                    if 90 <= int(e1.get()) <= 175:
                        if int(e1.get()) % 5 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_AOO[1][1] = str(e1.get())
                            success()

                    if int(e1.get()) > 175:
                        Lower_Rate_Limit_Error()

                else:
                    if int(e1.get()) >= int(row_AOO[1][2]):
                        tkinter.messagebox.showerror('Error', "LRL can not be greater than URL!")

                    else:
                        if int(e1.get()) < 30:
                            Lower_Rate_Limit_Error()
                        if 30 <= int(e1.get()) < 50:
                            if int(e1.get()) % 5 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_AOO[1][1] = str(e1.get())
                                success()

                        if 50 <= int(e1.get()) < 90:
                            if int(e1.get()) % 1 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_AOO[1][1] = str(e1.get())
                                success()

                        if 90 <= int(e1.get()) <= 175:
                            if int(e1.get()) % 5 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_AOO[1][1] = str(e1.get())
                                success()

                        if int(e1.get()) > 175:
                            Lower_Rate_Limit_Error()




        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AOO)
        csv_file.close()

        # URL input detecting

    def show_AOO_URL():

        try:
            if isinstance(int(e2.get()), int):
                if int(int(row_AOO[1][1]) == 0):
                    # if int(e2.get()) <= int(row_AOO[1][1]):
                    #     tkinter.messagebox.showerror('Error', "LRL can not be greater than URL!")
                    # else:
                    if int(e2.get()) < 50:
                        Upper_Rate_Limit_Error()

                    if int(e2.get()) > 175:
                        Upper_Rate_Limit_Error()

                    if 50 <= int(e2.get()) <= 175:
                        if int(e2.get()) % 5 != 0:
                            Upper_Rate_Limit_Error()

                        else:
                            row_AOO[1][2] = str(e2.get())
                            success()
                else:
                    if int(e2.get()) <= int(row_AOO[1][1]):
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
                                row_AOO[1][2] = str(e2.get())
                                success()



        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AOO)
        csv_file.close()

    # AA input detecting
    def show_AOO_AA():
        try:
            if isinstance(int(e3.get()), int):
                if 0 <= int(e3.get()) <= 100:
                    row_AOO[1][7] = str(e3.get())
                    success()
                else:
                    Atrial_Amplitude_Error()

                with open('{}.csv'.format(content), 'w', newline='') as csv_file:
                    cw = csv.writer(csv_file)
                    cw.writerows(row_AOO)
                csv_file.close()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

    def show_AOO_APW():
        try:
            if isinstance(int(e4.get()), int):
                if 0 <= int(e4.get()) <= 20:
                    row_AOO[1][9] = str(e4.get())
                    success()
                else:
                    Atrial_Pulse_Width_Error()

                with open('{}.csv'.format(content), 'w', newline='') as csv_file:
                    cw = csv.writer(csv_file)
                    cw.writerows(row_AOO)
                csv_file.close()

        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

    Button(root_AOO, text='Fire', width=5, command=trans).place(x=143, y=165)
    Button(root_AOO, text='Cancel', width=5, command=root_AOO.destroy).place(x=205, y=165)

    Button(root_AOO, text='Save', width=5, command=show_AOO_LRL).grid(row=0, column=2, padx=10, pady=5)
    Button(root_AOO, text='Save', width=5, command=show_AOO_URL).grid(row=1, column=2, padx=10, pady=5)
    Button(root_AOO, text='Save', width=5, command=show_AOO_AA).grid(row=2, column=2, padx=10, pady=5)
    Button(root_AOO, text='Save', width=5, command=show_AOO_APW).grid(row=3, column=2, padx=10, pady=5)

    mainloop()


def trans():
    writePara(mode=1, Lower_Rate=int(e1.get()), ATR_Amplitude=int(e3.get()), ATR_Width=int(e4.get())),
    successFire()