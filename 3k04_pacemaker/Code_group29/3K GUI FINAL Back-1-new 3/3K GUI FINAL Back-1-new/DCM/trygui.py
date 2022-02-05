import tkinter.messagebox
from DCM.functions import *
import csv
from tkinter import ttk
from DCM.AAI import AAI_window
from DCM.AAIR import AAIR_window
from DCM.AOO import AOO_window
from DCM.AOOR import AOOR_window
from DCM.DDD import DDD_window
from DCM.DOO import DOO_window
from DCM.VOO import VOO_window
from DCM.VOOR import VOOR_window
from DCM.VVI import VVI_window
from DCM.VVIR import VVIR_window
from DCM.serial_comm import writePara
import tkinter as pk

counter = 0
data = []
state = content = 'Yes'
situation = True
condition = -1
cond = 1


def main_window():
    global window
    global username
    global userPswd
    global username_input
    global userPswd_input


    # Main Window
    window = pk.Tk()
    window.title("Pacemaker")
    window.geometry('400x355')
    # BackGround Picture & Text
    back = pk.Canvas(window, width=400, height=400, bg='pink')
    image_file = pk.PhotoImage(file='animeheart.gif')
    back.create_image(200, 0, anchor='n', image=image_file)
    back.pack(side='top')
    pk.Label(window, text="Welcome to Pacemaker", font=("Times New Roman", 17)).pack()

    # User Name & Password Text
    pk.Label(window, text="User Name :", bg='pink', font=("Times New Roman", 15)).place(x=50, y=215)
    pk.Label(window, text="Password :", bg='pink', font=("Times New Roman", 15)).place(x=50, y=255)

    # User Name Block
    username = pk.StringVar()
    username.set('example@mcmaster.ca')
    username_input = pk.Entry(window, textvariable=username, font=("Times New Roman", 14), show=None)
    username_input.place(x=160, y=215)

    # User Password Block
    userPswd = pk.StringVar()
    userPswd_input = pk.Entry(window, textvariable=userPswd, font=("Times New Roman", 14), show='*')
    userPswd_input.place(x=160, y=255)

    # Log in & Sign Up Buttons
    blk_login = pk.Button(window, text="Log In", command=user_login, width=6)
    blk_login.place(x=270, y=295)
    blk_signup = pk.Button(window, text="Sign Up", command=user_sign_up, width=6)
    blk_signup.place(x=160, y=295)


    # print(type(username))
    # print(type(userPswd))
    # print(type(username_input))
    # print(type(userPswd_input))
    # Loop for Main Window
    window.mainloop()


# Function Window Only
def function_window():
    global func_window
    global roll

    func_window = pk.Tk()
    func_window.title("Function")
    func_window.geometry('280x200')

    la_mode = pk.Label(func_window, text='Mode')
    la_mode.place(x=115, y=50)
    bt_go = pk.Button(func_window, width=6, text='Go', command=modeChoose)
    bt_go.place(x=70, y=120)
    bt_cancel = pk.Button(func_window, width=6, text='Cancel', command=lambda:[func_window.destroy(), main_window()])
    bt_cancel.place(x=150, y=120)

    mode = pk.StringVar()
    roll = ttk.Combobox(func_window, width=15, height=5, textvariable=mode, state='readonly')
    roll['values'] = ('AOO', 'VOO', 'AAI', 'VVI', 'DOO', 'DDD', 'AOOR', 'VOOR', 'AAIR', 'VVIR')
    roll.place(x=70, y=80)
    roll.current(0)


def modeChoose():
    if roll.current() == 0:
        AOO_window()
    elif roll.current() == 1:
        VOO_window()
    elif roll.current() == 2:
        AAI_window()
    elif roll.current() == 3:
        VVI_window()
    elif roll.current() == 4:
        DOO_window()
    elif roll.current() == 5:
        DDD_window()
    elif roll.current() == 6:
        AOOR_window()
    elif roll.current() == 7:
        VOOR_window()
    elif roll.current() == 8:
        AAIR_window()
    elif roll.current() == 9:
        VVIR_window()
    # elif roll.current() == 10:
    #    DOOR_window()
    # elif roll.current() == 11:
    #    DDDR_window()


