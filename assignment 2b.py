# Blake Hayama
# Computer Programming, period 4
# assignment 3a
# September 25, 2026 
alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points for shooting the alien!")
else:
    print("You earned 10 points for shooting the alien!")
alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points for shooting the alien!")
else:
    print("You earned 10 points for shooting the alien!")
alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")
alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")
alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")
ages = [1, 3.9, 10, 13, 19, 20, 21, 65]
for age in ages:
    if age < 2:
        print("You are a baby.")
    elif age < 4:
        print("You are a toddler.")
    elif age < 13:
        print("You are a kid.")
    elif age < 20:
        print("You are a teenager.")
    elif age < 65:
        print("You are an adult.")
    else:
        print("You are an elder.")
usernames = ['blake', 'gurt', 'phelo', 'him', 'her']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username.title() + ", thank you for logging in again.")
else:
    print("We need to find some users!")
current_users = ['blake', 'gurt', 'phelo', 'him', 'her']

new_users = ['blake123', 'gurt123', 'phelo123', 'him123', 'her123']
current_users_lower = []
for username in current_users:
    current_users_lower.append(username.lower())
for username in new_users:
    if username.lower() in current_users_lower:
        print(username + " will need to enter a new username.")
    else:
        print(username + " is available.")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")