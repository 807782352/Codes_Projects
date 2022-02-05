# -*- coding: utf-8 -*-
# @Organization  : ${CAPSTONE PROJECT - GROUP 25}
# @Author        : Ziyi(Kyrie) Xu
# @Time          : ${Feb/03/2021}
# @Description   : UI Module for the HMSD project

import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk
# from Crypto.Cipher import AES
import mysql.connector.pooling
import page.LoginPage as lp
import re 

class RegisterPage(object):

    def __init__(self,login_page):
        # self.goLogin = login_page

        self.root = tk.Tk()
        self.height = 300
        self.width = 300
        self.resize = (100,100)
        self.root.geometry('%dx%d' % (self.width,self.height))
        self.root.title('Registration')
        self.username = tk.StringVar(value="example@mcmaster.ca")
        self.name_pattern = tk.StringVar(value= r'^[a-zA-Z]+[0-9]*@mcmaster.ca')
        self.password = tk.StringVar()
        self.con_password = tk.StringVar()
        self.pswd_pattern = tk.StringVar(value= r'^[a-zA-Z0-9]\w{5,17}$')
        self.file_path = tk.StringVar(value="image\logo.jpg")
        self.createRegister()

    def createRegister(self):
        canvas = tk.Canvas(self.root,bg="white",width=self.width, height=self.height/3+10)
        canvas.pack()
        img = ImageTk.PhotoImage(Image.open(self.file_path.get()).resize(self.resize),master=canvas)
        canvas.create_image((self.width/2-self.resize[0]/2),5,anchor='nw',image=img)
        
        self.page = tk.Frame(self.root) # to create a Frame
        self.page.pack()    

        # Layout of Username and Password
        l_name = tk.Label(self.page, text='Username: ')
        l_name.grid(row=1,stick='W',pady=0)
        e_name = tk.Entry(self.page, textvariable=self.username,show=None)
        e_name.grid(row=2,column=0,stick='W',pady=0)
        l_pswd = tk.Label(self.page, text='Password: ')
        l_pswd.grid(row=3,stick='W',pady=0)
        e_pswd = tk.Entry(self.page, textvariable=self.password,show='*')
        e_pswd.grid(row=4,column=0,stick='W',pady=0)
        l_pswd2 = tk.Label(self.page, text='Confirmed Password: ')
        l_pswd2.grid(row=5,stick='W',pady=0)
        e_pswd2 = tk.Entry(self.page, textvariable=self.con_password,show='*')
        e_pswd2.grid(row=6,column=0,stick='W',pady=0)

        # Layout of buttons 
        b_signup = tk.Button(self.page,text="Sign Up",command=self.sign_up)
        b_signup.grid(row=7,stick="W",pady=10)
        b_back = tk.Button(self.page,text="Back",command=self.go_login)
        b_back.grid(row=7,column=0,stick="E",pady=10)

        self.root.mainloop()
    
    def go_login(self):
        self.root.destroy()
        rt = tk.Tk()
        rt.title('HMSD')
        lp.LoginPage(rt)

    def sign_up(self):
        config={
            "host":"localhost",
            "port":3306,
            "user":"root",
            "password":"123456",
            "database":"HMSD"
        }
        
        try:
            pool = mysql.connector.pooling.MySQLConnectionPool(
                **config,
                pool_size=10
            )
            con = pool.get_connection()
            con.start_transaction()
            cursor=con.cursor()
            # 这里要对限制做补充！
            # Note: 64 characters for the "local part" (username).
                    # 1 character for the @ symbol.
                    # 255 characters for the domain name.
            sql="CREATE TABLE IF NOT EXISTS Users (Username VARCHAR(400) NOT NULL UNIQUE, \
                Password TEXT NOT NULL, Mode int, SpeedLevel int, \
                TorqueLevel int)"
            cursor.execute(sql)
            if self.reg_check():
                # Below: make sure the strings have " " 
                sql="INSERT INTO Users VALUES (" + '"' + self.username.get() + '"' + "," + "HEX(AES_ENCRYPT(" + '"' + self.password.get() + '"' +",\"HMSD\"))"
                sql+= "," "0,0,0)"
                print(sql)
                cursor.execute(sql,)
                tk.messagebox.showinfo(title="Success",message="Congratulations! You have successfully signed up!!!")
            
        except Exception as err:
            print("================= ERROR ==================")
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            # print("Error Code:", type(err.errno))
            # print("SQLSTATE", type(err.sqlstate))
            print("Message", err.msg)
            print("==========================================")

            if (err.errno == 1062) and (err.sqlstate == "23000"):
                tk.messagebox.showerror(title="Username Existed",message="Sorry. This name has already be registered.\n \
                Please try again!")
        finally:
            con.commit()

    def reg_check(self):
        # Use Regular Expression to check the format 
    
        if re.match(self.name_pattern.get(),self.username.get()) == None:
            tk.messagebox.showerror(title="Oops",message="Sorry. Please use your McMaster Email as your username.\n \
                Example: hello123@mcmaster.ca")
            return False
        else:
            pass

        if re.match(self.pswd_pattern.get(),self.password.get()) == None:
            tk.messagebox.showerror(title="Oops",message="Sorry. Please use the right format.\n \
                The password could only contain letters, numbers and '_' within 6 to 18 characters")
            return False
        else:
            pass

        if self.password.get() != self.con_password.get() :
            tk.messagebox.showerror(title="Oops",message="Sorry.Your password and confirmed password are not compatible!")
            return False
        else:
            pass
            
        return True


if __name__ == "__main__":
    root = tk.Tk()
    root.title('HMSD')
    RegisterPage(None)
    root.mainloop()

