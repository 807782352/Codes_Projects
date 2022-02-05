# -*- coding: utf-8 -*-
# @Organization  : ${CAPSTONE PROJECT - GROUP 25}
# @Author        : Ziyi(Kyrie) Xu
# @Time          : ${Feb/03/2021}
# @Description   : UI Module for the HMSD project

import tkinter as tk

from page.LoginPage import LoginPage

root = tk.Tk()
root.title('HMSD')
LoginPage(root)
root.mainloop()