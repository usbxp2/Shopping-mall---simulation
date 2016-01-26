__author__ = 'huanghao'

import print_color
import num_three

def balance(username,user_file):
    '''
    :param username:
    :param user_file:
    :return:返回值为正整数
    '''
    with open(user_file,'r') as f:
        for line in f.readlines():
            if line.strip().split()[0] == username:
                money = line.strip().split()[-1]
                money = int(money)
                if money <1000:
                    print('当前用户：',end='')
                    print_color.print_color('%s' % username, 'green'),
                    print('帐户余额：',end=''),
                    print_color.print_color('%s' % num_three.num_three(str(money)),'red')
                if money >=1000 and money <= 2500:
                    print('当前用户：',end=''),
                    print_color.print_color('%s' % username, 'green'),
                    print('帐户余额：',end=''),
                    print_color.print_color('%s' % num_three.num_three(str(money)),'yellow')
                if money > 2500:
                    print('当前用户：',end=''),
                    print_color.print_color('%s' % username, 'green'),
                    print('帐户余额：',end=''),
                    print_color.print_color('%s' % num_three.num_three(str(money)),'green')
                return money