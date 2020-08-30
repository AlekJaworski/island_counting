from island_finding.file_checking import count_islands


def vertical_lines(vertical_dimension, horizontal_dimension):
    yield [1 for i in range(horizontal_dimension)]
    yield from ([i % 2 for i in range(horizontal_dimension)] for _ in range(vertical_dimension))


def test_long_vertical_line_file():
    res = count_islands(vertical_lines(100, 100))
    assert res == 1
