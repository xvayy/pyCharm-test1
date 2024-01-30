##1. Two Sum
"""def twoSum(arr, target):
    size = len(arr)
    extra_arr = []
    for index in range(size):
        for index2 in range(index + 1, size):
            aim = arr[index] + arr[index2]
            if aim == target:
                extra_arr.append(index)
                extra_arr.append(index2)
                return extra_arr


my_list = [3,2,4]
print(twoSum(my_list, 6))"""

##13. Roman to Integer
"""def romanToInt(s) -> int:
    sum = 0
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    arr = []
    for char in s:
        arr.append(char)

    print(arr)
    ris = 0
    for key, value in roman.items():
        for i in range(len(arr) - 1):
            if arr[i] == "I":
                if arr[i + 1] == "V":
                    ris = roman["V"] - roman["I"]
                elif arr[i + 1] == "X":
                    ris = roman["X"] - roman["I"]
            elif arr[i] == key:
                sum += value

    result = sum + ris
    return result


print(romanToInt("XXXIX"))
"""

##9. Palindrome Numbe
"""def isPalindrome(x) -> bool:
    arr = []
    new_arr = []
    string = str(x)

    for i in string:
        arr.append(i)
        new_arr.append(i)

    print(arr)
    new_arr.reverse()
    print(new_arr)
    result = []

    for char, char2 in zip(arr, new_arr):
        if char == char2:
            result.append(char)
        else:
            return False
    print("dffs",result)
    return True

print(isPalindrome(211112))"""

##14. Longest Common Prefix
"""def longestCommonPrefix(strs) -> str:
     result = []

     str1 = strs[0]
     arr = list(str1)
     print(arr)
     if len(strs) == 1:
         return "".join(strs)

     for i in range(len(arr)):
         search_char = arr[i]
         search_index = i
         next_char = i + 1 < len(arr)
         t_counter = 0
         f_counter = 0
         print("Search",search_char)
         for str in strs:
             print(str)
             for index, char in enumerate(str):
                 print("Char: ", char)
                 if search_char == char:
                     # print("Yes")
                     if index == 0:
                         t_counter += 1
                     elif str.index(char) + 1 < len(str) and str[str.index(char) + 1] == next_char:
                         t_counter += 1

                 else:
                     # print("NO")
                     f_counter += 1
         print("True: ", t_counter)
         print("False: ", f_counter)

         if t_counter == len(strs):
             result.append(search_char)
     print(next_char, "NEXT")
     print(search_index, "jsfhkjsdhf")
     if len(result) == 0:
         return ""
     else:
         ret = "".join(result)
         print(type(ret))
         return ret
def longestCommonPrefix(strs) -> str:
        result = []

        if not strs:
            return ""

        str1 = strs[0]
        arr = list(str1)

        if len(strs) == 1:
            return "".join(strs)

        for i in range(len(arr)):
            search_char = arr[i]
            search_index = i
            next_char = arr[i + 1] if search_index + 1 < len(arr) else None
            t_counter = 0
            f_counter = 0

            for string in strs:
                if search_index < len(string) and search_char == string[search_index]:
                    t_counter += 1
                elif search_index == len(string):
                    t_counter += 1
                else:
                    f_counter += 1

            if t_counter == len(strs) and next_char is not None:
                result.append(search_char)

        if len(result) == 0:
            return ""
        else:
            ret = "".join(result)
            return ret
print(longestCommonPrefix(strs = ["cir"]))
print(longestCommonPrefix(strs = ["flower","flower","flower","flower"]))"""