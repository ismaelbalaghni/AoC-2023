# coding: utf-8

import os
import re

testInputFile = f"{os.path.dirname(__file__)}{os.path.sep}testInput.txt"
inputFile = f"{os.path.dirname(__file__)}{os.path.sep}input.txt"

fileContents = ""
fileLines = list()
hashTotals = list()
lightBoxes = dict()
for i in range(256):
    lightBoxes[i] = dict()


with open(inputFile, mode="r", encoding="utf-8") as file:
    fileContents = file.read()
    fileLines = fileContents.splitlines()

print("##################################################################")

for line in fileLines:
    instructions = line.split(",")
    for instruction in instructions:
        splitInstruction = re.split('(-|=)', instruction)
        instructionHash = 0
        for instructionChar in splitInstruction[0]:
            instructionHash += ord(instructionChar)
            instructionHash *= 17
            instructionHash %= 256
        print(instruction, instructionHash)
        if splitInstruction[1] == "-":
            if splitInstruction[0] in lightBoxes[instructionHash]:
                lightBoxes.popitem()
        elif splitInstruction[1] == "=":
            lightBoxes[instructionHash][splitInstruction[0]] = splitInstruction[2]
        hashTotals.append(instructionHash)

print(lightBoxes)
