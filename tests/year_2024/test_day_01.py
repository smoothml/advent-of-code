import numpy as np
import pytest
from numpy.typing import NDArray

from advent_of_code.year_2024.day_01 import problem_01_a, problem_01_b


@pytest.fixture
def data() -> NDArray[np.int64]:
    return np.array(
        [
            [3, 4],
            [4, 3],
            [2, 5],
            [1, 3],
            [3, 9],
            [3, 3],
        ]
    )


def test_day_01_a(data: NDArray[np.int64]) -> None:
    """Test the solution to problem 1 (a) from day 1.
    
    Args:
        data: The test input data.
    """
    expected_solution = 11
    solution = problem_01_a(data)
    assert solution == expected_solution


def test_day_01_b(data: NDArray[np.int64]) -> None:
    """Test the solution to problem 1 (b) from day 1.
    
    Args:
        data: The test input data.
    """
    expected_solution = 31
    solution = problem_01_b(data)
    assert solution == expected_solution
