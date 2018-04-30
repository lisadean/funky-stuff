from rot13 import rot13
from dedupe import dedupe
from leetspeak import leetspeak
from multiply import multiply
from smallest_number import smallest_number
from longvowel import longvowel

text = "lbh zhfg hayrnea jung lbh unir yrnearq"
print("Converting this ROT13 encoded text: %s" % text)
print(rot13(text))
print()

list_to_dedupe = [1, 3, 4, 4, 23, 1, 0, 100]
print("Deduping this list: %s" % list_to_dedupe)
print(dedupe(list_to_dedupe))
print()

text_to_convert = "elite speak"
print("Converting this to leetspeak: %s" % text_to_convert)
print(leetspeak(text_to_convert))
print()

numbers_to_multiply = [1, 45, -67, 62, 0, -1]
multiplication_factor = 5
print("Multiplying these numbers by %d: %s" % (multiplication_factor, numbers_to_multiply))
print(multiply(numbers_to_multiply, multiplication_factor))
print()

list_of_numbers = [1, 45, 62, 0, -1]
print("Finding smallest number in this list: %s" % list_of_numbers)
print(smallest_number(list_of_numbers))
print()

text = "scoot the door open for the cheese"
print("Converting this string to long vowels: %s" % text)
print(longvowel(text))
print()