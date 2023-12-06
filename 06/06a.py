# coding: utf-8

# For this day, we might need regular expressions
import re

testInputFile = "testInput.txt"
inputFile = "input.txt"

boatRaceTimes = list()
boatRaceDistances = list()
boatRaces = dict()

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
boatRaceTimes.extend([int(i) for i in matchedTimes])

# Get the distances
matchedDistanceString = re.fullmatch(regexPattern, fileLines[1], re.M)
matchedDistances = re.findall(r"(\d+)", matchedDistanceString.group(2))
boatRaceDistances.extend([int(i) for i in matchedDistances])

# Make the dict
for race, time, distance in zip(range(len(boatRaceTimes)), boatRaceTimes, boatRaceDistances):
    boatRaces[race+1] = (time, distance)

# Go through each race
numberOfWinnableTimes = 0
for race, raceInfo in boatRaces.items():
    print(race, raceInfo)
    raceCombinations = 0
    for milli in range(raceInfo[0]+1):
        timePressed = milli
        speed = milli
        timeRemaining = max(range(raceInfo[0]+1)) - timePressed
        distanceRun = speed*timeRemaining
        print("\t", "button pressed for", timePressed, "ms time remaining for the race", timeRemaining, "ms distance run by the boat", distanceRun, "mm")
        if distanceRun > raceInfo[1]:
            if numberOfWinnableTimes == 0:
                numberOfWinnableTimes += 1
            raceCombinations += 1
    numberOfWinnableTimes *= raceCombinations
    boatRaces[race] = (raceInfo[0], raceInfo[1], raceCombinations)

print(boatRaces)
print("Number of winnable times: ", numberOfWinnableTimes)