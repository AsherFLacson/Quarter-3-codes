import numpy as pyn
names = [ "Borris", "Bobby", "Garry"]
days = [ "Friday","Saturday", "Sunday", "Monday", "Tuesday" ]
steps = pyn.array([ [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]])
  
daily_totals = steps.sum(axis=0)
print(daily_totals)
for i in range(len(days)):
    print(days[i], "total steps:", daily_totals[i])
most_active = pyn.argmax(daily_totals)
most_active_day = days[most_active]

print("Most active day overall:", most_active_day)
print("Total steps that day:", daily_totals[most_active])