# Login function
def user_login():
    global state
    global user_name
    global condition
    global column_name

    user_name = username.get()
    user_pswd = userPswd.get()

    try:
        with open('userdata.csv', 'r') as csvfile1:
            lines2 = csvfile1.readlines()
        csvfile1.close()
        row2 = []
        column_name = []
        column_pswd = []
        for line2 in lines2:
            row2.append(line2.split(','))
            while ['\n'] in row2:
                row2.remove(['\n'])
        for element in row2:
            element.pop()

        for col2 in row2:
            column_name.append(col2[1])
        for col3 in row2:
            column_pswd.append(col3[2])
        print(type(column_name))
        print(column_pswd)
        print("--------------")
    except FileNotFoundError:
        # file = open('userdata.csv','w')
        # file.close()
        pass

    #content in state shows 'Yes' meaning there are places for signing up
    try:
        with open('state.txt', 'r') as s_file:
            content = s_file.read()
    except FileNotFoundError:
        with open('state.txt', 'w') as s_file:
            s_file.write("Yes")
    s_file.close()

    try:
        # if len(column_name) != 0 and content == 'Yes':
        for element in column_name:
            # print(user_name == element)
            # print(column_name.index(str(user_name)))
            # print("//////")
            # print(column_pswd[column_name.index(user_name)] == user_pswd)
            if user_name == '':
                tkinter.messagebox.showerror("Error", "Do not blank your username!")
                break
            if user_pswd == '':
                tkinter.messagebox.showerror("Error","Do not blank your password!")
                break
            elif user_name == element:
                if column_pswd[column_name.index(user_name)] == user_pswd:
                    # print("cool")
                    condition = 1
                    break
            elif user_name != column_name[len(column_name)-1]:
                condition = 3


        for element2 in column_name:
            if user_name == element2:
                if column_pswd[column_name.index(user_name)] != user_pswd:
                    condition = 2


        # elif content != 'Yes':
        #     tkinter.messagebox.showinfo('No vacancies!', 'Sorry! You do not sign up and there is no room for registration!')
    except:
        is_sign_up = tkinter.messagebox.askyesno('Welcome! ', 'You have not sign up yet. Sign up now?')

        # ask them if need to sign up
        if is_sign_up:
            user_sign_up()

        # ask them if need to sign up
        # if is_sign_up:
        #     user_sign_up()

    if condition == 3:
        # print("sign up")
        is_sign_up = tkinter.messagebox.askyesno('Welcome! ', 'You have not sign up yet. Sign up now?')

        # ask them if need to sign up
        if is_sign_up:
            user_sign_up()

    elif condition == 2:

        print("wrong")
        tkinter.messagebox.showerror(message='Error, your password is wrong, try again! ')
    # break

    elif condition == 1:

        tkinter.messagebox.showinfo(title='Welcome!', message='Hi! ' + user_name)
        function_window()

        data = ['mode', 'Lower Rate Limit', 'Upper Rate Limit', 'Maximum Sensor Rate', 'Fixed AV Delay',
                'Dynamic AV Delay',
                'Sensed AV Delay Offset', 'Atrial Amplitude', 'Ventricular Amplitude', 'Atrial Pulse Width',
                'Ventricular Pulse Width', 'Atrial Sensitivity', 'Ventricular Sensitivity', 'VRP', 'ARP', 'PVARP',
                'PVARP Extension', 'Hysteresis', 'Rate Smoothing', 'ATR Duration', 'ATR Fallback Mode',
                'ATR Fallback Time',
                'Activity Threshold', 'Reaction Time', 'Response Factor', 'Recovery Time','']
        # print(len(data))
        try:
            with open('{}.csv'.format(user_name), 'r', newline='') as user_file:
                pass
        except FileNotFoundError:
            with open('{}.csv'.format(user_name), 'w', newline='') as user_file:
                cw = csv.writer(user_file, dialect='excel')
                cw.writerow(data)
                cw.writerow(
                    ['AOO', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                     '0',
                     '0', '0', '0', '0', '0', '0',''])
                cw.writerow(
                    ['VOO', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                     '0',
                     '0', '0', '0', '0', '0', '0',''])
                cw.writerow(
                    ['AAI', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                     '0',
                     '0', '0', '0', '0', '0', '0',''])
                cw.writerow(
                    ['VVI', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                     '0',
                     '0', '0', '0', '0', '0', '0',''])
                cw.writerow(
                    ['DOO', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                     '0',
                     '0', '0', '0', '0', '0', '0', ''])
                cw.writerow(
                    ['DDD', '60', '120', '0', '150', '-1', '-1', '3.75', '3.75', '0.4', '0.4', '0.75', '2.5', '320', '250', '250', '-1', '-1', '-1',
                     '20',
                     '-1', '1', '0', '0', '0', '0', ''])
                cw.writerow(
                    ['AOOR', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                     '0',
                     '0', '0', '0', '0', '0', '0', ''])
                cw.writerow(
                    ['VOOR', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                     '0',
                     '0', '0', '0', '0', '0', '0', ''])
                cw.writerow(
                    ['AAIR', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                     '0',
                     '0', '0', '0', '0', '0', '0', ''])
                cw.writerow(
                    ['VVIR', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                     '0',
                     '0', '0', '0', '0', '0', '0', ''])
                cw.writerow(
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                     ' ',
                     ' ', ' ', ' ', ' ', ' ', ' ', ''])
        user_file.close()

        window.destroy()
        # break
        # print(type(func_window))
        # print(type(roll))
        with open('user.txt', 'w') as user_file:
            user_file.write(user_name)
        user_file.close()



