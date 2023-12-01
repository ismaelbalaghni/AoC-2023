# coding: utf-8


input_file = "input.txt"

valid_digits = [str(x) for x in range(10)]
valid_digits.extend(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])

numbers_map = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

input_calibrations = []

with open(input_file, "r") as f:
    for line in f.readlines():
        line_digits = []
        line_calib_value = ""

        # Clean the line (strip newlines characters and convert lettered digits to regular digits)
        clean_line = line.splitlines(keepends=False)[0]

        # Check if any digit is in the text
        for digit in valid_digits:
            try:
                digit_index_first = clean_line.index(digit)
                digit_index_last = clean_line.rindex(digit)
                digit_length_first = digit_index_first+len(digit)
                digit_length_last = digit_index_last+len(digit)
                digit_text_first = clean_line[digit_index_first:digit_length_first]
                digit_text_last = clean_line[digit_index_last:digit_length_last]
                if digit_text_first.isalpha():
                    digit_text_first = numbers_map[digit_text_first]
                if digit_text_last.isalpha():
                    digit_text_last = numbers_map[digit_text_last]
                line_digits.append((digit_index_first, digit_text_first))
                line_digits.append((digit_index_last, digit_text_last))
            except ValueError:
                pass
        line_digits = sorted(line_digits)
        line_calib_value = line_calib_value.join([line_digits[0][1], line_digits[-1][1]])
        if line_calib_value != "":
            input_calibrations.append(int(line_calib_value))
            print(clean_line, line_digits, line_calib_value)

# Compute the sum
input_calibrations_sum = sum(input_calibrations)
print(input_calibrations_sum)
