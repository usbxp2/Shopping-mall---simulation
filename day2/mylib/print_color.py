__author__ = 'huanghao'

def print_color(str,yanse):
    if yanse == 'red':
        print('\033[0;31;1m%s \033[0m' % str)
    elif yanse == 'green':
        print('\033[0;32;1m%s \033[0m' % str)
    elif yanse == 'yellow':
        print('\033[0;33;1m%s \033[0m' % str)
    else:
        print('%s' % str)

if __name__ == '__main__':
    print_color('test string!!!','green')
    print_color('test string!!!','yellow')
    print_color('test string!!!','red')
    print_color('test string!!!','black')