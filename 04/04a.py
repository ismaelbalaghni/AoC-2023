# coding: utf-8

# For this day, we might need regular expressions
import re

testInputFile = "testInputA.txt"
inputFile = "input.txt"

cardsWinningNumbers = dict()
pointsPileOfScratchcards = 0
totalAmountOfScratchcards = 0

with open(inputFile, "r") as inputFile:
    inputFileContents = inputFile.read()
    fileLines = inputFileContents.splitlines()
    # Go through all lines
    for lineIndex, line in enumerate(fileLines):
        # We use regular expressions to find the numbers in each line
        # It is much easier this way to get the whole number and we
        # check the first and last digit to see if there is any valid
        # characters.
        cardScore = 0
        scoreMultiplier = 1
        regexPattern = r"Card +(\d+)\: {1,2}((?:\d{1,2} {1,})+)\| {1,2}((?:\d{1,2} {0,})+)"
        compiledRegexPattern = re.compile(regexPattern, re.M)
        regexMatch = re.fullmatch(compiledRegexPattern, line)
        cardsWinningNumbers[regexMatch.group(1)] = [int(i.group(0)) for i in re.finditer(r"\d{1,2}", regexMatch.group(2))]
        userNumbers = [int(i.group(0)) for i in re.finditer(r"\d{1,2}", regexMatch.group(3))]
        for userNumber in userNumbers:
            if userNumber in cardsWinningNumbers[regexMatch.group(1)]:
                if cardScore == 0:
                    cardScore += 1
                cardScore *= scoreMultiplier
                scoreMultiplier = 2
        pointsPileOfScratchcards += cardScore

print(pointsPileOfScratchcards)
