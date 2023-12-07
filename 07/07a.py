# coding: utf-8

# For this day, we might need regular expressions
import re
from collections import Counter
from operator import itemgetter

def card_sorter(a):
    return a[3], a[0]

testInputFile = "testInput.txt"
inputFile = "input.txt"

cardStack = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
cardTypes = [range(1, 7)]

cards = list()
cardsRanked = list()

inputFileContents = ""
fileLines = ""

regexPattern = r"([A-Z0-9]{5})\ (\d+)"

# Parse the file to grab its contents
with open(testInputFile, "r", encoding="utf-8") as inputFile:
    inputFileContents = inputFile.read()
    fileLines = inputFileContents.splitlines()

# Make the dict of cards given
for handMatch in re.finditer(regexPattern, inputFileContents):
    cards.append((handMatch.group(1), int(handMatch.group(2))))

# For each hand, compute its type
for handIndex, hand in enumerate(cards):
    cardOccurrences = Counter(hand[0])
    cardOccurencesValues = Counter(cardOccurrences.values())
    handType = 1
    if max(cardOccurencesValues) == 5:
        handType = 7
    elif max(cardOccurencesValues) == 4:
        handType = 6
    elif max(cardOccurencesValues) == 3 and cardOccurencesValues[2] == 1:
        handType = 5
    elif max(cardOccurencesValues) == 3 and cardOccurencesValues[1] == 2:
        handType = 4
    elif cardOccurencesValues[max(cardOccurencesValues)] == 2:
        handType = 3
    elif max(cardOccurencesValues) == 2 and cardOccurencesValues[1] == 2:
        handType = 2
    cards[handIndex] = (cards[handIndex][0],cards[handIndex][1],handIndex,handType)
cards.sort(key=card_sorter)
# Go through each hand and rank them based on their type
for cardIndex, card in enumerate(cards):
    if card[3] == cards[cardIndex-1][3] or card[3] == cards[cardIndex+1][3]:
        if card[0]
        print(card, cards[cardIndex-1])

