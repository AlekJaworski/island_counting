import pytest

from islands.island_finding.line_checking import check_consecutive_lines


def test_should_return_correct_counter_value_for_slant_edges():
    line_top = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    line_bot = [0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, -2, -2, -2, 0, 0, 0, 0, 0, 0, 0, 0]
    result = check_consecutive_lines(line_top, line_bot)
    result_backward = check_consecutive_lines(line_bot, line_top)
    assert result[0] == 0
    assert result_backward[0] == -1


def test_should_return_correct_counter_value_for_vertical_edges():
    line_top = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    line_bot = [0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, -2, -2, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    result = check_consecutive_lines(line_top, line_bot)
    result_backward = check_consecutive_lines(line_bot, line_top)
    assert result[0] == 0
    assert result_backward[0] == -1


@pytest.mark.parametrize("length_parameter", [
    10, 30, 50, 100, 1000,
])
def test_should_return_correct_counter_value_for_a_wave_pattern(length_parameter):
    length_param = 10
    length = length_param * 2

    linetop = [i % 2 for i in range(length)]
    linebot = [-(i + 1) * ((i + 1) % 2) for i in range(length)]

    counter, colours = check_consecutive_lines(linetop, linebot)
    counter_bwd, colours_bwd = check_consecutive_lines(linebot, linetop)
    assert counter == 0
    assert counter_bwd == -(length_param - 1)
