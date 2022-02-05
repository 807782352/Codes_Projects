import tkinter as tk
from page.LoginPage import *
 
root = tk.Tk()     #  root是初始化窗口
root.title('HMSD')    # 第2步，给窗口的可视化起名字
LoginPage(root)
root.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
