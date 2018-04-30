# numbers = [1, 45, 62, 0, -1]

# smallest = 0
# for num in numbers:
#     if num < smallest:
#         smallest = num

# print(smallest)

def smallest_number(list_of_numbers):
    list_of_numbers = [1, 45, 62, 0, -1]

    smallest = 0
    for num in list_of_numbers:
        if num < smallest:
            smallest = num

    return smallest