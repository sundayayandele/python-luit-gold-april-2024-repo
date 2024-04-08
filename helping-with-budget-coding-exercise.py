spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]
low_count = 0
normal_count = 0
high_count = 0

for spending in spendings:
    if spending < 1000.0:
        low_count += 1
    elif spending >= 1000.0 and spending <= 2500.0:
        normal_count += 1
    else:
        high_count += 1


print("Numbers of months with low spendings: " + str(low_count) + ", normal spendings: "+ str(normal_count) +", high spendings: " + str(high_count) + ".")
