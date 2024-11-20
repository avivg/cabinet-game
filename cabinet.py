# This script is a solution to the "Cabinet Game" problem.
# The problem is as follows:
# There are N rows of cabinets, each row containing M cabinets.
# K cabinets are selected at random, and have a prize inserted in them.
# Player 1 scans each cabinet row from left to right.
# Player 2 scans each cabinet column from top to bottom.
# The player who finds a prize first wins.
# If both players find a prize in the same step, the game is a draw.
# This script calculates the probability of Player 1 winning the game.

from itertools import combinations


class Game:
    def __init__(self, num_rows: int, cabinets_per_row: int, selection: list[int]):
        self.rows = num_rows
        self.cabinets_per_row = cabinets_per_row
        self.selection = selection

    def __player_one_scan(self) -> list[int]:
        return list(range(1, self.cabinets_per_row * self.rows + 1))

    def __player_two_scan(self) -> list[int]:
        scan = []
        for col in range(1, self.cabinets_per_row + 1):
            scan += list(col + r * self.cabinets_per_row for r in range(self.rows))
        return scan

    def __player_step(self, scan) -> int:
        for idx, cabinet in enumerate(scan):
            if cabinet in self.selection:
                return idx

    def __player_one_step(self) -> int:
        return self.__player_step(self.__player_one_scan())

    def __player_two_step(self) -> int:
        return self.__player_step(self.__player_two_scan())

    PLAYER_ONE_WIN = 1
    PLAYER_TWO_WIN = 2
    DRAW = 0

    def score(self) -> int:
        player_one_score = self.__player_one_step()
        player_two_score = self.__player_two_step()
        if player_one_score < player_two_score:
            return Game.PLAYER_ONE_WIN
        elif player_one_score > player_two_score:
            return Game.PLAYER_TWO_WIN
        else:
            return Game.DRAW

    def __str__(self):
        return f"Selection: {self.selection}, Player 1 finding step: {self.__player_one_step()}, Player 2 finding step: {self.__player_two_step()}"


class GamesGen:
    def __init__(self, num_rows: int, cabinets_per_row: int, num_selections: int):
        self.num_rows = num_rows
        self.cabinets_per_row = cabinets_per_row
        self.num_selections = num_selections

    def __iter__(self):
        num_cabinets = self.num_rows * self.cabinets_per_row
        for selection in combinations(range(1, num_cabinets + 1), self.num_selections):
            yield Game(self.num_rows, self.cabinets_per_row, list(selection))


class ScoreAccumulator:
    def __init__(self):
        self.scores = {Game.PLAYER_ONE_WIN: 0, Game.PLAYER_TWO_WIN: 0, Game.DRAW: 0}
        self.games = 0

    def add(self, score: int):
        self.scores[score] += 1
        self.games += 1

    def __str__(self):
        return f"Player 1 wins: {self.scores[Game.PLAYER_ONE_WIN]}, Player 2 wins: {self.scores[Game.PLAYER_TWO_WIN]}, Draws: {self.scores[Game.DRAW]}"

    def ratio(self, score: int) -> float:
        if self.games == 0:
            return 0.0  # no games means no chance of winning
        return self.scores[score] / self.games


def parse_args():
    import argparse as ap

    parser = ap.ArgumentParser()
    parser.add_argument("num_rows", type=int, help="Number of rows of cabinets")
    parser.add_argument("cabinets_per_row", type=int, help="Number of cabinets per row")
    parser.add_argument(
        "num_selections", type=int, help="Number of cabinets with prizes"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Print verbose output"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    games = GamesGen(args.num_rows, args.cabinets_per_row, args.num_selections)
    scores = ScoreAccumulator()
    for game in games:
        if args.verbose:
            print(game)
        scores.add(game.score())
    print(scores)
    print(f"Player 1 win ratio: {scores.ratio(Game.PLAYER_ONE_WIN)}")
    print(f"Player 2 win ratio: {scores.ratio(Game.PLAYER_TWO_WIN)}")
    print(f"Draw ratio: {scores.ratio(Game.DRAW)}")


if __name__ == "__main__":
    main()
