#Pass skips the entire loop
for i in range (11):
    pass

#Nested loop
for a in range(1,6):
    for b in range(1, 6):
        print(a, 'x', b, '=', a * b)
        
#Else with loop. Else branch of a loop is always executed exactly onc. Exception: break
i = 2
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)