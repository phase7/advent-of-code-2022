from icecream import ic
from puzzle_input import given_cases
import string

char_values = {
    letter: values for values, letter in (enumerate(string.ascii_letters, start=1))
}

# puzzle 1
sum = 0
for item in given_cases:
    half_point = len(item) // 2
    firstpart, secondpart = map(set, (item[:half_point], item[half_point:]))
    common_letter = firstpart & secondpart
    sum += char_values[common_letter.pop()]

assert sum == 8105
