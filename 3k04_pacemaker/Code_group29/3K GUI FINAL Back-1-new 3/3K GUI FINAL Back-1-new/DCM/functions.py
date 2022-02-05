import tkinter.messagebox


def successFire():
    tkinter.messagebox.showinfo('Success', 'Successfully Fired!')


def success():
    tkinter.messagebox.showinfo('Success', 'Successfully saved!')


def Lower_Rate_Limit_Error():
    tkinter.messagebox.showerror('Error', 'Invalid Lower Rate Limit entered!\nPlease use another number!')
    tkinter.messagebox.showinfo("Tips",
                                "The value should be in one of the list below:\n - 30~50 with increment by 5\n -50~90 with increment by 1\n -  90~175 with increment by 5")


def Upper_Rate_Limit_Error():
    tkinter.messagebox.showerror('Error', 'Invalid Upper Rate Limit entered!\nPlease use another number!')
    tkinter.messagebox.showinfo("Tips",
                                "The value should be in the range of 50~175 with increment by 5")


def Ventricular_Amplitude_Error():
    tkinter.messagebox.showerror('Error', 'Invalid Ventricular Amplitude entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips', 'The value should be the one in the range of 0~100 with the increment by 1')


def Atrial_Amplitude_Error():
    tkinter.messagebox.showerror('Error', 'Invalid Atrial Amplitude entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips', 'The value should be the one in the range of 0~100 with the increment by 1')


def Ventricular_Pulse_Width_Error():
    tkinter.messagebox.showerror('Error',
                                 'Invalid Ventricular Pulse Width entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips',
                                'The value should be in one of the list below:\n- 0~20 with increment by 1')

def Atrial_Pulse_Width_Error():
    tkinter.messagebox.showerror('Error',
                                 'Invalid Atrial Pulse Width entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips',
                                'The value should be in one of the list below:\n- 0~20 with increment by 1')


def ARP_Error():
    tkinter.messagebox.showerror('Error', 'Invalid ARP entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips', 'The value should be in the range of 150~500 with the increment by 10')


def VRP_Error():
    tkinter.messagebox.showerror('Error', 'Invalid VRP entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips', 'The value should be in the range of 150~500 with the increment by 10')


def Atrial_Sensitivity_Error():
    tkinter.messagebox.showerror('Error', 'Invalid Atrial Sensitivity entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips',
                                'The value should be in the list below:\n- 0.25\t0.5\t0.75\n- 1.0~10 with the increment by 0.5')

def Ventricular_Sensitivity_Error():
    tkinter.messagebox.showerror('Error', 'Invalid Ventricular Sensitivity entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips',
                                'The value should be in the list below:\n- 0.25\t0.5\t0.75\n- 1.0~10 with the increment by 0.5')


def Hysteresis_Error():
    tkinter.messagebox.showerror('Error', 'Invalid Hysteresis entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips',
                                'The value should be in the list below:\n- off(use -1 to represent)\n- 30~50 with increment by 5\n -50~90 with increment by 1\n -  90~175 with increment by 5')


def Rate_Smoothing_Error():
    tkinter.messagebox.showerror('Error', 'Invalid Hysteresis entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips',
                                'The value should be in the list below:\n- off(use -1 to represent)\n- 3\t6\t9\t12\n- 15\t18\t21\t25\n(note:the system has % already,you just put an integer here!')

def PVARP_Error():
    tkinter.messagebox.showerror('Error', 'Invalid PVARP entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips',
                                'The value should be in the range of 150~500 with the increment by 10')

def FixDelay_Error():
    tkinter.messagebox.showerror('Error', 'Invalid Fixed AV Delay entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips',
                                'The value should be in the range of 70~300 with the increment by 10')

def Reaction_Time_Error():
    tkinter.messagebox.showerror('Error', 'Invalid Reaction Time Error entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips',
                                'The value should be in the range of 10~50 with the increment by 10')


def Response_Factor_Error():
    tkinter.messagebox.showerror('Error', 'Invalid Reaction Factor Error entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips',
                                'The value should be in the range of 1~16 with the increment by 1')


def Recovery_Time_Error():
    tkinter.messagebox.showerror('Error', 'Invalid Recovery Factor Error entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips',
                                'The value should be in the range of 2~16 with the increment by 1')

def Activity_Threshold_Error():
    tkinter.messagebox.showerror('Error', 'Invalid Activity Threshold Error entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips',
                                'The value should be:\n-1)V-Low(put integer 1)\n-2)Low(put integer 2)\n-3)Med-Low(put '
                                'integer 3\n-4)Med(put integer 4)\n-5)Med-High(put integer 5)\n-6)High(put integer '
                                '6)\n-7)V-High(put integer 7)')


def Maximum_Sensor_Rate_Error():
    tkinter.messagebox.showerror('Error', 'Invalid Maximum Sensor Rate Error entered!\nPlease use another number!')
    tkinter.messagebox.showinfo('Tips',
                                'The value should be in the range of 50~175 with the increment by 5')

# def Amplitude_Error():
#     tkinter.messagebox.showerror('Error', 'Invalid Amplitude entered!\nPlease use another number!')
#     tkinter.messagebox.showinfo('Tips',
#                                 'The value should be in the list below:\n- off\n- 3\t6\t9\t12\n- 15\t18\t21\t25')


# def Pulse_Width_Error():
#     tkinter.messagebox.showerror('Error', 'Invalid Pulse width entered!\nPlease use another number!')



