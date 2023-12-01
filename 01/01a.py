# coding: utf-8

input_file = "input.txt"

input_calibrations = []

# Get line input calibration values

with open(input_file, "r") as f:
    for line in f.readlines():
        line_digits = []
        line_calib_value = ""
        for line_char in line:
            if line_char.isdigit():
                line_digits.append(line_char)
        line_calib_value = line_calib_value.join([line_digits[0], line_digits[-1]])
        if line_calib_value != "":
            input_calibrations.append(int(line_calib_value))

# Compute sum
calibration_values_sum = sum(input_calibrations)
print(calibration_values_sum)