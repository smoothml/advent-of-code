from typing import Generator

import numpy as np
from numpy.typing import NDArray

from advent_of_code import DATA_DIR


def parse_row(report: str) -> NDArray[np.int64]:
    """Parse a report from the input data.

    Args:
        report: The report to parse.

    Returns:
        The parsed report.
    """
    return np.array([int(level) for level in report.strip().split()])


def data_stream() -> Generator[NDArray[np.int64], None, None]:
    """Return a stream of parsed reports from the data file.

    Yields:
        A parsed report from the data file.
    """
    def stream() -> Generator[NDArray[np.int64], None, None]:
        with open(DATA_DIR / "day_02.txt") as f:
            for report in f:
                yield parse_row(report)
    return stream


def is_safe(report: NDArray[np.int64]) -> bool:
    """Determine whether a report is safe.

    Args:
        report: The report to check.

    Returns:
        Whether the report is safe.
    """
    diffs = np.diff(report)
    return (
        np.all(np.abs(diffs) >= 1)
        and np.all(np.abs(diffs) <= 3)
        and (np.all(diffs >= 0) or np.all(diffs <= 0))
    )


def problem_02_a(stream: Generator[str, None, None]) -> int:
    """Solve problem 2 (a) from day 2.

    Args:
        stream: The input data stream.

    Returns:
        The solution to the problem.
    """
    safe_count = 0
    for report in stream():
        if is_safe(report):
            safe_count += 1
    return safe_count


def problem_02_b(stream: Generator[str, None, None]) -> int:
    """Solve problem 2 (b) from day 2.

    Args:
        stream: The input data stream.

    Returns:
        The solution to the problem.
    """
    safe_count = 0
    for report in stream():
        if is_safe(report):
            safe_count += 1
        else:
            if any(
                is_safe(np.concatenate((report[:idx], report[idx+1:])))
                for idx in range(report.size)
            ):
                safe_count += 1
    return safe_count


if __name__ == "__main__":
    stream = data_stream()
    solution_02_a = problem_02_a(stream)
    solution_02_b = problem_02_b(stream)
    print(f"Solution A: {solution_02_a}")
    print(f"Solution B: {solution_02_b}")
