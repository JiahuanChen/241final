import random

avg_days = []
calc_length = []
steps = 50
simulate_times = 50000
#simulate each probability
for j in range(1,steps):
    p = j/steps
    avg_days.append(1)
    calc_length.append(0)
    #do lots of simulations
    for i in range(0,simulate_times):
        total_days = 0
        # keep on running at probability of p
        while (random.uniform(0.0, 1.0)<=p):
            total_days += 1
        avg_days[j-1] += total_days/simulate_times

p = [i/steps for i in range(1,steps)]

for i in range(0,steps-1):
    #probability; difference between simulation and calculation; sumulation results
    print(round(p[i],2), round(avg_days[i] - 1/(1-p[i]),5), round(avg_days[i],5))
