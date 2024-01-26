'''a,b=input().split()
a1,b1=int(a),int(b)
c=a1-b1+2
print(c)'''

'''

n=eval(input('请输入层数:'))   #0<n<100000
  





'''

'''
sum=0
N=eval(input())
for i in range(1,N+1):
    a=0.5*(1+i)*i
    sum+=a
    a1=int(a)
    sum1=int(sum)
    #print(a1)
    #print(sum1)
    print(sum1)    

'''

#int函数 将数变为整数输出
#spilt函数  将字符串分隔开
'''
A=(input("输入多个整数，用空格隔开："))  
#A=1 2 3 4 5 6 
#for i in A:
A1=A.split()
b=max(A1)
print(b)
'''
'''求最大值
nummap = map(int,input().split()) #读取输入，并将字符串分割后转换为整数
maxnum = max(nummap) #获取最大值
print(maxnum)'''
'''  
a=input()
lst1=a.split(' ')   #分隔  字符串组成的列表
lst2=list(map(int,lst1))   #map函数  转化为数字列表
print(max(lst2)) '''   #max函数   取出最大值

#n=input('请输入一个整数:')
'''N=int(n)
if n<37:
    print('0')
sum=0
if n>=37:
    for i in range(n+1):
        if i%37==0:
            sum=sum+i
print(sum)'''




'''


n=input('请输入一个整数:')
N=int(n)
if N<37:
    print('0')
sum=0
if N>=37:
    for i in range(N):
        if i%37==0:
            sum=sum+i
        print(sum)
#print(n)
#print(N)
#print(type(n))
#print(type(N))
'''


#import keyword
#print(keyword.kwlist)

num=eval(input('请输入：'))
'''
if m==1 or 0:
    m1=1

for i in m:
    m1=i*(i-1)
    print(m1)    '''
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(num))