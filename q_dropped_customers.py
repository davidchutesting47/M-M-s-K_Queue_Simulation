from MMSK.mathAnalysis import *
from MMSK.simulation import *
import matplotlib.pyplot as plt
import math

lam = 100*1000  # arrivals per hour
meanServiceTime = 5/60 # mean service time
mu = 1/meanServiceTime  # param of exponential distribution. 1/mu is mean service time
# sList = range(1,8)
sList = [i * 1000 for i in range(1,11)] # num servers
# k = 8  # max number of customers (in queue + being served by servers)
waitQueueLen = 1 # set to at least 1 to avoid bug. replaces k
x = []
simLy = []
simWy = []
simLqy = []
simWqy = []
simHours = 2
numCustomers = lam * 2
#numCustomers = 2000
numCustomersDroppedPct = []

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
    simLy.append(quSim.avgWaitLen) # The average number of customers in the system
    simWy.append(quSim.avgWaitTime) # The average dwell time of a customer in the system
    simLqy.append(quSim.avgWaitQuLen) # The average queuing length
    simWqy.append(quSim.avgWaitQuTime) # The average waiting time of customers
    numCustomersDroppedPct.append(quSim.numCustomersDropped / numCustomers)

print('SIM :x = ', x, ', avgWaitLen = ', simLy)
print('SIM :x = ', x, ', avgWaitTime = ', simWy)
print('SIM :x = ', x, ', avgWaitQuLen = ', simLqy)
print('SIM :x = ', x, ', avgWaitQuTime = ', simWqy)
print('SIM2 :x = ', x, ', dropped = ', numCustomersDroppedPct)

plt.plot(x, numCustomersDroppedPct, 'bo-', label='pct. dropped')
plt.title('')
plt.xlabel('num servers')
plt.ylabel('% customers dropped')
for x, y in zip(x, numCustomersDroppedPct):
    plt.text(x, y, '%.4f' % y, ha='center', va='bottom')

plt.legend()
plt.show()
