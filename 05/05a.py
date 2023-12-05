# coding: utf-8

# For this day, we might need regular expressions
import re

testInputFile = "testInput.txt"
inputFile = "input.txt"

with open(inputFile, "r") as inputFile:
    inputFileContents = inputFile.read()
    fileLines = inputFileContents.splitlines()