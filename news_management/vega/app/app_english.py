from colorama import Fore, Style
from getpass import getpass
# getpass和input的功能是类型的，但是getpass输出的字符是加密的，看不到输入的情况。
# pycharm是无法使用该方法的，只能在终端。
from service_english.user_service import UserService
from service_english.news_service import NewsService
from service_english.role_service import RoleService
# from app import ChineseVersion
import os
import sys
import time


class EnglishVersion:
    def main_app(self):
        __user_service = UserService()
        __news_service = NewsService()
        __role_service = RoleService()
        # chinese_version = ChineseVersion()

        while True:
            os.system("cls")
            print(Fore.LIGHTBLUE_EX, "\n\t==================================")
            print(Fore.LIGHTBLUE_EX, "\n\tWelcome to use News Management System")
            print(Fore.LIGHTBLUE_EX, "\n\t==================================")
            print(Fore.LIGHTGREEN_EX, "\n\t1.Login the system")
            print(Fore.LIGHTRED_EX, "\n\t2.Exit the system")
            # print(Fore.LIGHTYELLOW_EX, "\n\t3.中文版本")
            print(Style.RESET_ALL)
            opt = input("\n\tCommand here for operation：")  # 保存的是字符串类型
            if opt == "1":
                username = input("\n\tUsername：")
                password = getpass("\n\tPassword：")
                result = __user_service.login(username, password)
                # 登录成功
                if result == True:
                    role = __user_service.search(username)
                    os.system("cls")
                    while True:
                        os.system("cls")
                        if role == "News Editor":
                            print("\n\tThis module is developing. Sorry...(back in 3 seconds)")  # 先放着 以后再来编辑
                            time.sleep(3)
                            break
                        elif role == "Administrator":
                            print(Fore.LIGHTGREEN_EX, "\n\t1.News Management")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.Users Management")
                            print(Fore.LIGHTRED_EX, "\n\tback.Log out the system")
                            print(Fore.LIGHTRED_EX, "\n\texit.Exit the system")
                            print(Style.RESET_ALL)
                            opt = input("\n\tCommand here for operation：")  # 保存的是字符串类型
                            if opt == '1':
                                # 新闻管理
                                while True:
                                    os.system("cls")
                                    print(Fore.LIGHTGREEN_EX, "\n\t1.Vet News")
                                    print(Fore.LIGHTGREEN_EX, "\n\t2.Delete News")
                                    print(Fore.LIGHTRED_EX, "\n\tback.Back to previous level")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\tCommand here for operation：")  # 保存的是字符串类型
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
                                            print(Fore.LIGHTRED_EX, "\n\tback.back to previous level")
                                            if page == 1:
                                                print(Fore.LIGHTRED_EX, "\n\tnext.next page")
                                                print(Style.RESET_ALL)
                                            elif page == count_page:
                                                print(Fore.LIGHTRED_EX, "\n\tprev.last page")
                                                print(Style.RESET_ALL)
                                            else:
                                                print(Fore.LIGHTRED_EX, "\n\tprev.last page")
                                                print(Fore.LIGHTRED_EX, "\n\tnext.next page")
                                                print(Style.RESET_ALL)
                                            opt = input("\n\tCommand here for operation：")  # 保存的是字符串类型
                                            if opt.lower == "back":
                                                break
                                            elif str(opt).lower == "prev" and page > 1:
                                                page -= 1
                                            elif opt.lower == "next" and page < count_page:
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
                                            print(Fore.LIGHTRED_EX, "\n\tback.Back to previous level")
                                            if page == 1:
                                                print(Fore.LIGHTRED_EX, "\n\tnext.Next page")
                                                print(Style.RESET_ALL)
                                            elif page == count_page:
                                                print(Fore.LIGHTRED_EX, "\n\tprev.Last page")
                                                print(Style.RESET_ALL)
                                            else:
                                                print(Fore.LIGHTRED_EX, "\n\tprev.Last page")
                                                print(Fore.LIGHTRED_EX, "\n\tnext.Next page")
                                                print(Style.RESET_ALL)
                                            opt = input("\n\tCommand here for operation：")  # 保存的是字符串类型
                                            if opt.lower() == "back":
                                                break
                                            elif opt.lower() == "prev" and page > 1:
                                                page -= 1
                                            elif opt.lower() == "next" and page < count_page:
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
                                    print(Fore.LIGHTGREEN_EX, "\n\t1.Add users")
                                    print(Fore.LIGHTGREEN_EX, "\n\t2.Edit users")
                                    print(Fore.LIGHTGREEN_EX, "\n\t3.Delete users")
                                    print(Fore.LIGHTRED_EX, "\n\tback.Back to previous level")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\tCommand here for operation：")  # 保存的是字符串类型
                                    if opt == "back":
                                        break
                                    elif opt == "1":
                                        os.system("cls")
                                        username = input("\n\tUsername：")
                                        password = getpass("\n\tPassword：")
                                        repassword = getpass("\n\tRepeat the password：")
                                        if password != repassword:
                                            print("\n\tTwo passwords are not paired（back in 3 seconds automatically）")
                                            time.sleep(3)
                                            continue
                                        email = input("\n\tEmail：")
                                        result = __role_service.search_role_list()
                                        # 查询数据库已有角色
                                        print(Fore.LIGHTBLUE_EX, "\n\tRole：")
                                        for index in range(len(result)):
                                            one = result[index]
                                            print(Fore.LIGHTBLUE_EX, "\n\t{0}.{1}".format(index + 1, one[1]))
                                        print(Style.RESET_ALL)
                                        opt = input("\n\tInsert the role's number：")
                                        role_id = result[int(opt) - 1][0]
                                        __user_service.insert(username, password, email, role_id)
                                        print("\n\tSaved Successfully!（back in 3 seconds automatically）")
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
                                            print(Fore.LIGHTRED_EX, "\n\tback.Back to previous level")
                                            if page == 1:
                                                print(Fore.LIGHTRED_EX, "\n\tnext.Next page")
                                                print(Style.RESET_ALL)
                                            elif page == count_page:
                                                print(Fore.LIGHTRED_EX, "\n\tprev.Last page")
                                                print(Style.RESET_ALL)
                                            else:
                                                print(Fore.LIGHTRED_EX, "\n\tprev.Last page")
                                                print(Fore.LIGHTRED_EX, "\n\tnext.Next page")
                                                print(Style.RESET_ALL)
                                            opt = input("\n\tCommand here for operation：")  # 保存的是字符串类型
                                            if opt == "back":
                                                break
                                            elif opt == "prev" and page > 1:
                                                page -= 1
                                            elif opt == "next" and page < count_page:
                                                page += 1
                                            elif 1 <= int(opt) <= 10:
                                                os.system("cls")
                                                user_id = result[int(opt) - 1][0]
                                                username = input("\n\tNew Username：")
                                                password = getpass("\n\tPassword：")
                                                repassword = getpass("\n\tRetype the password：")
                                                if repassword != password:
                                                    print(
                                                        "\n\tTwo passwords are not paired (back in 3 seconds automatically)")
                                                    time.sleep(3)
                                                email = input("\n\tEmail：")
                                                result = __role_service.search_role_list()
                                                for index in range(len(result)):
                                                    one = result[index]
                                                    print(Fore.LIGHTBLUE_EX, "\n\t{0}.{1}".format(index + 1, one[1]))
                                                print(Style.RESET_ALL)
                                                opt = input("\n\tInsert number for role：")
                                                role_id = result[int(opt) - 1][0]
                                                opt = input("\n\tContinue to save？（Y/N）")
                                                if opt == "Y" or opt == "y":
                                                    __user_service.update(user_id, username, password, email, role_id)
                                                    print("\n\tSuccessfully Saved!! (back in 3 seconds automatically)")
                                                    time.sleep(3)
                                                else:
                                                    print(
                                                        "\n\tSorry,something wrong in save. (back in 3 seconds automatically")
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
                                            print(Fore.LIGHTRED_EX, "\n\tback.Back to previous level")
                                            if page == 1:
                                                print(Fore.LIGHTRED_EX, "\n\tnext.next page")
                                                print(Style.RESET_ALL)
                                            elif page == count_page:
                                                print(Fore.LIGHTRED_EX, "\n\tprev.last page")
                                                print(Style.RESET_ALL)
                                            else:
                                                print(Fore.LIGHTRED_EX, "\n\tprev.last page")
                                                print(Fore.LIGHTRED_EX, "\n\tnext.next page")
                                                print(Style.RESET_ALL)
                                            opt = input("\n\tCommand here for operation：")  # 保存的是字符串类型
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
                                                print("\n\tDelete Successfully!!(back in 3 seconds automatically)")
                                                time.sleep(3)

                            elif opt == "back":
                                break
                            elif opt == "exit":
                                os.system("cls")
                                print(Fore.LIGHTRED_EX, "\n\tYou have successfully logged out!" \
                                                        " Take care and welcome to use again!")
                                sys.exit(0)
                # elif opt == "3":
                #     chinese_version.main_app()
                else:
                    print("\n\tLogin unsuccessfully (back in 3 seconds)")
                    time.sleep(3)
            elif opt == "2":
                sys.exit(0)  # 0代表安全退出
