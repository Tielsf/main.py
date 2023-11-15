########## Begin ##########
def norm(x):
    sum=0
    for i in (x):
        sum+=i**2
        x=sum**0.5
    x=float(x)
    return(x)
x1 = [3, 4]
x2 = [1, 2, 3]
x3 = [1, 2, 3, 5, 6, 7, 8]
print('||x1|| = %.2f' % norm(x1))
print('||x2|| = %.2f' % norm(x2))
print('||x3|| = %.2f' % norm(x3))