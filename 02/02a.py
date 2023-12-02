# coding: utf-8

test_input_file = "testInput.txt"
input_file = "input.txt"

MAX_NO_RED_BALLS = 12
MAX_NO_GRN_BALLS = 13
MAX_NO_BLU_BALLS = 14

listOfPossibleGames = list()

with open(input_file, "r") as inputFile:
    inputFileContents = inputFile.read()
    file_lines = inputFileContents.splitlines()
    for file_line in file_lines:
        game_info = file_line.split(":")  # Separate the game ID from the game sets
        game_sets = game_info[1].strip().split(";")  # Game sets are made of fetches from the bag
        game_id = int(game_info[0].strip().split(" ")[1])

        isGamePossible = True
        # Parse the game sets and compute the statistics for each color
        for set in game_sets:
            for balls in set.split(","):
                balls = balls.strip()
                amountOfBalls = int(balls.split(" ")[0])
                if "red" in balls:
                    if amountOfBalls > MAX_NO_RED_BALLS:
                        isGamePossible = False
                if "blue" in balls:
                    if amountOfBalls > MAX_NO_BLU_BALLS:
                        isGamePossible = False
                if "green" in balls:
                    if amountOfBalls > MAX_NO_GRN_BALLS:
                        isGamePossible = False
        if isGamePossible:
            listOfPossibleGames.append(game_id)

# Compute the sum of the possible games
listOfPossibleGamesSum = sum(listOfPossibleGames)
print(listOfPossibleGamesSum)
