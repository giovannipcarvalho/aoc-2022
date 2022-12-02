# A, X -- ROCK
# B, Y -- PAPER
# C, Z -- SCISSORS
# scores for selecting what to play
# ROCK     - 1
# PAPER    - 2
# SCISSORS - 3
# scores for game result
# lose = 0
# draw = 3
# win  = 6

points = {
    "rock": 1,  # rock
    "paper": 2,  # paper
    "scissors": 3,  # scissors
    "L": 0,  # lose
    "D": 3,  # draw
    "W": 6,  # win
}

moves = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}


wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
loses = {v: k for k, v in wins.items()}


def outcome(opponent: str, me: str) -> str:
    """
    Returns the outcome of the game
    - L: lose
    - D: draw
    - W: win
    """
    if opponent == me:
        return "D"
    if me in wins[opponent]:
        return "L"
    else:
        return "W"


plays = []
with open("input.txt") as f:
    for line in f.read().splitlines():
        plays.append(line.split(" "))


total_points = 0
for play in plays:
    opponent = moves[play[0]]
    me = moves[play[1]]
    total_points += points[me]
    total_points += points[outcome(opponent, me)]

print("part 1:", total_points)

outcome_mapping = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

total_points = 0
for play in plays:
    opponent = moves[play[0]]

    desired_outcome = outcome_mapping[play[1]]
    if desired_outcome == "win":
        me = loses[opponent]
    elif desired_outcome == "lose":
        me = wins[opponent]
    else:
        me = opponent

    total_points += points[me]
    total_points += points[outcome(opponent, me)]

print("part 2:", total_points)
