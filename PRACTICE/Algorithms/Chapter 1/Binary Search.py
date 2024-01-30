my_list = [1,2,5,7,8,9,14,34,57,78,89,90]


def binar(list, search):
    left = 0
    right = len(list) - 1
    compare_caunter = 0
    while left <= right:
        middle = int((left + right)/2)
        compare_caunter += 1
        if search == list[middle]:
            result = print("Значення знайдено, було потрібно",compare_caunter,"порівнянь")
            break
        elif search > list[middle]:
            left = middle + 1
        elif search < list[middle]:
            right = middle - 1

    return result


print(binar(my_list, 5))