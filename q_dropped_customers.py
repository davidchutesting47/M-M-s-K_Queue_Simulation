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

# if lam <= 1/mu:
#     serviceTime = 1/mu
#     print(f'Service time is too long for arrival rate: Lambda {lam} <= 1/Mu {serviceTime}')
#     print('Behavior is unstable.')
#     quit()

for i in range(1, 8):
    # i is number of servers
    x.append(i)
    quSim = queueSim(lam, mu, i, k, numCustomers)
    quSim.simRun()
    simLy.append(quSim.avgWaitLen)
    Ly.append(L_(lam, mu, i, k))
    numCustomersDroppedPct.append(quSim.numCustomersDropped / numCustomers)
print('MATH:x = ', x, ', y = ', Ly)
print('SIM :x = ', x, ', y = ', simLy)
print('SIM2 :x = ', x, ', dropped = ', numCustomersDroppedPct)

#plt.plot(x, simLy, 'ro-', label='sim')
#plt.plot(x, Ly, 'g^-', label='math')
plt.plot(x, numCustomersDroppedPct, 'bo-', label='pct. dropped')
plt.title('')
plt.xlabel('num servers')
plt.ylabel('% customers dropped')
tempX = x
tempX2 = x
# for x, y in zip(x, Ly):
#     plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
#
# for x, y in zip(tempX, simLy):
#     plt.text(x, y, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(tempX2, numCustomersDroppedPct):
    plt.text(x, y, '%.4f' % y, ha='center', va='bottom')

plt.legend()
plt.show()
