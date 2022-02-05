import tkinter.messagebox
from DCM.functions import *
import csv
from tkinter import *
import tkinter as pk
from DCM.serial_comm import writePara

from DCM.functions import Lower_Rate_Limit_Error, Atrial_Pulse_Width_Error, Atrial_Amplitude_Error, \
    Upper_Rate_Limit_Error, Rate_Smoothing_Error, Hysteresis_Error, ARP_Error, Atrial_Sensitivity_Error, \
    Reaction_Time_Error, Response_Factor_Error, Recovery_Time_Error, Maximum_Sensor_Rate_Error, \
    Activity_Threshold_Error,PVARP_Error


row_AAIR = []

def AAIR_window():
    root_AAIR = pk.Tk()
    root_AAIR.title('AAIR')
    root_AAIR.geometry('480x600')

    with open("user.txt", 'r') as s_file:
        content = s_file.read()
        print(content)
    s_file.close()

    with open('{}.csv'.format(content), 'r+') as user_file:
        lines1 = user_file.readlines()
        user_file.truncate()
    user_file.close()

    for line1 in lines1:
        row_AAIR.append(line1.split(','))
        while ['"\n'] in row_AAIR:
            row_AAIR.remove(['"\n'])
    for element in row_AAIR:
        if '\n' in element:
            element.pop()

    Label(root_AAIR, text='Lower Rate Limit:').grid(row=0, column=0)
    Label(root_AAIR, text='Upper Rate Limit:').grid(row=1, column=0)
    Label(root_AAIR, text='Maximum Sensor Rate:').grid(row=2, column=0)
    Label(root_AAIR, text='Atrial Amplitude:').grid(row=3, column=0)
    Label(root_AAIR, text='Atrial Pulse Width:').grid(row=4, column=0)
    Label(root_AAIR, text='Atrial Sensitivity:').grid(row=5, column=0)
    Label(root_AAIR, text='ARP:').grid(row=6, column=0)
    Label(root_AAIR, text='PVARP:').grid(row=7, column=0)
    Label(root_AAIR, text='Hysteresis(-1 as "off"):').grid(row=8, column=0)
    Label(root_AAIR, text='Rate Smoothing(-1 as "off"):').grid(row=9, column=0)
    Label(root_AAIR, text='Activity Threshold(eg:V-Low as 1):').grid(row=10, column=0)
    Label(root_AAIR, text='Reaction Time:').grid(row=11, column=0)
    Label(root_AAIR, text='Response Factor:').grid(row=12, column=0)
    Label(root_AAIR, text='Recovery Time:').grid(row=13, column=0)

    v1 = pk.StringVar()
    v1.set(row_AAIR[9][1])
    v2 = pk.StringVar()
    v2.set(row_AAIR[9][2])
    v3 = pk.StringVar()
    v3.set(row_AAIR[9][3])
    v4 = pk.StringVar()
    v4.set(row_AAIR[9][7])
    v5 = pk.StringVar()
    v5.set(row_AAIR[9][9])
    v6 = pk.StringVar()
    v6.set(row_AAIR[9][10])
    v7 = pk.StringVar()
    v7.set(row_AAIR[9][14])
    v8 = pk.StringVar()
    v8.set(row_AAIR[9][15])
    v9 = pk.StringVar()
    v9.set(row_AAIR[9][17])
    v10 = pk.StringVar()
    v10.set(row_AAIR[9][18])
    v11 = pk.StringVar()
    v11.set(row_AAIR[9][22])
    v12 = pk.StringVar()
    v12.set(row_AAIR[9][23])
    v13 = pk.StringVar()
    v13.set(row_AAIR[9][24])
    v14 = pk.StringVar()
    v14.set(row_AAIR[9][25])

    e1 = Entry(root_AAIR, textvariable=v1)
    e2 = Entry(root_AAIR, textvariable=v2)
    e3 = Entry(root_AAIR, textvariable=v3)
    e4 = Entry(root_AAIR, textvariable=v4)
    e5 = Entry(root_AAIR, textvariable=v5)
    e6 = Entry(root_AAIR, textvariable=v6)
    e7 = Entry(root_AAIR, textvariable=v7)
    e8 = Entry(root_AAIR, textvariable=v8)
    e9 = Entry(root_AAIR, textvariable=v9)
    e10 = Entry(root_AAIR, textvariable=v10)
    e11 = Entry(root_AAIR, textvariable=v11)
    e12 = Entry(root_AAIR, textvariable=v12)
    e13 = Entry(root_AAIR, textvariable=v13)
    e14 = Entry(root_AAIR, textvariable=v14)

    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)
    e3.grid(row=2, column=1, padx=10, pady=5)
    e4.grid(row=3, column=1, padx=10, pady=5)
    e5.grid(row=4, column=1, padx=10, pady=5)
    e6.grid(row=5, column=1, padx=10, pady=5)
    e7.grid(row=6, column=1, padx=10, pady=5)
    e8.grid(row=7, column=1, padx=10, pady=5)
    e9.grid(row=8, column=1, padx=10, pady=5)
    e10.grid(row=9, column=1, padx=10, pady=5)
    e11.grid(row=10, column=1, padx=10, pady=5)
    e12.grid(row=11, column=1, padx=10, pady=5)
    e13.grid(row=12, column=1, padx=10, pady=5)
    e14.grid(row=13, column=1, padx=10, pady=5)

    print(row_AAIR)

    # LRL input detecting
    def show_AAIR_LRL():
        try:

            if isinstance(int(e1.get()), int):
                if int(e1.get()) < 30:
                    Lower_Rate_Limit_Error()
                if 30 <= int(e1.get()) < 50:
                    if int(e1.get()) % 5 != 0:
                        Lower_Rate_Limit_Error()

                    else:
                        row_AAIR[9][1] = str(e1.get())
                        success()

                if 50 <= int(e1.get()) < 90:
                    if int(e1.get()) % 1 != 0:
                        Lower_Rate_Limit_Error()

                    else:
                        row_AAIR[9][1] = str(e1.get())
                        success()

                if 90 <= int(e1.get()) <= 175:
                    if int(e1.get()) % 5 != 0:
                        Lower_Rate_Limit_Error()

                    else:
                        row_AAIR[9][1] = str(e1.get())
                        success()

                if int(e1.get()) > 175:
                    Lower_Rate_Limit_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAIR)
        csv_file.close()

    # URL input detecting
    def show_AAIR_URL():

        try:
            if isinstance(int(e2.get()), int):
                if int(e2.get()) < 50:
                    Upper_Rate_Limit_Error()

                if int(e2.get()) > 175:
                    Upper_Rate_Limit_Error()

                if 50 <= int(e2.get()) <= 175:
                    if int(e2.get()) % 5 != 0:
                        Upper_Rate_Limit_Error()

                    else:
                        row_AAIR[9][2] = str(e2.get())
                        success()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAIR)
        csv_file.close()

    # Maximum Sensor Rate detecting
    def show_AAIR_MSR():
        try:
            if isinstance(int(e3.get()), int):
                if 50 <= int(e3.get()) <= 175:
                    if int(e3.get()) % 5 == 0:
                        row_AAIR[9][3] = str(e3.get())
                        success()
                    else:
                        Maximum_Sensor_Rate_Error()
                else:
                    Maximum_Sensor_Rate_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAIR)
        csv_file.close()

    # VA input detecting

    def show_AAIR_AA():
        try:
            if isinstance(int(e4.get()), int):
                if 0 <= int(e4.get()) <= 100:
                    row_AAIR[9][7] = str(e4.get())
                    success()
                else:
                    Atrial_Amplitude_Error()

        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAIR)
        csv_file.close()

    # VPW input detecting
    def show_AAIR_APW():
        try:
            if isinstance(int(e5.get()), int):
                if 0 <= int(e5.get()) <= 20:
                    row_AAIR[9][9] = str(e5.get())
                    success()
                else:
                    Atrial_Pulse_Width_Error()

        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAIR)
        csv_file.close()

    # VS input detecting
    def show_AAIR_AS():
        try:
            if isinstance(int(e6.get()), int):
                if int(e6.get()) * 100 == 25 or int(e6.get()) * 100 == 50 or int(e6.get()) * 100 == 75:
                    row_AAIR[9][11] = str(e6.get())
                    success()
                elif int(e6.get()) >= 10 and int(e6.get()) <= 100:
                    if int(e6.get()) % 5 == 0:
                        row_AAIR[9][11] = str(e6.get())
                        success()

                else:
                    Ventricular_Sensitivity_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers only!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAIR)
        csv_file.close()

    # VRP input detecting
    def show_AAIR_ARP():
        try:
            if isinstance(int(e7.get()), int):
                if int(e7.get()) < 150 or int(e7.get()) > 500:
                    ARP_Error()
                else:
                    if int(e7.get()) % 10 != 0:
                        ARP_Error()
            else:
                row_AAIR[9][14] = str(e7.get())
                success()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAIR)
        csv_file.close()

    # PVARP
    def show_AAIR_PVARP():
        try:
            if isinstance(int(e8.get(), int)):
                if 50 <= int(e8.get()) <= 500:
                    if int(e8.get()) % 10 == 0:
                        row_AAIR[9][15] = str(e8.get())
                        success()
                    else:
                        PVARP_Error()
                else:
                    PVARP_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAIR)
        csv_file.close()

        # Hysteresis input detecting

    def show_AAIR_Hysteresis():
        try:
            if isinstance(int(e9.get()), int):
                if 0 < int(e9.get()) < 30:
                    print('yes')
                    Hysteresis_Error()
                elif 30 <= int(e9.get()) < 50:
                    if int(e9.get()) % 5 != 0:
                        Hysteresis_Error()
                    else:
                        row_AAIR[9][17] = str(e9.get())
                        success()
                elif 50 <= int(e9.get()) < 90:
                    if int(e9.get()) % 1 != 0:
                        Hysteresis_Error()

                    else:
                        row_AAIR[9][17] = str(e9.get())
                        success()
                elif 90 <= int(e9.get()) <= 175:
                    if int(e9.get()) % 5 != 0:
                        Hysteresis_Error()

                    else:
                        row_AAIR[9][17] = str(e9.get())
                        success()
                elif int(e9.get()) > 175:
                    Hysteresis_Error()

                elif int(e9.get()) == -1:
                    row_AAIR[9][17] = str(e9.get())
                    success()

                else:
                    Hysteresis_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers or only use -1 as 'off'!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAIR)
        csv_file.close()

    # Rate Smoothing input detecting
    def show_AAIR_RS():
        try:
            if isinstance(int(e10.get()), int):
                if int(e10.get()) == 3 or int(e10.get()) == 6 or int(e10.get()) == 9 or int(e10.get()) == 12:
                    row_AAIR[9][18] = str(e10.get())
                    success()
                elif int(e10.get()) == 15 or int(e10.get()) == 18 or int(e10.get()) == 21 or int(e10.get()) == 25:
                    row_AAIR[9][18] = str(e10.get())
                    success()
                elif int(e10.get()) == -1:
                    row_AAIR[9][18] = str(e10.get())
                    success()
                else:
                    Rate_Smoothing_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers or only use -1 as 'off'!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAIR)
        csv_file.close()

    # Activity Threshold
    def show_AAIR_AT():
        try:
            if isinstance(int(e11.get()), int):
                if 1 <= int(e11.get()) <= 7:
                    row_AAIR[9][22] = str(e11.get())
                    success()
                else:
                    Activity_Threshold_Error()

        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAIR)
        csv_file.close()

    # Reaction Time
    def show_AAIR_ReactionT():
        try:
            if isinstance(int(e12.get()), int):
                if 10 <= int(e12.get()) <= 50:
                    if int(e12.get()) % 10 == 0:
                        row_AAIR[9][23] = str(e12.get())
                        success()
                    else:
                        Reaction_Time_Error()
                else:
                    Reaction_Time_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAIR)
        csv_file.close()

    # Response Factor
    def show_AAIR_RF():
        try:
            if isinstance(int(e13.get()), int):
                if 1 <= int(e13.get()) <= 16:
                    row_AAIR[9][24] = str(e13.get())
                    success()
                else:
                    Response_Factor_Error()

        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAIR)
        csv_file.close()

    # Recovery Time
    def show_AAIR_RecoveryT():
        try:
            if isinstance(int(e14.get()), int):
                if 2 <= int(e14.get()) <= 16:
                    row_AAIR[9][25] = str(e14.get())
                    success()
                else:
                    Recovery_Time_Error()

        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_AAIR)
        csv_file.close()

    Button(root_AAIR, text='Save', width=5, command=show_AAIR_LRL).grid(row=0, column=2, padx=10, pady=5)
    Button(root_AAIR, text='Save', width=5, command=show_AAIR_URL).grid(row=1, column=2, padx=10, pady=5)
    Button(root_AAIR, text='Save', width=5, command=show_AAIR_MSR).grid(row=2, column=2, padx=10, pady=5)
    Button(root_AAIR, text='Save', width=5, command=show_AAIR_AA).grid(row=3, column=2, padx=10, pady=5)
    Button(root_AAIR, text='Save', width=5, command=show_AAIR_APW).grid(row=4, column=2, padx=10, pady=5)
    Button(root_AAIR, text='Save', width=5, command=show_AAIR_AS).grid(row=5, column=2, padx=10, pady=5)
    Button(root_AAIR, text='Save', width=5, command=show_AAIR_ARP).grid(row=6, column=2, padx=10, pady=5)
    Button(root_AAIR, text='Save', width=5, command=show_AAIR_PVARP).grid(row=7, column=2, padx=10, pady=5)
    Button(root_AAIR, text='Save', width=5, command=show_AAIR_Hysteresis).grid(row=8, column=2, padx=10, pady=5)
    Button(root_AAIR, text='Save', width=5, command=show_AAIR_RS).grid(row=9, column=2, padx=10, pady=5)
    Button(root_AAIR, text='Save', width=5, command=show_AAIR_AT).grid(row=10, column=2, padx=10, pady=5)
    Button(root_AAIR, text='Save', width=5, command=show_AAIR_ReactionT).grid(row=11, column=2, padx=10, pady=5)
    Button(root_AAIR, text='Save', width=5, command=show_AAIR_RF).grid(row=12, column=2, padx=10, pady=5)
    Button(root_AAIR, text='Save', width=5, command=show_AAIR_RecoveryT).grid(row=13, column=2, padx=10, pady=5)

    Button(root_AAIR, text='Fire', width=5, command=root_AAIR.destroy).place(x=130, y=560)
    Button(root_AAIR, text='Cancel', width=5, command=root_AAIR.destroy).place(x=290, y=560)
    mainloop()
