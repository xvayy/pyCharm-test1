file_names = ["document1.txt", "image1.jpg", "document2.txt", "image2.jpg"]
for file_name in file_names:
    print(file_name)

greeting = "Yuliia"
count = 0
for char in greeting:
    print(char)
    if(char == "i"):
        count += 1

print(count)


autos = ["audi", "bmw", "mercedes"]

for auto in autos:
    print(auto)
    for char in auto:
        print(char)

numbers = [1,6,64,23,12,64,75,8,456,234,]
# for number in numbers:
#     if (number % 2 == 0):
#         print(number)

greet = "Hello world"
indexes = []
count = 0

for i in range(len(greet)):
    if greet[i] == "o":
        count += 1
        indexes.append(i)

print(count)
print(indexes)

for i in range(1, 10):
    for j in range(1, 10):
        print(i, " * ", j, " = ", i * j)