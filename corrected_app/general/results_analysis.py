from typing import Callable


def get_cluster_size(cluster: list) -> int:
    """Gets the size of a cluster.

    Args:
        cluster (list): A list of data points representing a cluster.

    Returns:
        int: The number of data points in the cluster.
    """
    return len(cluster)


def get_avg_distance_from_centroid_in_a_cluster(
    cluster: list,
    centroid: list,
    exclude_attributes_ids: list,
    calculate_distance_function: Callable[[list, list, list], list],
) -> float:
    """Calculates the average distance of all data points in a cluster from its centroid.

    Args:
        cluster (list): A list of data points in the cluster.
        centroid (list): The centroid of the cluster.
        exclude_attributes_ids (list): A list of attribute indices to exclude from the distance calculation.
        calculate_distance_function (Callable[[list, list, list], list]): A function to compute the distance
            between a data point and the centroid, while excluding specified attributes.

    Returns:
        float: The average distance of data points from the centroid.
    """
    if not cluster:
        return 0.0
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
    """Finds the maximum distance of any data point in a cluster from its centroid.

    Args:
        cluster (list): A list of data points in the cluster.
        centroid (list): The centroid of the cluster.
        exclude_attributes_ids (list): A list of attribute indices to exclude from the distance calculation.
        calculate_distance_function (Callable[[list, list, list], list]): A function to compute the distance
            between a data point and the centroid, while excluding specified attributes.

    Returns:
        float: The maximum distance of a data point from the centroid.
    """
    max_distance = 0
    for datapoint in cluster:
        distance = calculate_distance_function(centroid, datapoint, exclude_attributes_ids)
        if distance > max_distance:
            max_distance = distance
    return max_distance
