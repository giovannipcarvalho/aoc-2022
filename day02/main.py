points = {
    "rock": 1,  # rock
    "paper": 2,  # paper
    "scissors": 3,  # scissors
    "L": 0,  # lose
    "D": 3,  # draw
    "W": 6,  # win
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


def parse_input(s: str) -> list[list[str]]:
    """
    Reads input string and returns a list of move pairs such as ['A', 'X']
    """
    plays = []
    for line in s.splitlines():
        plays.append(line.split(" "))
    return plays


def decode_move(move: str) -> str:
    """Decodes the opponent move"""
    moves = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
    }
    return moves[move]


def score_game(game: list[tuple[str, str]]) -> int:
    """Scores the game playing from my perspective"""
    total_points = 0
    for move in game:
        opponent, me = move
        total_points += points[me]
        total_points += points[outcome(opponent, me)]
    return total_points


def reply_move(code: str) -> str:
    """Decodes the assumed move to be replied"""
    replies = {
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }
    return replies[code]


def reply_outcome(opponent_move: str, desired_outcome_code: str) -> str:
    """
    Replies the move that guarantees the desired outcome according to
    `opponent_move` and `desired_outcome_code`.
    """
    outcome_mapping = {
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }
    desired_outcome = outcome_mapping[desired_outcome_code]
    opponent_move = decode_move(opponent_move)

    if desired_outcome == "win":
        return loses[opponent_move]
    elif desired_outcome == "lose":
        return wins[opponent_move]
    else:
        return opponent_move


if __name__ == "__main__":
    s = parse_input(open("input.txt").read())
    game1 = [(decode_move(m0), reply_move(m1)) for m0, m1 in s]
    print("part 1:", score_game(game1))

    game2 = [(decode_move(m0), reply_outcome(m0, m1)) for m0, m1 in s]
    print("part 2:", score_game(game2))
