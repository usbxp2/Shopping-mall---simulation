__author__ = 'huanghao'

def num_three(num):

    num_left_ys = len(num)%3

    if num_left_ys == 0:
       return ','.join(num[i:i+3] for i in range(0,len(num),3))

    else:
        # TODO
        num_left = num[:num_left_ys]
        num_right_ys = len(num)/3
        num_right_num = num[num_left_ys:]
        num_right = ','.join(num_right_num[i:i+3] for i in range(0,len(num_right_num),3))
        #print(num_left + ','+ num_right)
        return '\033[0;32;1m %s,%s \033[0m' % (num_left,num_right)
