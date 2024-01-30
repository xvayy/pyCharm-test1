person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

person.popitem()
person.popitem()
person.popitem()
print(person)

for p in person:
    print(person[p])


for item in person.items():
    print(item)
    print(type(item))

for key in person.keys():
    print(key)
    print(type(key))

for value in person.values():
    print(value)
    print(type(value))


person1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
other_person = {
    "city": "Lviv",
    "age": 31,
    "name": "John",
    "auto": "audi"
}

# person1.update(other_person)
person1 = person1 | other_person
print(person1)



person10 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

m_copy = person10.copy()
m_copy["name"] = "Yuliia"

print(person10)
print(m_copy)