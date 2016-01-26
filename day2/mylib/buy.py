__author__ = 'huanghao'


__author__ = 'huanghao'

import print_color
import balance
import icbc

#商品
product = {'iphone':5000,
           '小米手机':799,
           '老男孩python培训':0,
           '上班族飞行神器':1000000,
           '山寨笔记本电脑':2500}

#打印商品列表
def show_product_list():
    '''
    :return: 打印商品列表，返回值为编号和商品名称对应的字典
    '''
    i = 1
    k_dic = {}
    print('商品价目表'.center(50,'*'))
    print('%-6s%-30s%-15s' % ('编号','商品名称','价格'))
    for k,v in product.items():
        print('%-8s%-30s%-15s' % (i,k,v))
        k_dic[i] = k
        i += 1
    print('*'*55)
    return k_dic



#显示购物车商品，帐户余额，总价格
def show_shopping_car_list(username,user_file,shopping_car_list):
    '''
    :param username:
    :param user_file:
    :return: 返回值为商品总价格 和 帐户余额。都为正整数.返回 False，说明购物车为空
    '''
    if len(shopping_car_list) == 0:
        print_color.print_color("购物车为空，赶紧购物吧！！",'green')
        return False
    else:
        total_price = 0
        car_dic = {}
        print('*'*51)
        print('%-6s%-30s%-15s' % ('编号','商品名称','价格'))
        for i,v in enumerate(shopping_car_list):
            #print('*'*51)
            print('%-8s%-30s%-15s' % (i,v,str(product[v])))
            total_price += product[v]
            car_dic[i] = v
        print('*'*51)
        money_ye = balance.balance(username,user_file)
        return car_dic

#购物车功能菜单
def shopping_car_fun_menu():
    #if money_ye < total_price:
    #    print_color.print_color("1  '充值'       e  '编辑购物车'     q  '退出系统'", 'yellow' )
    #else:
        print_color.print_color("p  '结算'  a  '充值'   e  '编辑购物车'    x  '继续购物'", 'yellow' )

#编辑购物车
def edit_car(shopping_car_list,product_name):
    shopping_car_list.remove(product_name)
    return shopping_car_list

#添加到购物车
def add_car(shopping_car_list,product_name):
    shopping_car_list.append(product_name)
    return shopping_car_list

#结算购物车
def pay(username,user_file,shopping_car_list):
    '''
    :param username:
    :param user_file:
    :param shopping_car_list:
    :return:返回值为结算后的帐户余额
    '''
    price = 0
    for i in shopping_car_list:
        price += product[i]

    money_ye = balance.balance(username,user_file)
    if price > money_ye:
        print_color.print_color('余额不足，结算失败,请充值后再结算！','red')
        return False
    else:
        money_ye = money_ye - price
    return money_ye


#购物主程序
def shopping(login_user,user_file):
    shopping_car_list = []
    flag1 = True
    flag2 = True
    while flag1:
        product_list_dic = show_product_list()
        print_color.print_color('b  返回主菜单','yellow')
        choice_product = input("请输入您想购买的商品编号：")
        if choice_product == 'b':
            break
        elif choice_product.isdigit():
            if int(choice_product) in product_list_dic:
                add_car(shopping_car_list,product_list_dic[int(choice_product)])
                while flag2:
                    print_color.print_color('当前购物车商品','green')
                    car_dic = show_shopping_car_list(login_user,user_file,shopping_car_list) #购物车商品名称及编号
                    shopping_car_fun_menu()
                    choice_fu = input('请输入您想要的操作编号：')
                    if choice_fu == 'e':
                        while True:
                            choice_del = input('请输入您想要删除的商品编号：')
                            if int(choice_del) in car_dic:
                                shopping_car_list.remove(car_dic[int(choice_del)])
                                print_color.print_color('删除成功！','green')
                                break
                            else:
                                print_color.print_color('您输入的不正确，请重新输入！','red')
                                continue
                    elif choice_fu == 'x':
                        break
                    elif choice_fu == 'a':
                        while True:
                            money_cz = input('请输入你想要充值的金额，只能充入正整数金额：')
                            if money_cz.isdigit():
                                money_ye = balance.balance(login_user,user_file)
                                money_ye = money_ye + int(money_cz)
                                result = icbc.icbc(login_user,user_file,money_ye)
                                if result == True:
                                    print_color.print_color('充值成功！！本次充值金额：%s' % money_cz,'green')
                                    balance.balance(login_user,user_file)
                                    break
                                else:
                                    print_color('充值失败，系统将返回购物车列表！','red')
                                    break
                            else:
                                print_color.print_color('你输入的金额不正确，请重新输入！','red')
                                continue
                    elif choice_fu == 'p':
                        money = pay(login_user,user_file,shopping_car_list)
                        if money == False:
                            continue
                        else:
                            result = icbc.icbc(login_user,user_file,str(money))
                            if result == True:
                                print_color.print_color('结算成功，东西就不给你了，哈哈哈！','green')
                                balance.balance(login_user,user_file)
                                shopping_car_list = []
                                while True:
                                    print_color.print_color('b  回到主菜单  q 退出系统','yellow')
                                    choice_last = input("请选择对应的操作编号：")
                                    if choice_last == 'q':
                                        print_color.print_color('感谢访问oldboy商城！欢迎下次光临，再见！','green')
                                        exit()
                                    elif choice_last == 'b':
                                        flag2 = False
                                        flag1 = False
                                        break
                                    else:
                                        print_color.print_color('您输入的不正确，请重新输入！')
                                        continue

                            else:
                                print_color.print_color('结算失败，返回购物车列表')
                                continue

                    else:
                        print_color.print_color('您的输入不正确，请重新输入！', 'red')
            else:
                print_color.print_color('您输入的不正确，请重新输入','red')
                continue
        else:
            print_color.print_color('您输入的不正确，请重新输入','red')

