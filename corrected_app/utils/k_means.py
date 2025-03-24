import math
from typing import Callable


def get_random_centroids(how_many: int, randomizer_function: Callable[[], list]) -> list:
    return [randomizer_function() for _ in range(how_many)]


def get_euclidean_distance(first_point: list, second_point: list, exclude_attributes_ids: list) -> float:
    total = 0
    for i in range(0, len(first_point)):
        if i not in exclude_attributes_ids:
            total += (first_point[i] - second_point[i]) ** 2
    return math.sqrt(total)


def get_closest_centroid_id(centroids: list, datapoint: list, exclude_attributes_ids: list) -> int:
    min_distance = 1e100
    min_index = -1
    for i, centroid in enumerate(centroids):
        next = get_euclidean_distance(centroid, datapoint, exclude_attributes_ids)
        if next < min_distance:
            min_distance = next
            min_index = i
    return min_index


def get_clusters(centroids: list, datapoints: list, exclude_attributes_ids: list) -> list:
    clusters = [[] for _ in centroids]

    for datapoint in datapoints:
        closest_centroid_id = get_closest_centroid_id(centroids, datapoint, exclude_attributes_ids)
        clusters[closest_centroid_id].append(datapoint)

    return clusters
