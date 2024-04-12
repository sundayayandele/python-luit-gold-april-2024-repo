connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
    
rome_counter = 0
total_f_time = 0
for connection in connections:
    if connection[1] == "Rome":
        rome_counter += 1
        total_f_time += connection[2]
    #total_f_time += connection[2]
    
avg_f_time = total_f_time/rome_counter

print(str(rome_counter) + " connections lead to Rome with an average flight time of " + str(avg_f_time) + " minutes")