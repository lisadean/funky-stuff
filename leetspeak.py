# text = "elite speak"

# original = "AEGIOST"
# translation = "4361057"

# text = text.upper()

# new_string = ""
# for c in text:
#     if c in original:
#         new_string = new_string + translation[original.index(c)]
#     else:
#         new_string = new_string + c

# print(new_string)

def leetspeak(text_to_convert):
    # text_to_convert = "elite speak"
    
    original = "AEGIOST"
    translation = "4361057"

    text_to_convert = text_to_convert.upper()

    new_string = ""
    for c in text_to_convert:
        if c in original:
            new_string = new_string + translation[original.index(c)]
        else:
            new_string = new_string + c

    return new_string