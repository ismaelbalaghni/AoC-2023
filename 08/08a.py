# coding: utf-8

import re

fileContents = ""
fileLines = list()

testInput1 = "testInputA1.txt"
testInput2 = "testInputA2.txt"
inputFile = "input.txt"
pathMap = dict()
startPoint = "AAA"
endPoint = "ZZZ"
steps = 0
directionMap = {
    "L": 0,
    "R": 1
}

with open(inputFile, "r", encoding="utf-8") as file:
    fileContents = file.read()
    fileLines.extend(fileContents.splitlines())

inputsRegex = r"^((?:[A-Z])+)$"
inputs = re.match(inputsRegex, fileContents, re.M).group(0)

pathsRegex = r"^([A-Z]{3})\ \=\ \(([A-Z]{3})\,\ ([A-Z]{3})\)$"
for regexMatch in re.finditer(pathsRegex, fileContents, re.M):
    pathMap[regexMatch.group(1)] = (regexMatch.group(2), regexMatch.group(3))

currentKey = startPoint
inputPos = 0

while currentKey != endPoint:
    currentKey = pathMap[currentKey][directionMap[inputs[inputPos]]]
    inputPos += 1
    if inputPos == len(inputs):
        inputPos = 0
    steps += 1

print(steps)