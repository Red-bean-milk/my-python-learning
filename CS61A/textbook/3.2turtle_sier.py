from turtle import *

# 谢尔宾斯三角形
def repeat(k,fn):
    if k > 0:
        fn()           
        repeat(k-1,fn)

def tri(fn):
    def inner():
        fn()
        lt(120)
    repeat(3,inner)

def sier(d,k):
    def inner():
        if k == 1:
            fd(d)
        else:
            leg(d,k)
    tri(inner)

def leg(d,k):
    sier(d/2,k-1)
    penup()
    fd(d)
    pendown()

speed(1000)
sier(200,3)

done()


