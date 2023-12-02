# coding: utf-8

test_input_file = "testInput.txt"
input_file = "input.txt"

MAX_NO_RED_BALLS = 12
MAX_NO_GRN_BALLS = 13
MAX_NO_BLU_BALLS = 14

games = dict()
listOfPossibleGames = list()
sumOfPowerBallsSets = 0

with open(input_file, "r") as inputFile:
    inputFileContents = inputFile.read()
    file_lines = inputFileContents.splitlines()
    for file_line in file_lines:
        game_info = file_line.split(":")  # Separate the game ID from the game sets
        game_sets = game_info[1].strip().split(";")  # Game sets are made of fetches from the bag
        game_id = int(game_info[0].strip().split(" ")[1])

        # Initialize some game statistics like is game possible and the amount
        # of balls from each color total
        maxAmountOfRedBallsInGame = 0
        maxAmountOfGrnBallsInGame = 0
        maxAmountOfBluBallsInGame = 0
        amountOfRedBallsInGame = 0
        amountOfGrnBallsInGame = 0
        amountOfBluBallsInGame = 0
        isGamePossible = True
        # Parse the game sets and compute the statistics for each color
        for set in game_sets:
            for balls in set.split(","):
                balls = balls.strip()
                amountOfBalls = int(balls.split(" ")[0])
                if "red" in balls:
                    amountOfRedBallsInGame += amountOfBalls
                    if amountOfBalls >= maxAmountOfRedBallsInGame:
                        maxAmountOfRedBallsInGame = amountOfBalls
                    if amountOfBalls > MAX_NO_RED_BALLS:
                        isGamePossible = False
                if "blue" in balls:
                    amountOfBluBallsInGame += amountOfBalls
                    if amountOfBalls >= maxAmountOfBluBallsInGame:
                        maxAmountOfBluBallsInGame = amountOfBalls
                    if amountOfBalls > MAX_NO_BLU_BALLS:
                        isGamePossible = False
                if "green" in balls:
                    amountOfGrnBallsInGame += amountOfBalls
                    if amountOfBalls >= maxAmountOfGrnBallsInGame:
                        maxAmountOfGrnBallsInGame = amountOfBalls
                    if amountOfBalls > MAX_NO_GRN_BALLS:
                        isGamePossible = False
        powerBallsSets = maxAmountOfRedBallsInGame * maxAmountOfBluBallsInGame * maxAmountOfGrnBallsInGame
        sumOfPowerBallsSets += powerBallsSets
        if isGamePossible:
            listOfPossibleGames.append(game_id)
        games[game_id] = (isGamePossible, amountOfRedBallsInGame, amountOfGrnBallsInGame, amountOfBluBallsInGame, powerBallsSets, game_sets)

# Compute the sum of the possible games
listOfPossibleGamesSum = sum(listOfPossibleGames)
print(listOfPossibleGamesSum)
print(sumOfPowerBallsSets)
