#圆面积的计算
radius=25
area=3.1415*radius*radius
print(area)
print("{:.2f}".format(area))


#简单的人名对话
#name=input("输入姓名")  
#输入姓名:"练思帆"l
#print("{}同学，学好Python，前途无量！".format(name))
#print("{}大侠，学好Python，大展拳脚！".format(name[0]))
#print("{}哥哥，学好Python，人见人爱！".format(name[1:]))


#斐波那契数列的计算
a,b=0,1       
while a<1000:
    print(a,end=',')
    a,b=b,a+b


#同切圆的绘制
#import turtle  
#turtle.pensize(2)
#turtle.circle(10)
#turtle.circle(40)
#turtle.circle(80)
#turtle.circle(160)


#日期和时间的输出
from datetime import datetime  
now=datetime.now()
print(now)
now.strftime("%x")
now.strftime("%X")


