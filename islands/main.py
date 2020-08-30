import argparse
import sys

from island_finding.file_checking import count_islands


def parse_line(string):
    return [int(c) for c in list(string) if c != '\n']


def log_to_std_error(to_print):
    print(to_print, file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description='Count number of islands for a given file.')
    parser.add_argument("-p", "--path", dest="filepath", help="Input file to be processed")
    args = parser.parse_args()
    filepath = args.filepath
    if not filepath:
        print('A file path to the file with islands should be specified.')
        return
    try:
        with open(filepath, 'r') as f:
            try:
                lines_int = map(parse_line, f)
                res = count_islands(lines_int)
                print(res)
            except ValueError as e:
                log_to_std_error(
                    f'A value error has occurred: "{e}".\n'
                    f'A probable cause is that non-valid characters have been found in the input file.')
    except FileNotFoundError as e:
        log_to_std_error(f'The file {filepath} could not be found.')
        log_to_std_error(e)


if __name__ == "__main__":
    main()
