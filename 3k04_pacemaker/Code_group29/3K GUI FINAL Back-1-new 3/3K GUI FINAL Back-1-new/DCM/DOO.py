import tkinter.messagebox
from DCM.functions import *
import csv
from tkinter import *
import tkinter as pk
from DCM.serial_comm import writePara

from DCM.functions import Lower_Rate_Limit_Error, Atrial_Pulse_Width_Error, Atrial_Amplitude_Error, \
    Upper_Rate_Limit_Error,FixDelay_Error,Ventricular_Amplitude_Error, Ventricular_Pulse_Width_Error


row_DOO = []
def DOO_window():
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7

    root_DOO = pk.Tk()
    root_DOO.title('DOO')
    root_DOO.geometry('460x330')

    with open("user.txt", 'r') as s_file:
        content = s_file.read()
        print(content)
    s_file.close()

    with open('{}.csv'.format(content), 'r+') as user_file:
        lines1 = user_file.readlines()
        user_file.truncate()
    user_file.close()

    for line1 in lines1:
        row_DOO.append(line1.split(','))
        while ['"\n'] in row_DOO:
            row_DOO.remove(['"\n'])
    for element in row_DOO:
        if '\n' in element:
            element.pop()

    print(row_DOO)

    Label(root_DOO, text='Lower Rate Limit:').grid(row=0, column=0)
    Label(root_DOO, text='Upper Rate Limit:').grid(row=1, column=0)
    Label(root_DOO, text='Fixed AV Delay:').grid(row=2, column=0)
    Label(root_DOO, text='Atrial Amplitude:').grid(row=3, column=0)
    Label(root_DOO, text='Ventricular Amplitude:').grid(row=4, column=0)
    Label(root_DOO, text='Atrial Pulse Width:').grid(row=5, column=0)
    Label(root_DOO, text='Ventricular Pulse Width:').grid(row=6, column=0)

    v1 = pk.StringVar()
    v1.set(row_DOO[5][1])
    v2 = pk.StringVar()
    v2.set(row_DOO[5][2])
    v3 = pk.StringVar()
    v3.set(row_DOO[5][4])
    v4 = pk.StringVar()
    v4.set(row_DOO[5][7])
    v5 = pk.StringVar()
    v5.set(row_DOO[5][8])
    v6 = pk.StringVar()
    v6.set(row_DOO[5][9])
    v7 = pk.StringVar()
    v7.set(row_DOO[5][10])

    e1 = Entry(root_DOO, textvariable=v1)
    e2 = Entry(root_DOO, textvariable=v2)
    e3 = Entry(root_DOO, textvariable=v3)
    e4 = Entry(root_DOO, textvariable=v4)
    e5 = Entry(root_DOO, textvariable=v5)
    e6 = Entry(root_DOO, textvariable=v6)
    e7 = Entry(root_DOO, textvariable=v7)

    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)
    e3.grid(row=2, column=1, padx=10, pady=5)
    e4.grid(row=3, column=1, padx=10, pady=5)
    e5.grid(row=4, column=1, padx=10, pady=5)
    e6.grid(row=5, column=1, padx=10, pady=5)
    e7.grid(row=6, column=1, padx=10, pady=5)


    print("Lower Rate Limit:%s" % e1.get())
    print("Upper Rate Limit:%s" % e2.get())
    print("Atrial Amplitude:%s" % e3.get())
    print("Atrial Pulse Width:%s" % e4.get())
    print("ARP:%s" % e5.get())




    def show_DOO_LRL():
        # LRL input detecting
        try:
            if isinstance(int(e1.get()),int):

                if int(int(row_DOO[5][2]) == 0):
                    if int(e1.get()) < 30:
                        Lower_Rate_Limit_Error()
                    if 30 <= int(e1.get()) < 50:
                        if int(e1.get()) % 5 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_DOO[5][1] = str(e1.get())
                            success()

                    if 50 <= int(e1.get()) < 90:
                        if int(e1.get()) % 1 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_DOO[5][1] = str(e1.get())
                            success()

                    if 90 <= int(e1.get()) <= 175:
                        if int(e1.get()) % 5 != 0:
                            Lower_Rate_Limit_Error()

                        else:
                            row_DOO[5][1] = str(e1.get())
                            success()

                    if int(e1.get()) > 175:
                        Lower_Rate_Limit_Error()

                else:
                    if int(e1.get()) >= int(row_DOO[5][2]):
                        tkinter.messagebox.showerror('Error', "LRL can not be greater than URL!")

                    else:
                        if int(e1.get()) < 30:
                            Lower_Rate_Limit_Error()
                        if 30 <= int(e1.get()) < 50:
                            if int(e1.get()) % 5 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_DOO[5][1] = str(e1.get())
                                success()

                        if 50 <= int(e1.get()) < 90:
                            if int(e1.get()) % 1 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_DOO[5][1] = str(e1.get())
                                success()

                        if 90 <= int(e1.get()) <= 175:
                            if int(e1.get()) % 5 != 0:
                                Lower_Rate_Limit_Error()

                            else:
                                row_DOO[5][1] = str(e1.get())
                                success()

                        if int(e1.get()) > 175:
                            Lower_Rate_Limit_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")


        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_DOO)
        csv_file.close()

        # URL input detecting
    def show_DOO_URL():
        try:
            if isinstance(int(e2.get()), int):
                if int(int(row_DOO[1][1]) == 0):
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
                            row_DOO[1][2] = str(e2.get())
                            success()
                else:
                    if int(e2.get()) <= int(row_DOO[1][1]):
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
                                row_DOO[1][2] = str(e2.get())
                                success()


        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_DOO)
        csv_file.close()

    # Fixed AV Delay input detecting
    def show_DOO_FixDelay():
        try:
            if isinstance(int(e3.get()),int):
                if 70 <= int(e3.get()) <= 300:
                    if int(e3.get()) % 10 != 0:
                        FixDelay_Error()
                    row_DOO[5][4] = str(e3.get())
                    success()
                else:
                    Atrial_Amplitude_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_DOO)
        csv_file.close()



    # AA input detecting
    def show_DOO_AA():
        try:
            if isinstance(int(e4.get()),int):
                if 0 <= int(e4.get()) <= 100:
                    row_DOO[5][7] = str(e4.get())
                    success()
                else:
                    Atrial_Amplitude_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_DOO)
        csv_file.close()

    # VA input detecting
    def show_DOO_VA():
        try:
            if isinstance(int(e5.get()),int):
                if 0 <= int(e5.get()) <= 100:
                    row_DOO[5][8] = str(e5.get())
                    success()
                else:
                    Ventricular_Amplitude_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_DOO)
        csv_file.close()

    #APW input detecting
    def show_DOO_APW():
        try:
            if isinstance(int(e6.get()),int):
                if 0 <= int(e6.get()) <= 20:
                    row_DOO[5][9] = str(e6.get())
                    success()
                else:
                    Atrial_Pulse_Width_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_DOO)
        csv_file.close()

    #VPM input detecting
    def show_DOO_VPW():
        try:
            if isinstance(int(e7.get()),int):
                if 0 <= int(e7.get()) <= 20:
                    row_DOO[5][10] = str(e7.get())
                    success()
                else:
                    Ventricular_Pulse_Width_Error()
        except:
            tkinter.messagebox.showerror('Error', "Please use integers!")

        with open('{}.csv'.format(content), 'w', newline='') as csv_file:
            cw = csv.writer(csv_file)
            cw.writerows(row_DOO)
        csv_file.close()

    Button(root_DOO, text='Save', width=5, command=show_DOO_LRL).grid(row=0, column=2, padx=10, pady=5)
    Button(root_DOO, text='Save', width=5, command=show_DOO_URL).grid(row=1, column=2, padx=10, pady=5)
    Button(root_DOO, text='Save', width=5, command=show_DOO_FixDelay).grid(row=2, column=2, padx=10, pady=5)
    Button(root_DOO, text='Save', width=5, command=show_DOO_AA).grid(row=3, column=2, padx=10, pady=5)
    Button(root_DOO, text='Save', width=5, command=show_DOO_VA).grid(row=4, column=2, padx=10, pady=5)
    Button(root_DOO, text='Save', width=5, command=show_DOO_APW).grid(row=5, column=2, padx=10, pady=5)
    Button(root_DOO, text='Save', width=5, command=show_DOO_VPW).grid(row=6, column=2, padx=10, pady=5)

    Button(root_DOO, text='Fire', width=5, command=trans).place(x=150, y=290)
    Button(root_DOO, text='Cancel', width=5, command=root_DOO.destroy).place(x=270, y=290)

    mainloop()

row_DOO = []


def trans():
    writePara(mode=5, Lower_Rate=int(e1.get()), MSR=int(e2.get()), AV_Delay=int(e3.get()), ATR_Amplitude=int(e4.get()),
              VENT_Amplitude=int(e5.get()), ATR_Width=int(e6.get()), VENT_Width=int(e7.get()))
    successFire()