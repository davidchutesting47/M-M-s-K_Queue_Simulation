from MMSK.mathAnalysis import *
from MMSK.simulation import *
import matplotlib.pyplot as plt
import math

lam = 1*1000  # arrivals per hour
meanServiceTime = 15/60 # mean service time
mu = 1/meanServiceTime  # param of exponential distribution. 1/mu is mean service time
#sList = range(1,8)
sList = [i * 100 for i in range(1,6)] # num servers
# k = 8  # max number of customers (in queue + being served by servers)
waitQueueLen = 1 # set to at least 1 to avoid bug. replaces k
x = []
simLy = []
simHours = 2
numCustomers = lam * 2
#numCustomers = 2000
numCustomersDroppedPct = []

print(np.random.exponential(1/lam)*60)

print(f'lam={lam}, meanServiceTime={meanServiceTime}, mu={mu}')

if lam <= 1/mu:
    serviceTime = 1/mu
    print(f'Service time is too long for arrival rate: Lambda ({lam}) <= 1/Mu ({serviceTime})')
    print('Queue will go to infinity.')
    quit()

for i in sList:
    # i is number of servers
    x.append(i)
    k = i+waitQueueLen
    quSim = queueSim(lam, mu, i, k, numCustomers)
    quSim.simRun()
    simLy.append(quSim.avgWaitLen)
    numCustomersDroppedPct.append(quSim.numCustomersDropped / numCustomers)

print('SIM :x = ', x, ', avgWaitLen = ', simLy)
print('SIM2 :x = ', x, ', dropped = ', numCustomersDroppedPct)

plt.plot(x, numCustomersDroppedPct, 'bo-', label='pct. dropped')
plt.title('')
plt.xlabel('num servers')
plt.ylabel('% customers dropped')
for x, y in zip(x, numCustomersDroppedPct):
    plt.text(x, y, '%.4f' % y, ha='center', va='bottom')

plt.legend()
plt.show()
