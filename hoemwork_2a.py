#Hayama, Blake
#Computer Programming p4
#Assignment 2a
#september 10, 2026
hobbies = ["baseball", "beach", "video games", "Hanging with friends", " watching football"]
print(hobbies)
print(len(hobbies))
print(hobbies[2])
print(hobbies[0])
hello_list = ["hello!"] * 100
print(hello_list)
list1 = ["pumpkin", "halloween", "jack-o-lantern", "spooky"]
list2 = ["christmas", "new year", "holiday", "santa"]
list3 = list1 + list2
print(list3)
favFoods = ["sushi", "ice cream", "burger", "steak", "pasta"]
print(len(favFoods))
print(favFoods[2])
print(favFoods[-2])
favFoods.append("Blake")
favFoods.insert(2, 16)
favFoods.remove("ice cream")
print(favFoods)
for number in range(1, 3):
    print(number)
odd_numbers = list(range(1, 3, 5))
for number in odd_numbers:
    print(number)
animals = ["dog", "cat", "bird"]
for animal in animals:
    print(animal)
for animal in animals:
    print("A " + animal + " would make a great pet.")
print("Any of these animals would make a great pet!")
guests = ["LeBron James", "Mrs. Kashanchi", "Josh Allen"]
for guest in guests:
    print("You are invited to dinner, " + guest + "!")
print(guests[1] + " can't make it to dinner.")
guests[1] = "LeBron James"
for guest in guests:
    print("You are invited to dinner, " + guest + "!")

