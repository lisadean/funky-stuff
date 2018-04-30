def rot13(text):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_string = ""

    # for i in range(len(text)):

    #     if text[i] != " ":

    #         alphabet_index = alphabet.index(text[i])
    #         # print(str(text[i]) + " = " + str(alphabet_index))

    #         if alphabet_index < 13:
    #             transposition = alphabet_index + 13
    #         else:
    #             transposition = 13 - (25 - alphabet_index) - 1

    #         # print(transposition)
    #         new_string += alphabet[transposition]

    #     else:
    #         new_string += " "

    for i in range(len(text)):
        # text = "lbh zhfg hayrnea jung lbh unir yrnearq"

        if text[i] != " ":

            alphabet_index = alphabet.index(text[i])

            if alphabet_index + 13 < 26:
                transposition = alphabet_index + 13
            else:
                transposition = alphabet_index + 13 - 26
            
            new_string = new_string + alphabet[transposition]
        
        else:
            new_string = new_string + " "

    return new_string

# text = "lbh zhfg hayrnea jung lbh unir yrnearq"

# print(rot13(text))
