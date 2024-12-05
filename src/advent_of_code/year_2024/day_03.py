import re

from advent_of_code import DATA_DIR

MUL_PATTERN = re.compile(r"mul\((?P<first>\d{1,3}),(?P<second>\d{1,3})\)")
DO_PATTERN = re.compile(r"do\(\)")
DONT_PATTERN = re.compile(r"don't\(\)")

def load_input() -> str:
    """Load the input data for day 3.

    Returns:
        The input data as a string.
    """
    with open(DATA_DIR / f"day_03.txt") as f:
        return f.read()


def problem_03_a(text: str) -> int:
    """Solve problem 3 (a) from day 3.

    Args:
        text: The input string.

    Returns:
        The solution to the problem.
    """
    solution = 0
    for match in MUL_PATTERN.finditer(text):
        first = int(match.group("first"))
        second = int(match.group("second"))
        solution += first * second
    return solution


def problem_03_b(text: str) -> int:
    """Solve problem 3 (b) from day 3.

    Args:
        text: The input string.

    Returns:
        The solution to the problem.
    """
    mul_matches = [("mul", match) for match in MUL_PATTERN.finditer(text)]
    do_matches = [("do", match) for match in DO_PATTERN.finditer(text)]
    dont_matches = [("dont", match) for match in DONT_PATTERN.finditer(text)]

    matches = sorted(
        mul_matches + do_matches + dont_matches, key=lambda x: x[1].start()
    )

    solution = 0
    do = True
    for match in matches:
        if match[0] == "mul" and do:
            first = int(match[1].group("first"))
            second = int(match[1].group("second"))
            solution += first * second
        elif match[0] == "do":
            do = True
        elif match[0] == "dont":
            do = False
    return solution


if __name__ == "__main__":
    text = load_input()
    solution_03_a = problem_03_a(text)
    solution_03_b = problem_03_b(text)
    print(f"Solution A: {solution_03_a}")
    print(f"Solution B: {solution_03_b}")
