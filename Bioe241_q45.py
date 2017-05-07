import random

r = 0.4
p = 0.8
avg_r_days = 0
avg_v_days = 0
#say r is much faster then v ...
r_mu = 50
r_sigma = 5
v_mu = 80
v_sigma = 10

avg_speed = 0

simulate_times = 1000
flag = "Prunning"
#do lots of simulations
for i in range(0,simulate_times):
    r_days = 0
    v_days = 0
    speed = 0
    #simulate for 365 days
    #first day, probability of p is V
    if random.uniform(0.0, 1.0)<=p:
        flag = "Vrunning"
    else:
        flag = "Rrunning"
    for j in range(0,365):
        if flag == "Vrunning":
            #flag == True r is running
            v_days += 1
            speed += random.gauss(v_mu,v_sigma)/365
            if random.uniform(0.0, 1.0)<=p:
                flag = "Vrunning"
            else:
                flag = "Rrunning"
        else:
            r_days += 1
            speed += random.gauss(r_mu,r_sigma)/365
            if random.uniform(0.0, 1.0)<=r:
                flag = "Rrunning"
            else:
                flag = "Vrunning"

    avg_r_days += r_days/simulate_times
    avg_v_days += v_days/simulate_times
    avg_speed += speed/simulate_times

print("days proportion:")
print("sumulation results:")
print(avg_r_days, avg_v_days)
print("calculation results:")
print((1-p)/(2-p-r)*365,(1-r)/(2-p-r)*365 )
print("difference:")
print(avg_v_days-(1-r)/(2-p-r)*365, avg_r_days-(1-p)/(2-p-r)*365)
print("speed:")
print(avg_speed)
print((1-r)/(2-p-r)*v_mu + (1-p)/(2-p-r)*r_mu)
