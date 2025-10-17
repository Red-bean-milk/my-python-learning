#===========(1)递归=============
def sum_digits(n):
    '''函数计算正整数n所有位的数字之和
    '''
    if n // 10 == 0:    # Base case
        return n
    else:
        return sum_digits(n // 10) + n % 10     # Induction step

print(sum_digits(456))


def fact(n):
    '''fact函数使用递归计算自然数n的阶乘
    '''
    if n == 1:
        return n
    else:
        return fact(n - 1) * n
n = 5
print(f'自然数{n}的阶乘是{fact(n)}')


#===========(2)互递归======================
# 当一个递归过程被划分到两个相互调用的函数中时，这两个函数被称为是互递归的（mutually recursive）
# 如果一个数比一个奇数大 1，那它就是偶数
# 如果一个数比一个偶数大 1，那它就是奇数
# 0 是偶数

def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)
print(is_odd(7)) 

def is_even_single(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return is_even_single(n - 2)
print('7是否是偶数', is_even_single(7))

# Reference Solution
def is_even_single_reference(n):
    if n == 0:
        return True
    else:
        if (n - 1) == 0:
            return False
        else:
            return is_even_single_reference((n - 1) - 1)
print('9是否是偶数', is_even_single_reference(9))

#===========(3)递归打印--可视化递归过程==============
def cascade(n):
    '''打印数字n的前缀的级联'''

    if n < 10:
        print(n)
        return n
    else:
        print(n)
        return cascade(n // 10)
print(cascade(2013),'\n')

# Reference Solution
print('Reference Solution:')
def cascade_reference(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)
print(cascade_reference(2013))

#取石子比赛（互递归）
#Alice的策略（策略返回Alice是否获胜）
def Alice(n):   
    if n==0 or n-1==0:
        print('Alice wins') #return True
    else:
        return Bob(n-1)
#Bob的策略（策略返回Bob是否获胜）
def Bob(n):
    if n-1==0 or n-2==0:
        print('Bob wins') #return True
    else:
        if n%2==0:
            return Alice(n-2)
        else:
            return Alice(n-1) 
print(Alice(13)) # 由于是Alice先手，所以先使用Alice的策略

# Reference Solution：
def play_alice(n):
    if n==0:     #这个我没有想到
        print('Bob wins!')
    else:
        play_bob(n-1)

def play_bob(n):
    if n==0:     #这个我没有想到
        print('Alice wins!')
    elif is_even(n):
        play_alice(n-2)
    else:
        play_alice(n-1)
print(play_alice(13))
#两种代码均正确

#==========（4）树递归===============
#具有多个递归调用的函数称为树递归
#斐波那契数列
def fib(n):
    '''输出斐波那契数列第n个数的值,假设fib(0)=0,fib(1)=1'''
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print('斐波那契数列第6个数是',fib(6))

#分割数
def count_partitions(n, m):
    '''该函数返回使用 m 作为最大部分对 n 进行分割的方式的数量'''
    if m==1 or n==0:
        return 1
    if m==0 or n<0:
        return 0
    else:
        return count_partitions(n-m,m)+count_partitions(n,m-1)
print(count_partitions(6,4))

# Reference Solution：
def count_partitions(n, m):
    """计算使用最大数 m 的整数分割 n 的方式的数量"""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:  #n>0且m==0
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)

'''我的代码是存在问题的，比如当n<0且m=1(虽然这种情况不会发生)，会先判定m=1而返回1，而n<0是不可能分割的
因此需要if-elif-else隐含的范围限定来做条件判断
其实我的代码把if m==1 or n==0改成if n==0就可以了，把m==1去掉。
因为树右边，m-1=0，返回0；左边(n-1,1)最后会变成(0,1)而返回1,因此不需要单独把m==1拿出来判断'''