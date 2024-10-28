import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

# Parameters
a=str(input('dori vositasining nomini kiriting: '))
x0=float(input('dori vositasining boshlangich miqdori co= '))
k1=float(input('oshqozondan qonga surilish foizi k1='))
k2=float(input('inson tanadan chiqib ketish foizi k2='))
t = 0
tstart = 0
tstop = 25
increment = 1
N = 25
#t = np.arange(tstart,tstop+1,increment)
#Alternative Approach
n = np.linspace(tstart, 24, 25)
t = np.linspace(tstart, tstop, 400)
f=x0*np.exp(-k1*t)
x = x0*k1/(k1-k2)*(np.exp(-k2*t)-np.exp(-k1*t))
print('dori konsentratsiyasining organizmdagi maximal qiymati= ',max(x))
print('organizmda qolgan minimum qiymati=',min(x))
fig, ax=plt.subplots(figsize=(10,5))
plt.plot(t,f)
plt.plot(t,x)
plt.xticks(n)
plt.title([a,' dori vositasining tanada harakatlanishining grafigi'])
plt.xlabel('Vaqt\n')
plt.ylabel('Dori konsentratsiyasi mgramm')
plt.grid()
plt.axis([0, 25, 0, x0])
plt.legend(["oshqozonda so'rilishi","qonga so'rilishi"])
plt.show()

