list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 1, 3]

print(4 in list1)


word = "hello"

list_t = list(word)
print(list1)


list4 = list1 + list2 + list3
print(list4)

autos = ["audi", "bmw", "mercedes"]
print(autos)
autos.append("toyota")
print(autos)

stringg = "hELLO, world"
new_s = stringg.replace("world", "python")
print(stringg)
print(new_s)

auto = autos.pop()
print(auto)

autos2 = ["volvo", "kia", "ferrari"]

autos.extend(autos2)
print(autos)
print(autos2)
print(len(autos))


list2.sort(reverse=True)
print(list2)

full_name = "Yuliia Ivaniuk 18 Davydiv student"
full_list = full_name.split(" ")
print(full_list)
join_name = " ".join(full_list)
print(join_name)

numbers = [1,6,64,23,12,64,75,8,456,234,567,35,63,14,235,457,588,23443,24,460,0]
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(len(numbers))

tmp = autos[0]
autos[0] = autos[4]
autos[4] = tmp
print(autos)