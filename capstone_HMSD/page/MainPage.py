# -*- coding: utf-8 -*-
# @Organization  : ${CAPSTONE PROJECT - GROUP 25}
# @Author        : Ziyi(Kyrie) Xu
# @Time          : ${Feb/03/2021}
# @Description   : UI Module for the HMSD project

import tkinter as tk
import mysql.connector
from PIL import Image, ImageTk
import page.Mode1Page as m1p
import page.Mode2Page as m2p
import serial



class MainPage(object):
    def __init__(self,name):
        print(name)
        self.name = name
        self.arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
        self.root = tk.Tk()
        self.height = 400
        self.width = 400
        self.resize = (100,100)
        self.root.geometry('%dx%d' % (self.width,self.height))
        self.root.title('Main Page')
        self.file_path = tk.StringVar(value="image\logo.jpg")
        self.createMainPage()

    def createMainPage(self):
        canvas = tk.Canvas(self.root,bg="white",width=self.width, height=self.height/4+10)
        canvas.pack()
        img = ImageTk.PhotoImage(Image.open(self.file_path.get()).resize(self.resize),master=canvas)
        canvas.create_image((self.width/2-self.resize[0]/2),5,anchor='nw',image=img)

        lastmode = self.lastMode(self.name)
        text = tk.Label(self.root,text=lastmode,font=14,pady=10)
        # text.grid(row=0,stick='NW',pady=10)
        text.pack()

        self.page = tk.Frame(self.root) # to create a Frame
        self.page.pack()    

        # Layout of Modes 
        mode1 = tk.Button(self.page,text="Mode 1\n\nSupporting Mode",height=8,width=16,font=20,command=self.go_mode1)
        mode1.grid(row=1,column=0,stick="E",pady=10,padx=8)
        mode2 = tk.Button(self.page,text="Mode 2\n\nTraining Mode",height=8,width=16,font=20,command=self.go_mode2)
        mode2.grid(row=1,column=1,stick="E",pady=10,padx=8)

        # # mouses suspend on the mode buttons
        # mode1.bind("<Enter>",self.on_mode1(mode1))
        # mode1.bind("<Leave>",self.on_leave1(mode1))

        self.root.mainloop()

    def lastMode(self,name):
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
            sql = "SELECT Mode FROM Users WHERE Username = %s"
            cursor.execute(sql,[name])
            mode = cursor.fetchone()
            print(mode[0])  # mode[0] for the first (or only) row

            if mode[0] == 0:
                msg = "Welcome, "+name+"\n\nChoose a Mode You Want"
            elif mode[0] == 1:
                msg = "Welcome Back "+ name +"!\n\nYour Last Mode:  Mode 1"
            elif mode[0] == 2:
                msg = "Welcome Back "+ name +"!\n\nYour Last Mode:  Mode 2"
            else:
                msg = "Something Wrong!"
            return msg

        except Exception as err:
            print("================= ERROR ==================")
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            # print("Error Code:", type(err.errno))
            # print("SQLSTATE", type(err.sqlstate))
            print("Message", err.msg)
            print("==========================================")
        finally:
            con.commit()

    def go_mode1(self):
        self.root.destroy()
        m1p.Mode1Page(self.name,self.arduino)
        
    def go_mode2(self):
        self.root.destroy()
        m2p.Mode2Page(self.name,self.arduino)
        
        
    # def on_mode1(self,mode):
    #     mode.config(text="HHHHHHH")

    # def on_leave1(self,mode):
    #     mode.configure(text="Mode 1")