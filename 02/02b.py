# coding: utf-8

test_input_file = "testInput.txt"
input_file = "input.txt"

sumOfPowerBallsSets = 0

with open(input_file, "r") as inputFile:
    inputFileContents = inputFile.read()
    file_lines = inputFileContents.splitlines()
    for file_line in file_lines:
        game_info = file_line.split(":")  # Separate the game ID from the game sets
        game_sets = game_info[1].strip().split(";")  # Game sets are made of fetches from the bag

        # Initialize some game statistics like is game possible and the amount
        # of balls from each color total
        maxAmountOfRedBallsInGame = 0
        maxAmountOfGrnBallsInGame = 0
        maxAmountOfBluBallsInGame = 0
        # Parse the game sets and compute the statistics for each color
        for set in game_sets:
            for balls in set.split(","):
                balls = balls.strip()
                amountOfBalls = int(balls.split(" ")[0])
                if "red" in balls:
                    if amountOfBalls >= maxAmountOfRedBallsInGame:
                        maxAmountOfRedBallsInGame = amountOfBalls
                if "blue" in balls:
                    if amountOfBalls >= maxAmountOfBluBallsInGame:
                        maxAmountOfBluBallsInGame = amountOfBalls
                if "green" in balls:
                    if amountOfBalls >= maxAmountOfGrnBallsInGame:
                        maxAmountOfGrnBallsInGame = amountOfBalls
        powerBallsSets = maxAmountOfRedBallsInGame * maxAmountOfBluBallsInGame * maxAmountOfGrnBallsInGame
        sumOfPowerBallsSets += powerBallsSets

# Compute the sum of the power of balls set
print(sumOfPowerBallsSets)
