import tkinter.messagebox
from DCM.functions import *
import csv
from tkinter import *
import tkinter as pk
from DCM.serial_comm import writePara

from DCM.functions import Lower_Rate_Limit_Error, Atrial_Pulse_Width_Error, Atrial_Amplitude_Error, \
    Upper_Rate_Limit_Error, Rate_Smoothing_Error, Hysteresis_Error, ARP_Error, Atrial_Sensitivity_Error, PVARP_Error

row_AAI = []


def AAI_window():
    global e1
    global e3
    global e4
    global e5

    root_AAI = pk.Tk()
    root_AAI.title('AAI')
    root_AAI.geometry('480x400')

    with open("user.txt", 'r') as s_file:
        content = s_file.read()
        print(content)
    s_file.close()

    with open('{}.csv'.format(content), 'r+') as user_file:
        lines1 = user_file.readlines()
        user_file.truncate()
    user_file.close()

    for line1 in lines1:
        row_AAI.append(line1.split(','))
        while ['"\n'] in row_AAI:
            row_AAI.remove(['"\n'])
    for element in row_AAI:
        if '\n' in element:
            element.pop()

    print(row_AAI)

    Label(root_AAI, text='Lower Rate Limit:').grid(row=0, column=0)
    Label(root_AAI, text='Upper Rate Limit:').grid(row=1, column=0)
    Label(root_AAI, text='Atrial Amplitude:').grid(row=2, column=0)
    Label(root_AAI, text='Atrial Pulse Width:').grid(row=3, column=0)
    Label(root_AAI, text='ARP:').grid(row=4, column=0)
    Label(root_AAI, text='Atrial Sensitivity:').grid(row=5, column=0)
    Label(root_AAI, text='PVARP:').grid(row=6, column=0)
    Label(root_AAI, text="Hysteresis(-1 as 'off'):").grid(row=7, column=0)
    Label(root_AAI, text="Rate Smoothing:(-1 as 'off')").grid(row=8, column=0)

    v1 = pk.StringVar()
    v1.set(row_AAI[3][1])
    v2 = pk.StringVar()
    v2.set(row_AAI[3][2])
    v3 = pk.StringVar()
    v3.set(row_AAI[3][7])
    v4 = pk.StringVar()
    v4.set(row_AAI[3][9])
    v5 = pk.StringVar()
    v5.set(row_AAI[3][14])
    v6 = pk.StringVar()
    v6.set(row_AAI[3][11])
    v7 = pk.StringVar()
    v7.set(row_AAI[3][15])
    v8 = pk.StringVar()
    v8.set(row_AAI[3][17])
    v9 = pk.StringVar()
    v9.set(row_AAI[3][18])

    e1 = Entry(root_AAI, textvariable=v1)
    e2 = Entry(root_AAI, textvariable=v2)
    e3 = Entry(root_AAI, textvariable=v3)
    e4 = Entry(root_AAI, textvariable=v4)
    e5 = Entry(root_AAI, textvariable=v5)
    e6 = Entry(root_AAI, textvariable=v6)
    e7 = Entry(root_AAI, textvariable=v7)
    e8 = Entry(root_AAI, textvariable=v8)
    e9 = Entry(root_AAI, textvariable=v9)

    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)
    e3.grid(row=2, column=1, padx=10, pady=5)
    e4.grid(row=3, column=1, padx=10, pady=5)
    e5.grid(row=4, column=1, padx=10, pady=5)
    e6.grid(row=5, column=1, padx=10, pady=5)
    e7.grid(row=6, column=1, padx=10, pady=5)
    e8.grid(row=7, column=1, padx=10, pady=5)
    e9.grid(row=8, column=1, padx=10, pady=5)

    print("Lower Rate Limit:%s" % e1.get())
    print("Upper Rate Limit:%s" % e2.get())
    print("Atrial Amplitude:%s" % e3.get())
    print("Atrial Pulse Width:%s" % e4.get())
    print("ARP:%s" % e5.get())
    print("Atrial Sensitivity:%s" % e6.get())
    print("PVARP:%s" % e7.get())
    print("Hysteresis(-1 as 'off':%s)" % e8.get())
    print("Rate Smoothing(-1 as 'off':%s)" % e9.get())

    # LRL input detecting
    def show_AAI_LRL():

        try:
            if isinstance(int(e1.get()), int):

                if int(int(row_AAI[3][2]) == 0):
                    if int(e1.get()) < 30:
                        Lower_Rate_Limit_Error()
                    if 30 <= int(e1.get()) < 50:
                        if int(e1.get()) % 5 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_AAI[3][1] = str(e1.get())
                            success()

                    if 50 <= int(e1.get()) < 90:
                        if int(e1.get()) % 1 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_AAI[3][1] = str(e1.get())
                            success()

                    if 90 <= int(e1.get()) <= 175:
                        if int(e1.get()) % 5 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_AAI[3][1] = str(e1.get())
                            success()

                    if int(e1.get()) > 175:
                        Lower_Rate_Limit_Error()

                else:
                    if int(e1.get()) >= int(row_AAI[3][2]):
                        tkinter.messagebox.showerror('Error', "LRL can not be greater than URL!")

                    else:
                        if int(e1.get()) < 30:
                            Lower_Rate_Limit_Error()
                        if 30 <= int(e1.get()) < 50:
                            if int(e1.get()) % 5 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_AAI[3][1] = str(e1.get())
                                success()

                        if 50 <= int(e1.get()) < 90:
                            if int(e1.get()) % 1 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_AAI[3][1] = str(e1.get())
                                success()

                        if 90 <= int(e1.get()) <= 175:
                            if int(e1.get()) % 5 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_AAI[3][1] = str(e1.get())
                                success()

                        if int(e1.get()) > 175:
                            Lower_Rate_Limit_Error()




        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAI)
        csv_file.close()

    # URL input detecting
    def show_AAI_URL():
        try:
            if isinstance(int(e2.get()), int):
                if int(int(row_AAI[3][1]) == 0):
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
                            row_AAI[3][2] = str(e2.get())
                            success()
                else:
                    if int(e2.get()) <= int(row_AAI[3][1]):
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
                                row_AAI[3][2] = str(e2.get())
                                success()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAI)
        csv_file.close()

    # AA input detecting
    def show_AAI_AA():
        try:
            if isinstance(int(e3.get()), int):
                if 0 <= int(e3.get()) <= 100:
                    row_AAI[3][7] = str(e3.get())
                    success()
                else:
                    Atrial_Amplitude_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAI)
        csv_file.close()

    # APW input detecting
    def show_AAI_APW():
        try:
            if isinstance(int(e4.get()), int):
                if 0 <= int(e4.get()) <= 20:
                    row_AAI[3][9] = str(e4.get())
                    success()
                else:
                    Atrial_Pulse_Width_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAI)
        csv_file.close()

    # ARP input detecting
    def show_AAI_ARP():
        try:
            if isinstance(int(e5.get()), int):
                if int(e5.get()) < 150 or int(e5.get()) > 500:
                    ARP_Error()
                else:
                    if int(e5.get()) % 10 != 0:
                        ARP_Error()
                    else:
                        row_AAI[3][14] = int(e5.get())
                        success()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAI)
        csv_file.close()

    # AS input detecting
    def show_AAI_AS():
        try:
            if isinstance(float(e1.get()), float):
                if int(float(e6.get()) * 100 )== 25 or int(float(e6.get()) * 100) == (50) or int(float(e6.get()) * 100) == (75):
                    row_AAI[3][11] = str(e6.get())
                    success()
                elif float(e6.get())  >= float(10) and float(e6.get()) <= float(100):
                    if int(float(e6.get())*100) % 5 == 0:
                        row_AAI[3][11] = str(e6.get())
                        success()
                else:
                    Atrial_Sensitivity_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use floats!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAI)
        csv_file.close()

    # PVARP input detecting
    def show_AAI_PVARP():
        try:
            if isinstance(int(e1.get()), int):
                if int(e7.get()) >= 150 and int(e7.get()) <= 500:
                    if int(e7.get()) % 10 == 0:
                        row_AAI[3][15] = str(e7.get())
                        success()
                else:
                    PVARP_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAI)
        csv_file.close()

    # Hysteresis input detecting
    def show_AAI_Hysteresis():
        try:
            if isinstance(int(e8.get()), int):
                if 0 < int(e8.get()) < 30:
                    Hysteresis_Error()
                elif 30 <= int(e8.get()) < 50:
                    if int(e8.get()) % 5 != 0:
                        Hysteresis_Error()
                    else:
                        row_AAI[3][17] = str(e8.get())
                        success()
                elif 50 <= int(e8.get()) < 90:
                    if int(e8.get()) % 1 != 0:
                        Hysteresis_Error()

                    else:
                        row_AAI[3][17] = str(e8.get())
                        success()
                elif 90 <= int(e8.get()) <= 175:
                    if int(e8.get()) % 5 != 0:
                        Hysteresis_Error()

                    else:
                        row_AAI[3][17] = str(e8.get())
                        success()
                elif int(e8.get()) > 175:
                    Hysteresis_Error()

                elif int(e8.get()) == -1:
                    row_AAI[3][17] = str(e8.get())
                    success()
                else:
                    Hysteresis_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers or only use -1 as 'off'!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAI)
        csv_file.close()

    # Rate Smoothing input detecting
    def show_AAI_RS():
        try:
            if isinstance(int(e9.get()), int):
                if int(e9.get()) == 3 or int(e9.get()) == 6 or int(e9.get()) == 9 or int(e9.get()) == 12:
                    row_AAI[3][18] = str(e9.get())
                    success()
                elif int(e9.get()) == 15 or int(e9.get()) == 18 or int(e9.get()) == 21 or int(e9.get()) == 25:
                    row_AAI[3][18] = str(e9.get())
                    success()
                elif int(e9.get()) == -1:
                    row_AAI[3][18] = str(e9.get())
                    success()
                else:
                    Rate_Smoothing_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers or only use -1 as 'off'!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAI)
        csv_file.close()

    Button(root_AAI, text='Save', width=5, command=show_AAI_LRL).grid(row=0, column=2, padx=10, pady=5)
    Button(root_AAI, text='Save', width=5, command=show_AAI_URL).grid(row=1, column=2, padx=10, pady=5)
    Button(root_AAI, text='Save', width=5, command=show_AAI_AA).grid(row=2, column=2, padx=10, pady=5)
    Button(root_AAI, text='Save', width=5, command=show_AAI_APW).grid(row=3, column=2, padx=10, pady=5)
    Button(root_AAI, text='Save', width=5, command=show_AAI_ARP).grid(row=4, column=2, padx=10, pady=5)
    Button(root_AAI, text='Save', width=5, command=show_AAI_AS).grid(row=5, column=2, padx=10, pady=5)
    Button(root_AAI, text='Save', width=5, command=show_AAI_PVARP).grid(row=6, column=2, padx=10, pady=5)
    Button(root_AAI, text='Save', width=5, command=show_AAI_Hysteresis).grid(row=7, column=2, padx=10, pady=5)
    Button(root_AAI, text='Save', width=5, command=show_AAI_RS).grid(row=8, column=2, padx=10, pady=5)

    # Button(root_AAI, text='Save', width=5, command=show_AAI).place(x=50, y=290)
    Button(root_AAI, text='Fire', width=5, command=trans).place(x=160, y=360)
    Button(root_AAI, text='Cancel', width=5, command=root_AAI.destroy).place(x=280, y=360)

    mainloop()


def trans():
    # writePara(mode=3, Lower_Rate=int(e1.get()), ATR_Amplitude=int(e3.get()), ATR_Width=int(e4.get()),
    #           ATR_Refractory=int(e5.get())),
    successFire()