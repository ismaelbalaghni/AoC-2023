# coding: utf-8

# For this day, we might need regular expressions
import re

testInputFile = "testInput.txt"
inputFile = "input.txt"

validPartNumbers = list()
invalidPartNumbers = list()

forbiddenChars = [str(n) for n in range(10)]
forbiddenChars.append(".")
forbiddenChars.append("")

with open(testInputFile, "r") as inputFile:
    inputFileContents = inputFile.read()
    fileLines = inputFileContents.splitlines()
    # Go through all lines
    for lineIndex, line in enumerate(fileLines):
        # We use regular expressions to find the numbers in each line
        # It is much easier this way to get the whole number and we
        # check the first and last digit to see if there is any valid
        # characters.
        potentialPartNumbersIterator = re.finditer(r"\d+", line)
        if lineIndex == 0:
            print(line)
            for potentialPartNumber in potentialPartNumbersIterator:
                # Check for the first digit
                # We're at first line
                matchN = ""
                matchNE = ""
                matchE = ""
                matchSE = ""
                matchS = ""
                matchSW = ""
                matchW = ""
                matchNW = ""
                if potentialPartNumber.start() == 0:
                    # We're at first column
                    matchS = fileLines[lineIndex+1][potentialPartNumber.start()]
                    matchSE = fileLines[lineIndex+1][potentialPartNumber.start()+1]
                else:
                    matchW = fileLines[lineIndex][potentialPartNumber.start()-1]
                    matchSW = fileLines[lineIndex+1][potentialPartNumber.start()-1]
                    matchS = fileLines[lineIndex+1][potentialPartNumber.start()]
                    matchSE = fileLines[lineIndex+1][potentialPartNumber.start()+1]
                if potentialPartNumber.end() == len(line)-1:
                    # We're at last column
                    matchS = fileLines[lineIndex+1][potentialPartNumber.end()]
                    matchSW = fileLines[lineIndex+1][potentialPartNumber.end()-1]
                else:
                    matchSW = fileLines[lineIndex+1][potentialPartNumber.end()+1]
                    matchS = fileLines[lineIndex+1][potentialPartNumber.end()]
                    matchSE = fileLines[lineIndex+1][potentialPartNumber.end()+1]
                    matchE = fileLines[lineIndex][potentialPartNumber.end()+1]
                print(potentialPartNumber[0], matchN, matchNE, matchE, matchSE, matchS, matchSW, matchW, matchNW)
        elif lineIndex == len(fileLines) - 1:
            print(line)
            for potentialPartNumber in potentialPartNumbersIterator:
                # We're at last line
                matchN = ""
                matchNE = ""
                matchE = ""
                matchSE = ""
                matchS = ""
                matchSW = ""
                matchW = ""
                matchNW = ""
                if potentialPartNumber.start() == 0:
                    # We're at first column
                    matchN = fileLines[lineIndex-1][potentialPartNumber.start()]
                    matchNE = fileLines[lineIndex-1][potentialPartNumber.start()+1]
                else:
                    matchNW = fileLines[lineIndex-1][potentialPartNumber.start()-1]
                    matchN = fileLines[lineIndex-1][potentialPartNumber.start()]
                    matchNE = fileLines[lineIndex-1][potentialPartNumber.start()+1]
                if potentialPartNumber.end() == len(line)-1:
                    # We're at last column
                    matchNW = fileLines[lineIndex-1][potentialPartNumber.start()-1]
                    matchN = fileLines[lineIndex-1][potentialPartNumber.start()]
                else:
                    matchNW = fileLines[lineIndex-1][potentialPartNumber.start()-1]
                    matchN = fileLines[lineIndex-1][potentialPartNumber.start()]
                    matchNE = fileLines[lineIndex-1][potentialPartNumber.start()+1]
                print(potentialPartNumber[0], matchN, matchNE, matchE, matchSE, matchS, matchSW, matchW, matchNW)
        else:
            # We're in the middle
            for potentialPartNumber in potentialPartNumbersIterator:
                # We're at last line
                matchN = ""
                matchNE = ""
                matchE = ""
                matchSE = ""
                matchS = ""
                matchSW = ""
                matchW = ""
                matchNW = ""
                if potentialPartNumber.start() == 0:
                    # We're at first column
                    pass
                if potentialPartNumber.end() == len(line)-1:
                    # We're at last column
                    pass
                print(potentialPartNumber[0], matchN, matchNE, matchE, matchSE, matchS, matchSW, matchW, matchNW)

# Compute the sum of the valid part numbers
partNumbersSum = sum(validPartNumbers)
print(partNumbersSum)