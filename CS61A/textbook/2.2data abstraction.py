from math import gcd   #gcd(x,y)求x和y的最大公约数

# 数据表示
def rational(n,d):
    '''返回一个有理数化简后的分子分母对'''
    a = gcd(n,d)
    return [n//a,d//a]

def numer(x):
    '''返回有理数x的分子'''
    return x[0]

def denom(x):
    '''返回有理数x的分母'''
    return x[1]

# 数据操作
def add_rationals(x,y):
    '''有理数加法:返回有理数x和y相加后的结果'''
    nx,dx = numer(x),denom(x)
    ny,dy = numer(y),denom(y)
    return rational(nx*dy+ny*dx,dx*dy)

def mul_rationals(x,y):
    '''有理数乘法'''
    return rational(numer(x)*numer(y),denom(x)*denom(y))

def print_rational(x):
    '''打印有理数，以分子/分母的形式输出'''
    print(numer(x),'/',denom(x))

def rationals_are_equal(x,y):
    '''判断两个有理数是否相等'''
    return numer(x)*denom(y)==numer(y)*denom(x)  #交叉相乘

#抽象屏障
def square_rational(x):
    return mul_rationals(x,x)

def square_rational_one(x):
    '''mul_rationals()由numer()和denom()定义'''
    return rational(numer(x)*numer(x),denom(x)*denom(x))

def square_rational_two(x):
    '''numer()和denom()由x[]定义'''
    return rational(x[0]*x[0],x[1]*x[1])



