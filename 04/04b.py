# coding: utf-8

# For this day, we might need regular expressions
import re

testInputFile = "testInputB.txt"
inputFile = "input.txt"

cards = dict()

with open(inputFile, "r") as inputFile:
    inputFileContents = inputFile.read()
    fileLines = inputFileContents.splitlines()
    totalAmountOfScratchCards = 0
    # Go through all lines
    for line in fileLines:
        # We use regular expressions to find the numbers in each line
        # It is much easier this way to get the whole number and we
        # check the first and last digit to see if there is any valid
        # characters.
        amountOfWinningNumbers = 0
        regexPattern = r"Card +(\d+)\: {1,2}((?:\d{1,2} {1,})+)\| {1,2}((?:\d{1,2} {0,})+)"
        regexMatch = re.fullmatch(regexPattern, line)
        cardsWinningNumbers = [int(i.group(0)) for i in re.finditer(r"\d{1,2}", regexMatch.group(2))]
        userNumbers = [int(i.group(0)) for i in re.finditer(r"\d{1,2}", regexMatch.group(3))]
        for userNumber in userNumbers:
            if userNumber in cardsWinningNumbers:
                amountOfWinningNumbers += 1
        cards[int(regexMatch.group(1))] = (1, amountOfWinningNumbers)
    for card in cards.keys():
        # Make copies of the other cards
        for i in range(cards[card][0]):
            for j in range(cards[card][1]):
                cards[card+j+1] = (cards[card+j+1][0]+1, cards[card+j+1][1])
    for cardIndex, card in enumerate(cards.keys()):
        # Get total amount of cards
        totalAmountOfScratchCards += cards[card][0]
print(totalAmountOfScratchCards)
