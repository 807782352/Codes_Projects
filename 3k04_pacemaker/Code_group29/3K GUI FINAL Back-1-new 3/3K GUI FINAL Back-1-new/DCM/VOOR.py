import tkinter.messagebox
from DCM.functions import *
import csv
from tkinter import *
import tkinter as pk
from DCM.serial_comm import writePara

from DCM.functions import Lower_Rate_Limit_Error, Ventricular_Pulse_Width_Error, Ventricular_Amplitude_Error, \
    Upper_Rate_Limit_Error,Reaction_Time_Error,Response_Factor_Error,Recovery_Time_Error,Maximum_Sensor_Rate_Error,\
    Activity_Threshold_Error



row_VOOR = []
def VOOR_window():
    root_VOOR = Tk()
    root_VOOR.title('VOOR')
    root_VOOR.geometry('430x460')

    with open("user.txt", 'r') as s_file:
        content = s_file.read()
        print(content)
    s_file.close()

    with open('{}.csv'.format(content), 'r+') as user_file:
        lines1 = user_file.readlines()
        user_file.truncate()
    user_file.close()

    for line1 in lines1:
        row_VOOR.append(line1.split(','))
        while ['"\n'] in row_VOOR:
            row_VOOR.remove(['"\n'])
    for element in row_VOOR:
        if '\n' in element:
            element.pop()

    print(row_VOOR)

    Label(root_VOOR, text='Lower Rate Limit:').grid(row=0, column=0)
    Label(root_VOOR, text='Upper Rate Limit:').grid(row=1, column=0)
    Label(root_VOOR, text='Maximum Sensor Rate:').grid(row=2, column=0)
    Label(root_VOOR, text='Ventricular Amplitude:').grid(row=3, column=0)
    Label(root_VOOR, text='Ventricular Pulse Width:').grid(row=4, column=0)
    Label(root_VOOR, text='Activity Threshold:').grid(row=5, column=0)
    Label(root_VOOR, text='Reaction Time:').grid(row=6, column=0)
    Label(root_VOOR, text='Response Factor:').grid(row=7, column=0)
    Label(root_VOOR, text='Recovery Time:').grid(row=8, column=0)

    v1 = pk.StringVar()
    v1.set(row_VOOR[8][1])
    v2 = pk.StringVar()
    v2.set(row_VOOR[8][2])
    v3 = pk.StringVar()
    v3.set(row_VOOR[8][3])
    v4 = pk.StringVar()
    v4.set(row_VOOR[8][8])
    v5 = pk.StringVar()
    v5.set(row_VOOR[8][10])
    v6 = pk.StringVar()
    v6.set(row_VOOR[8][22])
    v7 = pk.StringVar()
    v7.set(row_VOOR[8][23])
    v8 = pk.StringVar()
    v8.set(row_VOOR[8][24])
    v9 = pk.StringVar()
    v9.set(row_VOOR[8][25])

    e1 = Entry(root_VOOR, textvariable=v1)
    e2 = Entry(root_VOOR, textvariable=v2)
    e3 = Entry(root_VOOR, textvariable=v3)
    e4 = Entry(root_VOOR, textvariable=v4)
    e5 = Entry(root_VOOR, textvariable=v5)
    e6 = Entry(root_VOOR, textvariable=v6)
    e7 = Entry(root_VOOR, textvariable=v7)
    e8 = Entry(root_VOOR, textvariable=v8)
    e9 = Entry(root_VOOR, textvariable=v9)

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
    print("Maximum Sensor Rate:%s" % e3.get())
    print("Ventricular Amplitude:%s" % e4.get())
    print("Ventricular Pulse Width:%s" % e5.get())
    print("Activity Threshold:%s" % e6.get())
    print("Reaction Time:%s" % e7.get())
    print("Response Factor:%s" % e8.get())
    print("Recovery Time:%s" % e9.get())

    # LRL input detecting
    def show_VOOR_LRL():
        try:
            if isinstance(int(e1.get()), int):

                if int(int(row_VOOR[8][2]) == 0):
                    if int(e1.get()) < 30:
                        Lower_Rate_Limit_Error()
                    if 30 <= int(e1.get()) < 50:
                        if int(e1.get()) % 5 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_VOOR[8][1] = str(e1.get())
                            success()

                    if 50 <= int(e1.get()) < 90:
                        if int(e1.get()) % 1 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_VOOR[8][1] = str(e1.get())
                            success()

                    if 90 <= int(e1.get()) <= 175:
                        if int(e1.get()) % 5 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_VOOR[8][1] = str(e1.get())
                            success()

                    if int(e1.get()) > 175:
                        Lower_Rate_Limit_Error()

                else:
                    if int(e1.get()) >= int(row_VOOR[8][2]):
                        tkinter.messagebox.showerror('Error', "LRL can not be greater than URL!")

                    else:
                        if int(e1.get()) < 30:
                            Lower_Rate_Limit_Error()
                        if 30 <= int(e1.get()) < 50:
                            if int(e1.get()) % 5 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_VOOR[8][1] = str(e1.get())
                                success()

                        if 50 <= int(e1.get()) < 90:
                            if int(e1.get()) % 1 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_VOOR[8][1] = str(e1.get())
                                success()

                        if 90 <= int(e1.get()) <= 175:
                            if int(e1.get()) % 5 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_VOOR[8][1] = str(e1.get())
                                success()

                        if int(e1.get()) > 175:
                            Lower_Rate_Limit_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VOOR)
        csv_file.close()

    # URL input detecting
    def show_VOOR_URL():

        try:
            if isinstance(int(e2.get()),int):
                if int(int(row_VOOR[8][1]) == 0):
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
                            row_VOOR[8][2] = str(e2.get())
                            success()
                else:
                    if int(e2.get()) <= int(row_VOOR[8][1]):
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
                                row_VOOR[8][2] = str(e2.get())
                                success()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VOOR)
        csv_file.close()

    # Maximum Sensor Rate detecting
    def show_VOOR_MSR():
        try:
            if isinstance(int(e3.get()), int):
                if 50 <= int(e3.get()) <= 175:
                    if int(e3.get()) % 5 == 0:
                        row_VOOR[8][3] = str(e3.get())
                        success()
                    else:
                        Maximum_Sensor_Rate_Error()
                else:
                    Maximum_Sensor_Rate_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VOOR)
        csv_file.close()

    # AA input detecting


    def show_VOOR_VA():
        try:
            if isinstance(int(e4.get()), int):
                if 0 <= int(e4.get()) <= 100:
                    row_VOOR[8][8] = str(e4.get())
                    success()
                else:
                    Ventricular_Amplitude_Error()

        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

            with open('{}.csv'.format(content), 'w', newline='') as csv_file:
                cw = csv.writer(csv_file)
                cw.writerows(row_VOOR)
            csv_file.close()

    # VPW input detecting
    def show_VOOR_VPW():
        try:
            if isinstance(int(e5.get()), int):
                if 0 <= int(e5.get()) <= 20:
                    row_VOOR[8][10] = str(e5.get())
                    success()
                else:
                    Ventricular_Pulse_Width_Error()

        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VOOR)
        csv_file.close()

    # Activity Threshold
    def show_VOOR_AT():
        try:
            if isinstance(int(e6.get()), int):
                if 1 <= int(e6.get()) <= 7:
                    row_VOOR[8][22] = str(e6.get())
                    success()
                else:
                    Activity_Threshold_Error()

        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VOOR)
        csv_file.close()

    # Reaction Time
    def show_VOOR_ReactionT():
        try:
            if isinstance(int(e7.get()), int):
                if 10 <= int(e7.get()) <= 50:
                    if int(e7.get()) % 10 == 0:
                        row_VOOR[8][23] = str(e7.get())
                        success()
                    else:
                        Reaction_Time_Error()
                else:
                    Reaction_Time_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VOOR)
        csv_file.close()

    # Response Factor
    def show_VOOR_RF():
        try:
            if isinstance(int(e8.get()), int):
                if 1 <= int(e8.get()) <= 16:
                    row_VOOR[8][24] = str(e8.get())
                    success()
                else:
                    Response_Factor_Error()

        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VOOR)
        csv_file.close()

    # Recovery Time
    def show_VOOR_RecoveryT():
        try:
            if isinstance(int(e9.get()), int):
                if 2 <= int(e9.get()) <= 16:
                    row_VOOR[8][25] = str(e9.get())
                    success()
                else:
                    Recovery_Time_Error()

        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VOOR)
        csv_file.close()


    Button(root_VOOR, text='Save', width=5, command=show_VOOR_LRL).grid(row=0, column=2, padx=10, pady=5)
    Button(root_VOOR, text='Save', width=5, command=show_VOOR_URL).grid(row=1, column=2, padx=10, pady=5)
    Button(root_VOOR, text='Save', width=5, command=show_VOOR_MSR).grid(row=2, column=2, padx=10, pady=5)
    Button(root_VOOR, text='Save', width=5, command=show_VOOR_VA).grid(row=3, column=2, padx=10, pady=5)
    Button(root_VOOR, text='Save', width=5, command=show_VOOR_VPW).grid(row=4, column=2, padx=10, pady=5)
    Button(root_VOOR, text='Save', width=5, command=show_VOOR_AT).grid(row=5, column=2, padx=10, pady=5)
    Button(root_VOOR, text='Save', width=5, command=show_VOOR_ReactionT).grid(row=6, column=2, padx=10, pady=5)
    Button(root_VOOR, text='Save', width=5, command=show_VOOR_RF).grid(row=7, column=2, padx=10, pady=5)
    Button(root_VOOR, text='Save', width=5, command=show_VOOR_RecoveryT).grid(row=8, column=2, padx=10, pady=5)

    Button(root_VOOR, text='Fire', width=5, command=root_VOOR.destroy).place(x=120, y=380)
    Button(root_VOOR, text='Cancel', width=5, command=root_VOOR.destroy).place(x=190, y=380)

    mainloop()

