# factor = 5
# numbers = [1, 45, -67, 62, 0, -1]

# new_list = []
# for num in numbers:
#     new_list.append(num * factor)

# print(new_list)

def multiply(numbers_to_multiply, multiplication_factor):
    # numbers_to_multiply = [1, 45, -67, 62, 0, -1]

    new_list = []
    for num in numbers_to_multiply:
        new_list.append(num * multiplication_factor)

    return new_list