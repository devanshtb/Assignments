import sys
from utils import to_number, current_timestamp
from processor import (
    remove_invalid,
    square_numbers,
    filter_even,
    sum_numbers
)
from exceptions import InvalidNumberError, NoValidDataError


def main():
    raw_args = sys.argv[1:]

    if not raw_args:
        print("Error: Please provide at least one numeric argument.")
        return

    converted = []
    for value in raw_args:
        try:
            converted.append(to_number(value))
        except InvalidNumberError:
            converted.append(None)

    try:
        valid_numbers = remove_invalid(converted)
        squared = square_numbers(valid_numbers)
        even_squares = filter_even(squared)
        total = sum_numbers(even_squares)

        print(f"[{current_timestamp()}] Total even square sum: {total}")

    except NoValidDataError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
