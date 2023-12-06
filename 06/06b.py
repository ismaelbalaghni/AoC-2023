# coding: utf-8

# For this day, we might need regular expressions
import re

testInputFile = "testInput.txt"
inputFile = "input.txt"

boatRaceTime = 0
boatRaceDistance = 0
boatRace = tuple()

inputFileContents = ""
fileLines = ""

regexPattern = r"(Time|Distance)\:\s+(.+)"

# Parse the file to grab its contents
with open(inputFile, "r", encoding="utf-8") as inputFile:
    inputFileContents = inputFile.read()
    fileLines = inputFileContents.splitlines()

# Get the times
matchedTimeString = re.fullmatch(regexPattern, fileLines[0], re.M)
matchedTimes = re.findall(r"(\d+)", matchedTimeString.group(2))
boatRaceTime = int("".join(matchedTimes))

# Get the distances
matchedDistanceString = re.fullmatch(regexPattern, fileLines[1], re.M)
matchedDistances = re.findall(r"(\d+)", matchedDistanceString.group(2))
boatRaceDistance = int("".join(matchedDistances))

# Make the tuple
boatRace = (boatRaceTime, boatRaceDistance)

# Go through each race
numberOfWinnableTimes = 0
for milli in range(boatRace[0]+1):
    timePressed = milli
    speed = milli
    timeRemaining = (boatRace[0]+1) - timePressed
    distanceRun = speed*timeRemaining
    if distanceRun > boatRace[1]:
        numberOfWinnableTimes += 1

print("Number of winnable times: ", numberOfWinnableTimes)