# Sign up function
def user_sign_up():
    global register_window
    global counter
    global state
    global situation

    window.destroy()

    try:
        with open('userdata.csv', 'r') as user_file:
            pass
    except FileNotFoundError:
        user_file = open("userdata.csv", "w")
    user_file.close()

    def sign_to_Pacemaker():
        global counter
        global state
        global situation


        # below is what we need to know form the sign-up infomation
        newPswd = new_pswd.get()
        newPswdConfirm = new_pswd_confirm.get()
        newName = new_name.get()

        with open('userdata.csv', 'r') as usr_file:
            lines1 = usr_file.readlines()
            usr_file.close()
            row1 = []
            column1 = []
            for line1 in lines1:
                row1.append(line1.split(','))
                while ['\n'] in row1:
                    row1.remove(['\n'])
            for element in row1:
                element.pop()
            print("row1:")
            print(row1)
            for col1 in row1:
                column1.append(col1[1])
            print("column1:")
            print(column1)
            # print(len(column1))
            for element in column1:
                # print(element)
                if element == newName:
                    situation = False
                    tkinter.messagebox.showerror('Error', 'The user has already signed up!')


        if newPswd == '':
            situation = False
            tkinter.messagebox.showerror('Error', 'Password cannot be blank!')

        elif newName == '':
            situation = False
            tkinter.messagebox.showerror('Error', 'Name cannot be blank!')

        elif newPswd != newPswdConfirm:
            situation = False
            tkinter.messagebox.showerror('Error', 'Password and confirm password must be the same!')


        else:
            try:
                with open('state.txt', 'r+') as s_file:
                    state = s_file.read()
            except FileNotFoundError:
                with open('state.txt', 'w') as s_file:
                    s_file.write("Yes")
            s_file.close()

            if state == 'Yes' and situation == True:

                counter = counter + 1
                data_personal = []
                data_personal.append(counter)
                data_personal.append(newName)
                data_personal.append(newPswd)
                data_personal.append(newPswdConfirm)
                data_personal.append('')
                data.append(data_personal)

                try:
                    with open("userdata.csv", "w+") as csvfile:
                        cw = csv.writer(csvfile)
                        for item in data:
                            cw.writerow(item)

                except:  # If file does not exist, create it
                    csvfile = open("userdata.csv", "w")
                csvfile.close()

                file = open("userdata.csv", "r")
                lines = file.readlines()
                file.close()
                row = []
                column = []
                for line in lines:
                    row.append(line.split(','))
                    while ['\n'] in row:
                        row.remove(['\n'])
                for element in row:
                    element.pop()

                print("row[0]:")
                print(row[0])
                for col in row:
                    column.append(col[0])
                if len(column) - 1 < 0:
                    num_col = 1
                else:
                    num_col = (column[len(column) - 1])

                print("num_col:")
                print(num_col)

                #situation shows whether there is something wrong while signing up
                if (int(num_col)) < 3 and state == 'Yes':
                    tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up! ')
                    situation == True
                    # exist_usr_info[newName] = newPswd
                    # with open('usrs_info.txt', 'wb') as usr_file:
                    #     pickle.dump(exist_usr_info, usr_file)
                    register_window_close()

                elif (int(num_col)) == 3:
                    with open('state.txt', 'w+') as s_file:
                        s_file.write("No")
                    s_file.close()
                    tkinter.messagebox.showinfo('Congratulations', 'Wow, you are the last person to sign up! ')
                    register_window_close()


                else:
                    tkinter.messagebox.showerror('Error', 'Sorry! There are no more vacancies!!! ')
                    register_window_close()
            elif state == 'Yes' and situation == False:
                with open('state.txt', 'w+') as s_file:
                    s_file.write("No")
                    situation = True
                tkinter.messagebox.showerror('Error', 'Sorry! Please try it again! ')
                register_window_close()
            elif state == 'No' and situation == True:
                tkinter.messagebox.showerror('Error', 'Sorry! There are no more vacancies! ')
                register_window_close()
            else:
                tkinter.messagebox.showerror('Error', 'Please try it again! ')


    register_window = pk.Tk()
    register_window.geometry('380x220')
    register_window.title('Register')

    # User Name Block
    new_name = pk.StringVar()
    new_name.set('example@mcmaster.ca')
    pk.Label(register_window, text='User name: ', font=("Times New Roman", 14)).place(x=18, y=35)
    name_input = pk.Entry(register_window, textvariable=new_name, font=("Times New Roman", 14))
    name_input.place(x=175, y=35)

    # User Password Block
    new_pswd = pk.StringVar()
    pk.Label(register_window, text='Password: ', font=("Times New Roman", 14)).place(x=18, y=75)
    new_pswd_input = pk.Entry(register_window, textvariable=new_pswd, font=("Times New Roman", 14), show='*')
    new_pswd_input.place(x=175, y=75)

    # User Confirm Block
    new_pswd_confirm = pk.StringVar()
    pk.Label(register_window, text='Confirm Password: ', font=("Times New Roman", 14)).place(x=18, y=115)
    confirm_input = pk.Entry(register_window, textvariable=new_pswd_confirm, font=("Times New Roman", 14), show='*')
    confirm_input.place(x=175, y=115)

    # Register & Cancel Buttons
    blk_register = pk.Button(register_window, text="Sign Up", command=sign_to_Pacemaker)
    blk_register.place(x=90, y=165)
    blk_cancel = pk.Button(register_window, text="Cancel", command=lambda:[register_window.destroy(), main_window()])
    blk_cancel.place(x=230, y=165)
    print(type(register_window))
    print(type(counter))
    print(type(state))
    print(type(situation))


def register_window_close():
    register_window.destroy()
    main_window()

# Main Window Pop Up
main_window()
