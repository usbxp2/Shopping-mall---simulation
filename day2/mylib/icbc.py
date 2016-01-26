__author__ = 'huanghao'

import print_color
import num_three

def icbc(username,user_file,money):
    '''money是充值后的总额，user_file是user.txt的路径，
        username是充值用户，采用先读取user_file的内容到内存，
        然后进行修改，之后w写入到user_file。money是字符串'''
    try:
        with open(user_file,'r')as f:
            new_list = []
            for line in f.readlines():
                username_list = line.strip().split()
                if username_list[0] == username:
                    username_list[-1] = '%s\n' % money
                    username_str = ' '.join(i for i in username_list)
                    new_list.append(username_str)
                else:
                    new_list.append(line)
        with open(user_file,'w') as f:
            for line in new_list:
                f.write(line)
        return True
    except:
        return False
