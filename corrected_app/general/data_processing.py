import csv
from typing import Callable


def fetch_raw_data(filepath: str) -> list:
    raw_data = []
    with open(filepath, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            raw_data.append(row)
    return raw_data


def normalize_data(raw_data: list, normalization_function: Callable[[list, str], list]) -> list:
    normalized_data = []
    for row in raw_data:
        normalized_data.append(normalization_function(row))
    return normalized_data
