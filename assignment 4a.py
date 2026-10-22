#Blake Hayama
#Computer Programming
#Assignment 4a
#October 22, 2026

People = {
    "first_name": "Gabe",
    "last_name": "Hart",
    "age": 16,
    "city": "Los Angeles",
}
print("First Name:", People["first_name"])
print("Last Name:", People["last_name"])
print("Age:", People["age"])
print("City:", People["city"])

aboutMe = {
    "name": "Blake Hayama",
    "age": 16,
    "favFood": ["Sushi", "ice cream", "steak"],
    "hairColor": "Black",
    "favSubject": "Computer Programming",
    "favSweet": "Gummy Worms",
    "favHobbies": ["Baseball", "Golfing", "going to the beach"],
    "likeCoding": True
}
print("Name:", aboutMe["name"])
print("Age:", aboutMe["age"])
print("Favorite Food:", aboutMe["favFood"])
print("Hair Color:", aboutMe["hairColor"])
print("Favorite Subject:", aboutMe["favSubject"])
print("Favorite Sweet:", aboutMe["favSweet"])
print("Favorite Hobbies:", aboutMe["favHobbies"])
print("Like Coding:", aboutMe["likeCoding"])

phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
phonebook["Jake"] = 938273443
del phonebook["Jill"]
print(phonebook)

glossary = {
    "Rights": "Things that every person has.",
    "Constitution": "A document that explains how a government works.",
    "Revolution": "A major change in a government or society.",
    "Liberty": "The freedom to make choices.",
    "Freedom": "The power or right to act, speak, or think as one wants without hindrance or restraint."
}
print("Glossary")
for word, meaning in glossary.items():
    print(word + ":")
    print(meaning)

glossary["Ratification"] = "The official approval of an agreement or document."
glossary["Confederation"] = "A group of states joined together under a central government."
glossary["Amendment"] = "A change or addition to a document or law."
glossary["Republic"] = "A government where people elect representatives."
glossary["Compromise"] = "An agreement where each side gives up something."
print("Glossary 2")
for word, meaning in glossary.items():
    print(word + ":")
    print(meaning)

rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Mississippi": "United States"
}
print("Rivers")
for river, country in rivers.items():
    print(river + " runs through " + country)
print("Rivers:")
for river in rivers.keys():
    print(river)
print("Countries:")
for country in rivers.values():
    print(country)
   
person1 = {  
    "firstName": "Gabe",
    "lastName": "Hart",
    "favColor": "red",
    "birthMonth": "January"
}
person2 = {
    "firstName": "Evan",
    "lastName": "Miers",
    "favColor": "red",
    "birthMonth": "February"
}
person3 = {
    "firstName": "Harrison",
    "lastName": "Morris",
    "favColor": "Green",
    "birthMonth": "March"
}
people = [person1, person2, person3]
print("Nesting_1")
for person in people:
    print("First Name:", person["firstName"])
    print("Last Name:", person["lastName"])
    print("Favorite Color:", person["favColor"])
    print("Birth Month:", person["birthMonth"])

cities = {
    "Washington DC": {
        "country": "United States",
        "population": "About 700,000",
        "fact": "capital of usa."
    },
    "Paris": {
        "country": "France",
        "population": "About 2.1 million",
        "fact": "capital of france."
    },
    "Tokyo": {
        "country": "Japan",
        "population": "About 14 million",
        "fact": "It is the capital of Japan."
    }
}
print("Nesting_2")
for city, information in cities.items():
    print("City:", city)
    print("Country:", information["country"])
    print("Population:", information["population"])
    print("Fact:", information["fact"])