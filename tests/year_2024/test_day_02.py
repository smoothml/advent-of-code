from typing import Generator

import numpy as np
import pytest
from numpy.typing import NDArray

from advent_of_code.year_2024.day_02 import parse_row, problem_02_a, problem_02_b

@pytest.fixture
def fake_data_stream() -> Generator[NDArray[np.int64], None, None]:
    data = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    def stream() -> Generator[str, None, None]:
        for row in data:
            yield np.array(row)
    return stream

def test_parse_row() -> None:
    expected_report = np.array([1, 2, 3, 4, 5])
    report = parse_row("1 2 3 4 5")
    assert np.array_equal(report, expected_report)


def test_day_02_a(fake_data_stream: Generator[NDArray[np.int64], None, None]) -> None:
    expected_solution = 2
    solution = problem_02_a(fake_data_stream)
    assert solution == expected_solution


def test_day_02_b(fake_data_stream: Generator[NDArray[np.int64], None, None]) -> None:
    expected_solution = 4
    solution = problem_02_b(fake_data_stream)
    assert solution == expected_solution
