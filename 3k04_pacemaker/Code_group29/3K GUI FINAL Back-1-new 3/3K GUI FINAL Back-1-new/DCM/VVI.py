import tkinter.messagebox
from DCM.functions import *
import csv
from tkinter import *
import tkinter as pk
from DCM.serial_comm import writePara

from DCM.functions import Lower_Rate_Limit_Error, Ventricular_Pulse_Width_Error, Ventricular_Amplitude_Error, \
    Upper_Rate_Limit_Error,Rate_Smoothing_Error,Hysteresis_Error,VRP_Error,Ventricular_Sensitivity_Error



row_VVI = []
def VVI_window():
    global e1
    global e3
    global e4
    global e5

    root_VVI = pk.Tk()
    root_VVI.title('VVI')
    root_VVI.geometry('480x380')

    with open("user.txt", 'r') as s_file:
        content = s_file.read()
        print(content)
    s_file.close()

    with open('{}.csv'.format(content), 'r+') as user_file:
        lines1 = user_file.readlines()
        user_file.truncate()
    user_file.close()

    for line1 in lines1:
        row_VVI.append(line1.split(','))
        while ['"\n'] in row_VVI:
            row_VVI.remove(['"\n'])
    for element in row_VVI:
        if '\n' in element:
            element.pop()


    print(row_VVI)

    Label(root_VVI, text='Lower Rate Limit:').grid(row=0, column=0)
    Label(root_VVI, text='Upper Rate Limit:').grid(row=1, column=0)
    Label(root_VVI, text='Ventricular Amplitude:').grid(row=2, column=0)
    Label(root_VVI, text='Ventricular Pulse Width:').grid(row=3, column=0)
    Label(root_VVI, text='VRP:').grid(row=4, column=0)
    Label(root_VVI, text='Ventricular Sensitivity:').grid(row=5, column=0)
    Label(root_VVI, text='Hysteresis(-1 as "off"):').grid(row=6, column=0)
    Label(root_VVI, text='Rate Smoothing(-1 as "off"):').grid(row=7, column=0)

    v1 = pk.StringVar()
    v1.set(row_VVI[4][1])
    v2 = pk.StringVar()
    v2.set(row_VVI[4][2])
    v3 = pk.StringVar()
    v3.set(row_VVI[4][8])
    v4 = pk.StringVar()
    v4.set(row_VVI[4][10])
    v5 = pk.StringVar()
    v5.set(row_VVI[4][13])
    v6 = pk.StringVar()
    v6.set(row_VVI[4][12])
    v7 = pk.StringVar()
    v7.set(row_VVI[4][17])
    v8 = pk.StringVar()
    v8.set(row_VVI[4][18])

    e1 = Entry(root_VVI, textvariable=v1)
    e2 = Entry(root_VVI, textvariable=v2)
    e3 = Entry(root_VVI, textvariable=v3)
    e4 = Entry(root_VVI, textvariable=v4)
    e5 = Entry(root_VVI, textvariable=v5)
    e6 = Entry(root_VVI, textvariable=v6)
    e7 = Entry(root_VVI, textvariable=v7)
    e8 = Entry(root_VVI, textvariable=v8)


    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)
    e3.grid(row=2, column=1, padx=10, pady=5)
    e4.grid(row=3, column=1, padx=10, pady=5)
    e5.grid(row=4, column=1, padx=10, pady=5)
    e6.grid(row=5, column=1, padx=10, pady=5)
    e7.grid(row=6, column=1, padx=10, pady=5)
    e8.grid(row=7, column=1, padx=10, pady=5)

    print("Lower Rate Limit:%s" % e1.get())
    print("Upper Rate Limit:%s" % e2.get())
    print("Atrial Amplitude:%s" % e3.get())
    print("Atrial Pulse Width:%s" % e4.get())
    print("ARP:%s" % e5.get())
    print("Atrial Sensitivity:%s" % e6.get())
    print("Hysteresis:%s" % e7.get())
    print("Rate Smoothing:%s" % e8.get())




        # LRL input detecting
    def show_VVI_LRL():
        try:
            if isinstance(int(e1.get()),int):

                if int(int(row_VVI[4][2]) == 0):
                    if int(e1.get()) < 30:
                        Lower_Rate_Limit_Error()
                    if 30 <= int(e1.get()) < 50:
                        if int(e1.get()) % 5 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_VVI[4][1] = str(e1.get())
                            success()

                    if 50 <= int(e1.get()) < 90:
                        if int(e1.get()) % 1 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_VVI[4][1] = str(e1.get())
                            success()

                    if 90 <= int(e1.get()) <= 175:
                        if int(e1.get()) % 5 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_VVI[4][1] = str(e1.get())
                            success()

                    if int(e1.get()) > 175:
                        Lower_Rate_Limit_Error()

                else:
                    if int(e1.get()) >= int(row_VVI[4][2]):
                        tkinter.messagebox.showerror('Error', "LRL can not be greater than URL!")

                    else:
                        if int(e1.get()) < 30:
                            Lower_Rate_Limit_Error()
                        if 30 <= int(e1.get()) < 50:
                            if int(e1.get()) % 5 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_VVI[4][1] = str(e1.get())
                                success()

                        if 50 <= int(e1.get()) < 90:
                            if int(e1.get()) % 1 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_VVI[4][1] = str(e1.get())
                                success()

                        if 90 <= int(e1.get()) <= 175:
                            if int(e1.get()) % 5 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_VVI[4][1] = str(e1.get())
                                success()

                        if int(e1.get()) > 175:
                            Lower_Rate_Limit_Error()




        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")


        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VVI)
        csv_file.close()

    # URL input detecting
    def show_VVI_URL():
        try:
            if isinstance(int(e2.get()),int):
                if int(int(row_VVI[4][1]) == 0):
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
                            row_VVI[4][2] = str(e2.get())
                            success()
                else:
                    if int(e2.get()) <= int(row_VVI[4][1]):
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
                                row_VVI[4][2] = str(e2.get())
                                success()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VVI)
        csv_file.close()

    # VA input detecting
    def show_VVI_VA():
        try:
            if isinstance(int(e3.get()), int):
                if 0 <= int(e3.get()) <= 100:
                    row_VVI[4][8] = str(e3.get())
                    success()
                else:
                    Ventricular_Amplitude_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VVI)
        csv_file.close()

    #   VPM input detecting
    def show_VVI_VPW():
        try:
            if isinstance(int(e4.get()), int):
                if 0 <= int(e4.get()) <= 20:
                    row_VVI[4][10] = str(e4.get())
                    success()
                else:
                    Ventricular_Pulse_Width_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VVI)
        csv_file.close()

    # ARP input detecting
    def show_VVI_VRP():
        try:
            if isinstance(int(e5.get()), int):
                if int(e5.get()) < 150 or int(e5.get()) > 500:
                    VRP_Error()
                else:
                    if int(e5.get()) % 10 != 0:
                        VRP_Error()
                    else:
                        row_VVI[4][13] = str(e5.get())
                        success()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VVI)
        csv_file.close()

    # AS input detecting
    def show_VVI_VS():
        try:
            if isinstance(int(e6.get()), int):
                if int(e6.get()) * 100 == 25 or int(e6.get()) * 100 == 50 or int(e6.get()) * 100 == 75:
                    row_VVI[4][12] = str(e6.get())
                    success()
                elif int(e6.get()) >= 10 and int(e6.get()) <= 100:
                    if int(e6.get()) % 5 == 0:
                        row_VVI[4][12] = str(e6.get())
                        success()

                else:
                    Ventricular_Sensitivity_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers only!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VVI)
        csv_file.close()


    # Hysteresis input detecting
    def show_VVI_Hysteresis():
        try:
            if isinstance(int(e7.get()),int):
                if 0< int(e7.get()) < 30:
                    print('yes')
                    Hysteresis_Error()
                elif 30 <= int(e7.get()) < 50:
                    if int(e7.get()) % 5 != 0:
                        Hysteresis_Error()
                    else:
                        row_VVI[4][17] = str(e7.get())
                        success()
                elif 50 <= int(e7.get()) < 90:
                    if int(e7.get()) % 1 != 0:
                        Hysteresis_Error()

                    else:
                        row_VVI[4][17] = str(e7.get())
                        success()
                elif 90 <= int(e7.get()) <= 175:
                    if int(e7.get()) % 5 != 0:
                        Hysteresis_Error()

                    else:
                        row_VVI[4][17] = str(e7.get())
                        success()
                elif int(e7.get()) > 175:
                    Hysteresis_Error()

                elif int(e7.get()) == -1:
                    row_VVI[4][17] = str(e7.get())
                    success()

                else:
                    Hysteresis_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers or only use -1 as 'off'!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VVI)
        csv_file.close()


    # Rate Smoothing input detecting
    def show_VVI_RS():
        try:
            if isinstance(int(e8.get()),int):
                if int(e8.get()) == 3 or int(e8.get()) == 6 or int(e8.get()) == 9 or int(e8.get()) == 12 :
                    row_VVI[4][18] = str(e8.get())
                    success()
                elif int(e8.get()) == 15 or int(e8.get()) == 18 or int(e8.get()) == 21 or int(e8.get()) == 25 :
                    row_VVI[4][18] = str(e8.get())
                    success()
                elif int(e8.get()) == -1:
                    row_VVI[4][18] = str(e8.get())
                    success()
                else:
                    Rate_Smoothing_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers or only use -1 as 'off'!")


        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_VVI)
        csv_file.close()

    Button(root_VVI, text='Save', width=5, command=show_VVI_LRL).grid(row=0, column=2, padx=10, pady=5)
    Button(root_VVI, text='Save', width=5, command=show_VVI_URL).grid(row=1, column=2, padx=10, pady=5)
    Button(root_VVI, text='Save', width=5, command=show_VVI_VA).grid(row=2, column=2, padx=10, pady=5)
    Button(root_VVI, text='Save', width=5, command=show_VVI_VPW).grid(row=3, column=2, padx=10, pady=5)
    Button(root_VVI, text='Save', width=5, command=show_VVI_VRP).grid(row=4, column=2, padx=10, pady=5)
    Button(root_VVI, text='Save', width=5, command=show_VVI_VS).grid(row=5, column=2, padx=10, pady=5)
    Button(root_VVI, text='Save', width=5, command=show_VVI_Hysteresis).grid(row=6, column=2, padx=10, pady=5)
    Button(root_VVI, text='Save', width=5, command=show_VVI_RS).grid(row=7, column=2, padx=10, pady=5)

    Button(root_VVI, text='Fire', width=5, command=trans).place(x=160, y=330)
    Button(root_VVI, text='Cancel', width=5, command=root_VVI.destroy).place(x=280, y=330)

    mainloop()


def trans():
    writePara(mode=4, Lower_Rate=int(e1.get()), ATR_Amplitude=int(e3.get()), ATR_Width=int(e4.get()),
              VENT_Refractory=int(e5.get())),
    successFire()