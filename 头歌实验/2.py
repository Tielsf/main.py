########## Begin ##########
import numpy as np
import matplotlib.pyplot as plt

def calBombTrace(h, v0):
    g,n = 9.8,30
    v0=50
    tmax=(2*h/g)**0.5
    t=np.linspace(0, tmax, n)
    xt=v0*t*np.cos(np.radians(a))
    yt=v0*t*np.sin(np.radians(a))-0.5*g*t**2
    return xt, yt
A=[30,45,60,75]
for a in A:
    xt,yt = calBombTrace(a)
    plt.plot(xt,yt,'r-')
plt.grid('on')
plt.axis([0, 260, 0, 120])
plt.show()



########## End ##########
plt.savefig( 'src/step6/student/pic.png' )
plt.close()