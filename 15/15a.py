# coding: utf-8

testInputFile = "testInput.txt"
inputFile = "input.txt"

fileContents = ""
fileLines = list()
hashTotals = list()


with open(testInputFile, mode="r", encoding="utf-8") as file:
    fileContents = file.read()
    fileLines = fileContents.splitlines()

for line in fileLines:
    instructions = line.split(",")
    for instruction in instructions:
        instructionHash = 0
        for instructionChar in instruction:
            instructionHash += ord(instructionChar)
            instructionHash *= 17
            instructionHash %= 256
        hashTotals.append(instructionHash)

print(hashTotals)
print(sum(hashTotals))