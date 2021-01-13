people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

#def f(person):
#    return person["house"]
#people.sort(key=f)

# instead of creating the previous function it's best ellaborate the same way with the same results

people.sort(key=lambda person: person["name"])

print(people)

