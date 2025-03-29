from typing import Callable


def get_cluster_size(cluster: list) -> int:
    return len(cluster)


def get_avg_distance_from_centroid_in_a_cluster(
    cluster: list,
    centroid: list,
    exclude_attributes_ids: list,
    calculate_distance_function: Callable[[list, list, list], list],
) -> float:
    distances_sum = 0
    for datapoint in cluster:
        distance = calculate_distance_function(centroid, datapoint, exclude_attributes_ids)
        distances_sum += distance
    return distances_sum / len(cluster)


def get_max_distance_from_centroid_in_a_cluster(
    cluster: list,
    centroid: list,
    exclude_attributes_ids: list,
    calculate_distance_function: Callable[[list, list, list], list],
) -> float:
    max_distance = 0
    for datapoint in cluster:
        distance = calculate_distance_function(centroid, datapoint, exclude_attributes_ids)
        if distance > max_distance:
            max_distance = distance
    return max_distance
