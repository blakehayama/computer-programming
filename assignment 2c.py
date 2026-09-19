#Blake Hayama
#Assignment 2c
#Computer Programming p4
#September 18, 2026
flight_log = [1000, 2500, 4200, 6000, 7800, 9500, 11000, 12500]
print("Initial log:", flight_log)
flight_log.append(14000)
flight_log.append(15500)
print("After append:", flight_log)
removed = flight_log.pop(0)
removed = flight_log.pop(0)
print("After pop:", flight_log)
flight_log.insert(3, 9000)
print("After insert:", flight_log)
print(f"Reading at index 3: {flight_log[3]}")