import csv
from typing import Callable


def fetch_raw_data(filepath: str) -> list:
    """Reads a CSV file and returns its content as a list of rows.

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        list: A list of rows, where each row is represented as a list of strings.
    """
    raw_data = []
    with open(filepath, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            raw_data.append(row)
    return raw_data


def normalize_data(raw_data: list, normalization_function: Callable[[list], list]) -> list:
    """Applies a normalization function to each row in the raw data.

    Args:
        raw_data (list): A list of rows, where each row is a list of strings.
        normalization_function (Callable[[list], list]): A function that takes a row and returns a normalized row.

    Returns:
        list: A list of normalized rows.
    """
    normalized_data = []
    for row in raw_data:
        normalized_data.append(normalization_function(row))
    return normalized_data
