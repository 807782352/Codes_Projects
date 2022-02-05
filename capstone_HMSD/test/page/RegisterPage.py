from tkinter import *
 
 
class RegisterPage(object):
 
    def bf_goLogin(self):
        self.goLogin()
 
    def __init__(self, goLogin):
        self.goLogin = goLogin
 
        self.root = Tk()
 
        Label(self.root, text="用户").grid(row=0, column=0)
        Entry(self.root).grid(row=0, column=1, columnspan=2)
        Label(self.root, text="密码").grid(row=1, column=0)
        Entry(self.root, show="*").grid(row=1, column=1, columnspan=2)
        Label(self.root, text="确认").grid(row=2, column=0)
        Entry(self.root, show="*").grid(row=2, column=1, columnspan=2)
        Button(self.root, text="注册").grid(row=3, column=1)
        Button(self.root, text="返回", command=self.bf_goLogin).grid(row=3, column=2, )
 
        self.root.mainloop()
 
 
if __name__ == '__main__':
    root = Tk()
    RegisterPage(None)
