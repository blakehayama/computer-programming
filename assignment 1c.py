# Blake Hayama
# Computer Programming
# Assignment 1c
# September 11, 2026
object_name = "Baseball"
mass = 5.0
velocity = 4.0
ke_joules = 0.5 * mass * velocity ** 2
ke_calories = ke_joules / 4.184
ke_ergs = ke_joules * 10 ** 7
print(f"Kinetic Energy Report for: {object_name}")
print(f"Joules: {ke_joules:.2f} J")
print(f"Calories: {ke_calories:.2f} cal")
print(f"Ergs: {ke_ergs:.2f} erg")