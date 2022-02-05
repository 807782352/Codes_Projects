from tkinter import *
from tkinter.messagebox import *
from page.MainPage import *
 
class LoginPage(object):
    def __init__(self, master=None):
        self.root = master #定义内部变量root
        self.root.geometry('%dx%d' % (500, 300)) #设置窗口大小
        self.photo_path = "image\image01.png"
        self.username = StringVar(value="example@mcmaster.ca")
        self.password = StringVar()
        self.createPage()
 
    def createPage(self):
        self.page = Frame(self.root) #创建Frame
        self.page.pack()
        Label(self.page, text = 'Username: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username,show=None).grid(row=1, column=1, stick=E)
        Label(self.page, text = 'Password: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='Login', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='Exit', command=self.page.quit).grid(row=3, column=1, stick=E)
 
    def loginCheck(self):
        name = self.username.get()
        secret = self.password.get()
        if name=='111' and secret=='111':
            self.page.destroy()
            MainPage(self.root)
        else:
            showinfo(title='错误', message='账号或密码错误！')
