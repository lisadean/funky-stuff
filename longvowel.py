# text = "Good"

# vowels = "aaeeiioouu"

# new_string = ""
# for i in range(len(text)):

#     if text[i] in vowels and (i + 1) < len(text):
#         if text[i] == text[i + 1]:
#             new_string += (text[i] * 3)
#         else:
#             new_string += text[i]
#     else:
#         new_string += text[i]

# print(new_string)

def longvowel(text):
    # text = "scoot the door open for the cheese"

    vowels = "aaeeiioouu"

    new_string = ""
    for i in range(len(text)):

        if text[i] in vowels and (i + 1) < len(text):
            if text[i] == text[i + 1]:
                new_string += (text[i] * 4)
            else:
                new_string += text[i]
        else:
            new_string += text[i]

    return new_string