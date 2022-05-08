import time
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED

#Setup LED Matrix here

start_time = time.time()
laptime_current = 0
laptime_all= []
laptime_avg = 0
minutes = 0
seconds = 0

while (event.action != ACTION_HELD):
    press = input() 
    laptime_current = int((time.time()) - start_time)
    start_time = time.time()
    laptime_all.append(laptime_current)
    minutes = laptime_current / 60
    seconds = laptime_current % 60
    print("minutes:", minutes)
    print("seconds:", seconds)

for x in laptime_all:
    laptime_avg += x

laptime_avg = laptime_avg / len(laptime_all)

minutes = laptime_avg / 60
seconds = laptime_avg % 60

print("avg time:", minutes, " minutes,", seconds, " seconds")