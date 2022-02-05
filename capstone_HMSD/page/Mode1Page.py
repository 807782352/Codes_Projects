# -*- coding: utf-8 -*-
# @Organization  : ${CAPSTONE PROJECT - GROUP 25}
# @Author        : Ziyi(Kyrie) Xu
# @Time          : ${Feb/03/2021}
# @Description   : UI Module for the HMSD project

import tkinter as tk
import time
import page.MainPage as mp
import mysql.connector

from PIL import Image, ImageTk
from tkinter.messagebox import showerror,showinfo,showwarning

from page.comm import link


class Mode1Page(object):
    def __init__(self,name,arduino):
        # print(name)
        self.mode = 1
        self.name = name
        self.arduino = arduino
        (self.speedLevel, self.torqueLevel) = self.lastParameters(self.name)
        # print(self.speedLevel)
        # print(self.torqueLevel)
        self.root = tk.Tk()
        self.height = 400
        self.width = 400
        self.resize = (100,100)
        self.root.geometry('%dx%d' % (self.width,self.height))
        self.root.title('Mode 1 - Supporting Mode')
        self.file_path = tk.StringVar(value="image\logo.jpg")
        self.createMainPage()

    def createMainPage(self):
        canvas = tk.Canvas(self.root,bg="white",width=self.width, height=self.height/4+10)
        canvas.pack()
        img = ImageTk.PhotoImage(Image.open(self.file_path.get()).resize(self.resize),master=canvas)
        canvas.create_image((self.width/2-self.resize[0]/2),5,anchor='nw',image=img)

        text = tk.Label(self.root,text="You are in Mode 1 - Supporting Mode",font=14,pady=10)
        text.pack()

        # Two Scales
        s_speed = tk.Scale(self.root,label="Speed Level",from_=0,to=3,orient=tk.HORIZONTAL,
            length=200,showvalue=0,tickinterval=1,resolution=1)
        s_speed.set(self.speedLevel)
        s_speed.pack()
        # print(s_speed.get())

        s_torque = tk.Scale(self.root,label="Torque Level",from_=0,to=3,orient=tk.HORIZONTAL,
            length=200,showvalue=0,tickinterval=1,resolution=1)
        s_torque.set(self.torqueLevel)
        s_torque.pack()

        self.page = tk.Frame(self.root) # to create a Frame
        self.page.pack()    

        # Two buttons
        b_run = tk.Button(self.page,text="Run",command=lambda:self.run(s_speed,s_torque))
        b_run.grid(row=0,column=0,stick="W",pady=10,padx=50)
        b_back = tk.Button(self.page,text="Back",command=self.go_back)
        b_back.grid(row=0,column=1,stick="W",pady=10,padx=50)


        self.root.mainloop()

    def lastParameters(self,name):
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
            sql = "SELECT Mode,SpeedLevel,TorqueLevel FROM Users WHERE Username = %s"
            cursor.execute(sql,[name])
            parameters = cursor.fetchall()

            (speed,torque) = self.par_check(parameters)
            return (speed,torque)

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

    def par_check(self,parameters):
        mode = parameters[0][0]
        speed = parameters[0][1]
        torque = parameters[0][2]
        if (mode != 1):
            speed = 0
            torque = 0
        return (speed,torque)

    def run(self,speed,torque):
        """You can change codes here for running"""
        if ((speed.get() != 0 and torque.get() == 0) or (speed.get() == 0 and torque.get() != 0)):
            return showerror("ERROR","If you want to operate the device, please allow both levels not to be 0.\n ")


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
            # print(speed.get())
            # print(type(speed.get()))
            # print(self.name.get())
            # print(type(self.name))
            sql = "UPDATE Users SET Mode = %d, SpeedLevel = %d, TorqueLevel = %d WHERE Username = '%s'"
           
            val = (self.mode,speed.get(),torque.get(),self.name)
            print(sql % val)
            key = str(self.mode) + str(speed.get()) + str(torque.get())
            # print(key)

            link(self.arduino,key)
            # time.sleep(3)

            cursor.execute(sql % val)
            showinfo(title="Success!",message="Run Successfully")

        except Exception as err:
            print("================= ERROR ==================")
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
            print("==========================================")
        finally:
            con.commit()


    def go_back(self):
        self.root.destroy()
        mp.MainPage(self.name)


    # def on_mode1(self,mode):
    #     mode.config(text="HHHHHHH")

    # def on_leave1(self,mode):
    #     mode.configure(text="Mode 1")