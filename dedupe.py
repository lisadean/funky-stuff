# input_text = [1, 3, 4, 4, 23, 1, 0, 100]

# new_list = []
# for i in range(len(input_text)):
#     if input_text[i] not in new_list:
#         new_list.append(input_text[i])

# print(new_list)

def dedupe(list_to_dedupe):
    # list_to_dedupe = [1, 3, 4, 4, 23, 1, 0, 100]
    new_list = []
    for i in range(len(list_to_dedupe)):
        if list_to_dedupe[i] not in new_list:
            new_list.append(list_to_dedupe[i])

    return new_list
