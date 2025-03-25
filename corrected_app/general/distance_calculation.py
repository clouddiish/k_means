import math


def get_euclidean_distance(first_point: list, second_point: list, exclude_attributes_ids: list) -> float:
    """Calculates the Euclidean distance between two points, excluding specified attributes.

    Args:
        first_point (list): The first data point.
        second_point (list): The second data point.
        exclude_attributes_ids (list): Indices of attributes to be excluded from the calculation.

    Returns:
        float: The Euclidean distance between the two points.
    """
    total = 0
    for i in range(len(first_point)):
        if i not in exclude_attributes_ids:
            total += (first_point[i] - second_point[i]) ** 2
    return math.sqrt(total)


def get_manhattan_distance(first_point: list, second_point: list, exclude_attributes_ids: list) -> float:
    """Calculates the Manhattan distance between two points, excluding specified attributes.

    Args:
        first_point (list): The first data point.
        second_point (list): The second data point.
        exclude_attributes_ids (list): Indices of attributes to be excluded from the calculation.

    Returns:
        float: The Manhattan distance between the two points.
    """
    total = 0
    for i in range(len(first_point)):
        if i not in exclude_attributes_ids:
            total += abs(first_point[i] - second_point[i])
    return total
