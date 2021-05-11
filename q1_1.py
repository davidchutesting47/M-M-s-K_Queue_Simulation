from MMSK.mathAnalysis import *
from MMSK.simulation import *
import matplotlib.pyplot as plt
import math

lam = 2  # arrivals per hour
mu = 1.5  # param of exponential distribution. 1/mu is mean service time
k = 8  # max number of customers (in system or in line?)
x = []
Ly = []
simLy = []
numCustomers = 20000
numCustomersDroppedPct = []
for i in range(2, 8):
    # i is number of servers
    x.append(i)
    k = i+1
    quSim = queueSim(lam, mu, i, k, numCustomers)
    quSim.simRun()
    simLy.append(quSim.avgWaitLen)
    Ly.append(L_(lam, mu, i, k))
    numCustomersDroppedPct.append(quSim.numCustomersDropped / numCustomers)
print('MATH:x = ', x, ', y = ', Ly)
print('SIM :x = ', x, ', y = ', simLy)
print('SIM2 :x = ', x, ', dropped = ', numCustomersDroppedPct)
plt.plot(x, simLy, 'ro-', label='sim')
plt.plot(x, Ly, 'g^-', label='math')
plt.title('L')
plt.xlabel('s')
plt.ylabel('L')
tempX = x
for x, y in zip(x, Ly):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(tempX, simLy):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
plt.legend()
plt.show()
