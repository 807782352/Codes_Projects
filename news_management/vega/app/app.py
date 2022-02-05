from colorama import Fore, Style
from getpass import getpass
# getpass和input的功能是类型的，但是getpass输出的字符是加密的，看不到输入的情况。
# pycharm是无法使用该方法的，只能在终端。
from service.user_service import UserService
from service.news_service import NewsService
from service.role_service import RoleService
# from app_english import EnglishVersion
import os
import sys
import time


class ChineseVersion:

    def main_app(self):
        __user_service = UserService()
        __news_service = NewsService()
        __role_service = RoleService()
        # english_version = EnglishVersion()

        while True:
            os.system("cls")
            print(Fore.LIGHTBLUE_EX, "\n\t==============")
            print(Fore.LIGHTBLUE_EX, "\n\t欢迎使用新闻管理系统")
            print(Fore.LIGHTBLUE_EX, "\n\t==============")
            print(Fore.LIGHTGREEN_EX, "\n\t1、登录系统")
            print(Fore.LIGHTRED_EX, "\n\t2、退出系统")
            # print(Fore.LIGHTYELLOW_EX, "\n\t3、English Version")
            print(Style.RESET_ALL)
            opt = input("\n\t输入操作编号：")  # 保存的是字符串类型
            if opt == "1":
                username = input("\n\t用户名：")
                password = getpass("\n\t密码：")
                result = __user_service.login(username, password)
                # 登录成功
                if result == True:
                    role = __user_service.search(username)
                    os.system("cls")
                    while True:
                        os.system("cls")
                        if role == "新闻编辑":
                            print("新闻编辑模块正在开发中...(3秒后自动返回)")  # 先放着 以后再来编辑
                            time.sleep(3)
                            break
                        elif role == "管理员":
                            print(Fore.LIGHTGREEN_EX, "\n\t1.新闻管理")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.用户管理")
                            print(Fore.LIGHTRED_EX, "\n\tback.退出登录")
                            print(Fore.LIGHTRED_EX, "\n\texit.退出系统")
                            print(Style.RESET_ALL)
                            opt = input("\n\t输入操作编号：")  # 保存的是字符串类型
                            if opt == '1':
                                # 新闻管理
                                while True:
                                    os.system("cls")
                                    print(Fore.LIGHTGREEN_EX, "\n\t1.审批新闻")
                                    print(Fore.LIGHTGREEN_EX, "\n\t2.删除新闻")
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t输入操作编号：")  # 保存的是字符串类型
                                    if opt == "1":
                                        page = 1  # 默认初始page为1
                                        while True:
                                            os.system("cls")
                                            count_page = __news_service.search_unreview_count_page()
                                            result = __news_service.search_unreview_list(page)
                                            for index in range(len(result)):
                                                one = result[index]
                                                print(Fore.LIGHTBLUE_EX,
                                                      "\n\t%d\t%s\t%s\t%s" % (index + 1, one[1], one[2], one[3]))
                                            print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                            print(Fore.LIGHTBLUE_EX, "\n\t{0}/{1}".format(page, count_page))
                                            print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一级")
                                            if page == 1:
                                                print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                                print(Style.RESET_ALL)
                                            elif page == count_page:
                                                print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                                print(Style.RESET_ALL)
                                            else:
                                                print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                                print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                                print(Style.RESET_ALL)
                                            opt = input("\n\t输入操作编号：")  # 保存的是字符串类型
                                            if opt == "back":
                                                break
                                            elif opt == "prev" and page > 1:
                                                page -= 1
                                            elif opt == "next" and page < count_page:
                                                page += 1
                                            elif 1 <= int(opt) <= 10:
                                                news_id = result[int(opt) - 1][0]  # 得到选取元素的ID
                                                __news_service.update_unreview_news(news_id)
                                    elif opt == "2":
                                        page = 1  # 默认初始page为1
                                        while True:
                                            os.system("cls")
                                            count_page = __news_service.search_count_page()
                                            result = __news_service.search_list(page)
                                            for index in range(len(result)):
                                                one = result[index]
                                                print(Fore.LIGHTBLUE_EX,
                                                      "\n\t%d\t%s\t%s\t%s" % (index + 1, one[1], one[2], one[3]))
                                            print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                            print(Fore.LIGHTBLUE_EX, "\n\t{0}/{1}".format(page, count_page))
                                            print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一级")
                                            if page == 1:
                                                print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                                print(Style.RESET_ALL)
                                            elif page == count_page:
                                                print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                                print(Style.RESET_ALL)
                                            else:
                                                print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                                print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                                print(Style.RESET_ALL)
                                            opt = input("\n\t输入操作编号：")  # 保存的是字符串类型
                                            if opt == "back":
                                                break
                                            elif opt == "prev" and page > 1:
                                                page -= 1
                                            elif opt == "next" and page < count_page:
                                                page += 1
                                            elif 1 <= int(opt) <= 10:
                                                news_id = result[int(opt) - 1][0]  # 得到选取元素的ID
                                                __news_service.delete_by_id(news_id)
                                    elif opt == "back":
                                        break
                            elif opt == "2":
                                # 用户管理
                                while True:
                                    os.system("cls")
                                    print(Fore.LIGHTGREEN_EX, "\n\t1.添加用户")
                                    print(Fore.LIGHTGREEN_EX, "\n\t2.编辑用户")
                                    print(Fore.LIGHTGREEN_EX, "\n\t3.删除用户")
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t输入操作编号：")  # 保存的是字符串类型
                                    if opt == "back":
                                        break
                                    elif opt == "1":
                                        os.system("cls")
                                        username = input("\n\t用户名：")
                                        password = getpass("\n\t密码：")
                                        repassword = getpass("\n\t再次输入密码：")
                                        if password != repassword:
                                            print("\n\t密码前后不一致（3秒后自动返回）")
                                            time.sleep(3)
                                            continue
                                        email = input("\n\t邮箱：")
                                        result = __role_service.search_role_list()
                                        # 查询数据库已有角色
                                        print(Fore.LIGHTBLUE_EX, "\n\t角色编号：")
                                        for index in range(len(result)):
                                            one = result[index]
                                            print(Fore.LIGHTBLUE_EX, "\n\t{0}.{1}".format(index + 1, one[1]))
                                        print(Style.RESET_ALL)
                                        opt = input("\n\t输入角色编号：")
                                        role_id = result[int(opt) - 1][0]
                                        __user_service.insert(username, password, email, role_id)
                                        print("\n\t保存成功（3秒后自动返回）")
                                        time.sleep(3)
                                        continue
                                    elif opt == "2":
                                        page = 1
                                        while True:
                                            os.system("cls")
                                            count_page = __user_service.search_count_page()
                                            result = __user_service.search_list(page)
                                            for index in range(len(result)):
                                                one = result[index]
                                                print(Fore.LIGHTBLUE_EX,
                                                      "\n\t%d\t%s\t%s" % (index + 1, one[1], one[2]))
                                            print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                            print(Fore.LIGHTBLUE_EX, "\n\t{0}/{1}".format(page, count_page))
                                            print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一级")
                                            if page == 1:
                                                print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                                print(Style.RESET_ALL)
                                            elif page == count_page:
                                                print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                                print(Style.RESET_ALL)
                                            else:
                                                print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                                print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                                print(Style.RESET_ALL)
                                            opt = input("\n\t输入操作编号：")  # 保存的是字符串类型
                                            if opt == "back":
                                                break
                                            elif opt == "prev" and page > 1:
                                                page -= 1
                                            elif opt == "next" and page < count_page:
                                                page += 1
                                            elif 1 <= int(opt) <= 10:
                                                os.system("cls")
                                                user_id = result[int(opt) - 1][0]
                                                username = input("\n\t新用户名：")
                                                password = getpass("\n\t密码：")
                                                repassword = getpass("\n\t再次密码：")
                                                if repassword != password:
                                                    print("\n\t两次密码不符(3秒后自动返回)")
                                                    time.sleep(3)
                                                email = input("\n\t邮箱：")
                                                result = __role_service.search_role_list()
                                                for index in range(len(result)):
                                                    one = result[index]
                                                    print(Fore.LIGHTBLUE_EX, "\n\t{0}.{1}".format(index + 1, one[1]))
                                                print(Style.RESET_ALL)
                                                opt = input("\n\t输入角色编号：")
                                                role_id = result[int(opt) - 1][0]
                                                opt = input("\n\t是否保存？（Y/N）")
                                                if opt == "Y" or opt == "y":
                                                    __user_service.update(user_id, username, password, email, role_id)
                                                    print("\n\t保存成功(3秒后自动返回)")
                                                    time.sleep(3)
                                    elif opt == "3":
                                        page = 1
                                        while True:
                                            os.system("cls")
                                            count_page = __user_service.search_count_page()
                                            result = __user_service.search_list(page)
                                            for index in range(len(result)):
                                                one = result[index]
                                                print(Fore.LIGHTBLUE_EX,
                                                      "\n\t%d\t%s\t%s" % (index + 1, one[1], one[2]))
                                            print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                            print(Fore.LIGHTBLUE_EX, "\n\t{0}/{1}".format(page, count_page))
                                            print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一级")
                                            if page == 1:
                                                print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                                print(Style.RESET_ALL)
                                            elif page == count_page:
                                                print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                                print(Style.RESET_ALL)
                                            else:
                                                print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                                print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                                print(Style.RESET_ALL)
                                            opt = input("\n\t输入操作编号：")  # 保存的是字符串类型
                                            if opt == "back":
                                                break
                                            elif opt == "prev" and page > 1:
                                                page -= 1
                                            elif opt == "next" and page < count_page:
                                                page += 1
                                            elif 1 <= int(opt) <= 10:
                                                os.system("cls")
                                                user_id = result[int(opt) - 1][0]
                                                __user_service.delete_by_id(user_id)
                                                print("\n\t删除成功(3秒后自动返回)")
                                                time.sleep(3)

                            elif opt == "back":
                                break
                            elif opt == "exit":
                                os.system("cls")
                                print(Fore.LIGHTRED_EX, "\n\t您已成功退出，欢迎下次使用")
                                sys.exit(0)
                # elif opt == "3":
                #     english_version.main_app()

                else:
                    print("\n\t登录失败(3秒自动返回)")
                    time.sleep(3)
            elif opt == "2":
                sys.exit(0)  # 0代表安全退出
