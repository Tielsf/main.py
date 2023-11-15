
#e1.1TempConvert.py
TempStr=input("请输入带有符号的温度值：")
if TempStr[-1] in ['F','f']:
    C=(eval(TempStr[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F=1.8*eval(TempStr[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
    print("输入格式错误")    

'''
H=input("鼠子：")
if H[-1] in ['K','A']:
    C=(eval(H[0:-1]))
    print("我爱{}K".format(C))'''