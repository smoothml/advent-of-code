from collections import Counter
from functools import reduce

import numpy as np
from numpy.typing import NDArray

from advent_of_code import DATA_DIR


def load_input() -> NDArray[np.int64]:
    """Load the input data for day 1.

    Returns:
        The input data as a NumPy array.
    """
    with open(DATA_DIR / f"day_01.txt") as f:
        return np.array(
            [tuple(int(val) for val in line.strip().split()) for line in f]
        )


def problem_01_a(data: NDArray[np.int64]) -> int:
    """Solve problem 1 (a) from day 1.

    Args:
        data: The input data.

    Returns:
        The solution to the problem.
    """
    for idx in range(data.shape[1]):
        data[:, idx].sort()
    
    return int(np.sum(np.abs(np.diff(data))))


def problem_01_b(data: NDArray[np.int64]) -> int:
    """Solve problem 1 (b) from day 1.

    Args:
        data: The input data.

    Returns:
        The solution to the problem.
    """
    left_counter = Counter(data[:, 0])
    right_counter = Counter(data[:, 1])
    return int(
        sum(count * num * right_counter[num] for num, count in left_counter.items())
    )


if __name__ == "__main__":
    data = load_input()
    solution_01_a = problem_01_a(data)
    solution_01_b = problem_01_b(data)
    print(f"Soultion A: {solution_01_a:}")
    print(f"Soultion B: {solution_01_b:}")
