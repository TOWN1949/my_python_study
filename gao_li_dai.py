initial_money=10000
day_rate=1.008
final_money=initial_money*day_rate
i=1
while final_money<200000:
    final_money=final_money*day_rate
    i=i+1
print(i)
