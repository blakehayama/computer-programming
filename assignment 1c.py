#Blake Hayama
#Assignment 1c

#Part 1
name_of_object = input("Enter the name of an object: ")
mass_kg = input("What is the mass of the object in kg? ")
velocity = input("What is the velocity of the object in m/s? ")

name_of_object = name_of_object.strip().title()
mass_kg_num = float(mass_kg)
velocity_num = float(velocity)

KE_joules = 1/2 * mass_kg_num * (velocity_num ** 2)

KE_calories = KE_joules / 4.184

KE_erg = KE_joules * 10**7

#print("Kinetic Energy Report for: ", name_of_object)
output_line_one = f"Kinetic Energy Report for: {name_of_object}"
print(output_line_one)
output_line_two = f"Joules:\t{KE_joules} J"
print(output_line_two)
output_line_three = f"Calories:\t{KE_calories} cal"
print(output_line_three)
output_line_four = f"Ergs:\t{KE_erg} erg"
print(output_line_four)