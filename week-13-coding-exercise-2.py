income = 250_000
lowtaxland_rate = 0.05
ripoffland_rate = 0.43
lowtaxlandAmount = income * lowtaxland_rate
ripofflandAmount = income * ripoffland_rate

taxDiff = ripofflandAmount - lowtaxlandAmount

outputString = 'Your income is ' + str(income) + ' and you would pay ' + str(lowtaxlandAmount) + ' income tax in Lowtaxland or ' + str(ripofflandAmount) + ' income tax in Ripoffland. You would save ' + str(taxDiff) + ' by paying taxes in Lowtaxland!'

print(outputString)