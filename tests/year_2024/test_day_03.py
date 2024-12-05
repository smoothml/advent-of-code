from advent_of_code.year_2024.day_03 import problem_03_a, problem_03_b


def test_day_03_a() -> None:
    """Test for problem 3 (a) from day 3."""
    text = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    expected_solution = 161
    solution = problem_03_a(text)
    assert solution == expected_solution


def test_day_03_b() -> None:
    """Test for problem 3 (b) from day 3."""
    text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    expected_solution = 48
    solution = problem_03_b(text)
    assert solution == expected_solution
