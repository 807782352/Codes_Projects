from colorama import Fore, Style
from app.app import ChineseVersion
from app.app_english import EnglishVersion

import os
import time

chinese_version = ChineseVersion()
english_version = EnglishVersion()

while True:
    os.system("cls")
    print(Fore.LIGHTBLUE_EX, "\n\t==============")
    print(Fore.LIGHTBLUE_EX, "\n\t欢迎使用新闻管理系统")
    print(Fore.LIGHTBLUE_EX, "\n\tWelcome to use News Management System")
    print(Fore.LIGHTBLUE_EX, "\n\t==============")
    print(Fore.LIGHTYELLOW_EX, "\n\t1.中文版本")
    print(Fore.LIGHTYELLOW_EX, "\n\t2.English Version")
    print("\n")
    print(Style.RESET_ALL)
    opt = input("\n\t输入操作编号(Choose the number)：")  # 保存的是字符串类型
    if opt == "1":
        chinese_version.main_app()
    elif opt == "2":
        english_version.main_app()
    else:
        print(Fore.LIGHTRED_EX,"\n\t请输入正确值(Please put correct number)")
        time.sleep(3)