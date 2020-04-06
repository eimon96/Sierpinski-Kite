get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pylab as plt

def gasket(pa, pb, pc, level):
    if level == 0: 
        plt.fill([pa[0], pb[0], pc[0]], [pa[1], pb[1], pc[1]], 'r') 
        plt.hold(True)
    else:
        gasket(pa, (pa + pb) / 2., (pa + pc) / 2., level - 1) 
        gasket(pb, (pb + pa) / 2., (pb + pc) / 2., level - 1) 
        gasket(pc, (pc + pa) / 2., (pc + pb) / 2., level - 1)
        
a = np.array([-0.5 , np.sqrt(3)/2.])
b = np.array([0.5 , np.sqrt(3)/2.])
c = np.array([1.0,0])
d = np.array([0.5,-(np.sqrt(3)/2.)])
e = np.array([-0.5,-(np.sqrt(3)/2.)])
f = np.array([-1,0])
o = np.array([0,0])
level = 3
gasket(o, a, b, level)
gasket(o, b, c, level)
gasket(o, c, d, level)
gasket(o, d, e, level)
gasket(o, e, f, level)
gasket(o, f, a, level)
plt.hold(False)
plt.title("Lv.3")
plt.axis('equal')
