##Kata 1
"""""
def adjacent_element_product(array):
    max_arr = []
    for index in range(len(array) - 1):
        dob = 1
        dob = array[index] * array[index + 1]
        max_arr.append(dob)

    result = max(max_arr)
    return result

my_arr = [1,32,4,56,7,87,8,35,24,546,8]
adjacent_element_product(my_arr)
"""""

##Kata 2
def to_jaden_case(string):
    result = 0
    arr = []
    for char in string:
        arr.append(char)

    first = arr[0]
    arr[0] = first.upper()
    for index in range(len(arr) - 1):
        sumb = arr[index]
        if sumb == " ":
            tmp = arr[index + 1].upper()
            arr[index + 1] = tmp
    result = "".join(arr)
    print(result)
    return result

to_jaden_case("how can mirrors be real if our eyes aren't real")

