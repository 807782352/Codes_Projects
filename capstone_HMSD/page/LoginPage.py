# -*- coding: utf-8 -*-
# @Organization  : ${CAPSTONE PROJECT - GROUP 25}
# @Author        : Ziyi(Kyrie) Xu
# @Time          : ${Feb/03/2021}
# @Description   : UI Module for the HMSD project

import tkinter as tk
import mysql.connector
from PIL import Image, ImageTk
import page.RegisterPage as rp
import page.MainPage as mp

class LoginPage(object):
    def __init__(self,master=None):
        self.root = master
        self.height = 300
        self.width = 300
        self.resize = (140,140)
        self.root.geometry('%dx%d' % (self.width,self.height))
        # self.fig_size = [300,50]
        self.username = tk.StringVar(value="example@mcmaster.ca")
        self.password = tk.StringVar()
        self.file_path = tk.StringVar(value="image\logo.jpg")
        self.createLogin()
    
    def createLogin(self):
        canvas = tk.Canvas(self.root,bg="white",width=self.width, height=self.height/2)
        canvas.pack()
        img = ImageTk.PhotoImage(Image.open(self.file_path.get()).resize(self.resize),master=canvas)
        canvas.create_image((self.width/2-self.resize[0]/2),5,anchor='nw',image=img)
        self.page = tk.Frame(self.root) # to create a Frame
        self.page.pack()    

        # Layout of Username and Password
        l_name = tk.Label(self.page, text='Username: ')
        l_name.grid(row=1,stick='W',pady=10)
        e_name = tk.Entry(self.page, textvariable=self.username,show=None)
        e_name.grid(row=1,column=1,stick='E',pady=10)
        l_pswd = tk.Label(self.page, text='Password: ')
        l_pswd.grid(row=2,stick='W',pady=10)
        e_pswd = tk.Entry(self.page, textvariable=self.password,show='*')
        e_pswd.grid(row=2,column=1,stick='E',pady=10)

        # Layout of buttons 
        b_login = tk.Button(self.page,text="Login",command=self.loginCheck)
        b_login.grid(row=3,stick="W",pady=10)
        b_register = tk.Button(self.page,text="Sign Up",command=self.go_signup)
        b_register.grid(row=3,column=1,stick="W",pady=10,padx=15)
        b_exit = tk.Button(self.page,text="Exit",command=self.root.destroy)
        b_exit.grid(row=3,column=1,stick="E",pady=10)

        self.root.mainloop()

    def go_signup(self):
        self.root.destroy()
        rp.RegisterPage(self.root)

    def loginCheck(self):
        name = self.username.get()
        pswd = str(self.password.get())

        config={
            "host":"localhost",
            "port":3306,
            "user":"root",
            "password":"123456",
            "database":"HMSD"
        }
        # key = "HMSD"
        try:
            pool = mysql.connector.pooling.MySQLConnectionPool(
                **config,
                pool_size=10
            )
            con = pool.get_connection()
            con.start_transaction()
            cursor=con.cursor()
            # needs to make restriction！
            # Note: 64 characters for the "local part" (username).
                    # 1 character for the @ symbol.
                    # 255 characters for the domain name.
            sql="CREATE TABLE IF NOT EXISTS Users (Username VARCHAR(400) NOT NULL UNIQUE, \
                Password Char(20) NOT NULL, Mode int, SpeedLevel int, \
                TorqueLevel int)"
            cursor.execute(sql)
            
            # Below: make sure the strings have " " 
            # also add encryed and deencryed
            sql="SELECT Username, AES_DECRYPT(UNHEX(Password),\"HMSD\") FROM Users WHERE Username = %s"
            # print(sql)
            cursor.execute(sql,[name])
            
            temp=cursor.fetchall()
            name_sql = temp[0][0]   # first [0]: row 0; second [0]: column 0
            pswd_sql = str(temp[0][1])
            # print(pswd_sql)
            # print(pswd)
            # print(pswd is pswd_sql)
            if name_sql == name and pswd_sql == str(pswd):
                tk.messagebox.showinfo(title="Welcome",message="Congratulations! ")
                self.root.destroy()
                mp.MainPage(name)
            else:
                tk.messagebox.showerror(title="Error",message="Wrong Password!\nPlease try again")
            
        except IndexError as i_err:
            tk.messagebox.showerror(title="Error",message="The username has not be registered!\nPlease sign up first!")
        
        # except Exception as err:
        #     print("================= ERROR ==================")
        #     print(err)
        #     print("Error Code:", err.errno)
        #     print("SQLSTATE", err.sqlstate)
        #     # print("Error Code:", type(err.errno))
        #     # print("SQLSTATE", type(err.sqlstate))
        #     print("Message", err.msg)
        #     print("==========================================")
        finally:
            con.commit()
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title('HMSD')
    LoginPage(root)
    root.mainloop()

    # from tkinter import *  
    # from PIL import ImageTk,Image  
    # root = Tk()  
    # canvas = Canvas(root, width = 300, height = 300)  
    # canvas.pack()  
    # img = ImageTk.PhotoImage(Image.open("image\image01.png"))  
    # canvas.create_image(20, 20, anchor=NW, image=img) 
    # root.mainloop() 