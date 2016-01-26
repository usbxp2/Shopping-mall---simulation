__author__ = 'huanghao'

import os
import sys
path = os.getcwd()
my_path = os.path.join(path,'mylib')
sys.path.append(my_path)

from mylib.print_color import print_color
from mylib.login import login
from mylib.balance import balance
from mylib.icbc import icbc
from mylib.num_three import num_three
import mylib.buy




#登录后第一个菜单
def first_meun():
    print_color('''
          1   购物
          2   查询余额
          3   充值
          q   退出
    ''','yellow')

#返回功能菜单
def function_menu():
    print_color('''
          b   更多操作
          q   退出
    ''','yellow')

#充值成功后的菜单
def icbc_menu():
    print_color('''
          a   继续充值
          b   更多操作
          q   退出
    ''','yellow')

#用户信息文件和锁定信息文件
path = os.getcwd()
user_file = os.path.join(path,'user.txt')
locked_file = os.path.join(path,'locked.txt')

#打印欢迎信息
print_color('欢迎来到oldboy购物商城，请登录以使用更多功能！','green')
#用户登录
login_user,money = login(user_file,locked_file)

if login_user == False:
    exit()

while True:                          #用while循环，在做出查询，充值等操作后，用于返回主功能菜单
    #登录进入商城系统，显示第一个菜单
    first_meun()
    choice = input('请输入对应的编号：')

    if choice == 'q':
        print_color('感谢访问oldboy商城！欢迎下次光临，再见！','green')        #用户选择退出后的送别词，绿色显示
        exit()
    elif choice == '1':   #购物
        #购物程序开始=========================================
            mylib.buy.shopping(login_user,user_file)
        #购物程序结束==========================================
    elif choice == '2':    #查询余额
        balance(login_user,user_file)         #查询余额模块，根据余额大小 有不同颜色显示哦！
        while True:
            function_menu()      #查询完成后，显示功能菜单，退出或更多操作
            choice_s = input('请选择对应的操作：')
            if choice_s == 'q':
                print_color('感谢访问oldboy商城！欢迎下次光临，再见！','green')
                exit()
            elif choice_s == 'b':
                break
            else:
                print_color('您的选择不正确，请重新输入：','red')     #输入不正确时的提示，红色显示
                continue   #继续下一次循环，即重新选择
    elif choice == '3':
        flag = True
        while flag:
            in_money = input('请输入要充值的金额,您只能充值整数金额：')
            if in_money.isdigit():#判断输入是否是正整数数字
                money = balance(login_user,user_file)
                total_money = money + int(in_money)
                result = icbc(login_user,user_file,str(total_money))
                if result:
                    print_color('充值成功！！本次充值金额：%s' % in_money,'green')
                    balance(login_user,user_file)

                    while True:
                        icbc_menu()      #充值完成后的菜单，继续充值，更多操作或退出
                        choice_icbc = input('请选择对应的操作：')
                        if choice_icbc == 'a':  #继续充值
                            break
                        elif choice_icbc == 'b':  #更多操作，进入系统主菜单
                            flag = False
                            break
                        elif choice_icbc == 'q':  #退出
                            print_color('感谢访问oldboy商城！欢迎下次光临，再见！','green')
                            exit()
                        else:
                            print_color('您的输入有误，请重新输入','red')
                            continue
                    continue
                else:
                    print_color('充值失败，系统将返回主菜单！','red')
                break
            else:               #输入不是正整数数字，重新输入
                print_color('您只能充值正整数金额，请重新输入：','red')
                continue




    else:
        #输入不正确时的提示，红色显示，到这程序就结束了，自动进入一次循环，实现重新输入
        print_color('您的选择不正确，请重新输入：','red')
