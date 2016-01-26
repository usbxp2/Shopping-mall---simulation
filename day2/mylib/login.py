__author__ = 'huanghao'

import os
import print_color


path = os.getcwd()
parent_path = os.path.dirname(path)

def login(user_file,locked_file):
    #计数器
    n = 1
    #声明变量，配合计数器用
    username_temp = ''

    while n < 3:
        username = input("请输入用户名：")
        password = input("请输入密码：")
        #验证用户名或密码是否为空，为空则重新输入
        if username == '' or password == '':
            print_color.print_color('用户名或密码不能为空，请重新输入！','red')
            continue
        #验证用户是否被锁定
        with open(locked_file,'r') as f:
            for line in f.readlines():
                #print(line)
                if username == line.strip():
                    print_color.print_color("用户已被锁定，系统即将退出！",'red')
                    exit()

        #验证用户名密码是否正确
        with open(user_file,'r') as f:
            for line in f.readlines():
                if username == line.strip().split()[0] and password == line.strip().split()[1]:
                    print_color.print_color('欢迎登录oldboy商城！！祝您购物愉快！','green')
                    money = line.strip().split()[-1]
                    return username,money
            else:
                if username_temp == username:
                    n += 1
                    print_color.print_color('你已输错%s次，还有%s次机会！'% (n,3-n),'red')
                else:
                    username_temp = username
                    n = 1
                    print_color.print_color('用户名或密码错误，请重新输入！','red')
                    continue

    #验证连续三次失败的已存在的用户加入locked文件
    with open(user_file,'r') as f:
        for line in f.readlines():
            if username == line.strip().split()[0]:
                with open(locked_file,'a') as f1:
                    f1.write('%s\n' % username)
    print_color.print_color("尝试太多次，用户已被锁定，你已无法登录商城！系统即将退出",'red')
    return False,0
