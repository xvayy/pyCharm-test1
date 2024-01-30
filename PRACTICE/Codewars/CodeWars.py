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
'''def to_jaden_case(string):
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

to_jaden_case("how can mirrors be real if our eyes aren't real")'''

##Fix My Phone Numbers
"""def is_it_a_num(s: str) -> str:
    digit_counter = 0
    arr_of_digit = []
    for char in s:
        if char.isdigit():
            arr_of_digit.append(char)
            digit_counter += 1

    if digit_counter == 11 and arr_of_digit[0] == "0":
        return ''.join(arr_of_digit)
    else:
        return "Not a phone number"

print(is_it_a_num("S:)0207ERGQREG88349F82!efRF)"))"""

##Disemvowel Trolls A, E, I, O, U
"""def disemvowel(string):
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    arr = list(string)  # Convert string to a list of characters
    new_arr = []

    for char in arr:
        if char not in vowels:
            new_arr.append(char)

    new_string = ''.join(new_arr)
    return new_string

strrr = "This website is for losers LOL!"
disemvowel(strrr)"""

##Number of People in the Bus
"""def number(bus_stops):
    total_passengers = 0

    for stop in bus_stops:
        on_board, off_board = stop
        total_passengers += on_board - off_board

    return total_passengers

print(number([[10, 0], [3, 5], [5, 8]]))"""

##Given an array of integers.
def count_positives_sum_negatives(arr):
    count_positiv = 0
    arr_negative = []
    for i in arr:
        if i > 0:
            count_positiv += 1
        elif i < 0:
            arr_negative.append(i)

    sum = 0
    for i in arr_negative:
        sum += i

    result = []
    if count_positiv == 0 and sum == 0:
        return result
    elif not arr:
        return result
    else:
        result.append(count_positiv)
        result.append(sum)
        return result
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
)