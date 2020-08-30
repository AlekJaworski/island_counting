from typing import Iterable

from island_finding.line_checking import check_consecutive_lines


def count_islands(lines):
    transformed_lines = map(initialize_colours, lines)
    line1 = next(lines)
    line0 = [0 for _ in line1]
    res, line1 = check_consecutive_lines(line0, line1)
    for i, line in enumerate(transformed_lines):
        count, line1 = check_consecutive_lines(line1, line)
        res += count
    return res


def initialize_colours(iterable: Iterable[int]):
    temp_colour = 0
    res = []
    x_prev = 0
    for x in iterable:
        if x_prev == 0 and x == 1:
            temp_colour += 1
        if x == 0:
            res.append(0)
        else:
            res.append(temp_colour)
        x_prev = x
    return res
