from typing import Callable

from corrected_app.configs.configs import TOP_BABY_NAMES_ABS_FILEPATH
from corrected_app.general.data_processing import fetch_raw_data, normalize_data
from corrected_app.general.k_means import get_random_centroids, get_clusters, get_new_centroids
from corrected_app.top_baby_names.top_baby_names_k_means import (
    get_random_top_baby_names_attribues,
    get_new_top_baby_names_centroid,
)
from corrected_app.top_baby_names.top_baby_names_normalization import top_baby_names_normalize_row
from corrected_app.utils.logger import logger


def top_baby_names_loop(
    no_of_iterations: int, no_of_clusters: int, calculate_distance_function: Callable[[list, list, list], list]
) -> tuple:
    """Runs the k-means clustering algorithm on top baby names dataset.

    This function fetches and normalizes the dataset, initializes random centroids,
    and iteratively updates clusters and centroids using k-means clustering.

    Args:
        no_of_iterations (int): The number of iterations to run the k-means algorithm.
        no_of_clusters (int): The number of clusters to create.
        calculate_distance_function (Callable[[list, list, list], list]): A function that calculates
            distance between two points, excluding specified attributes.

    Returns:
        tuple: Tuple of final clusters and centroids
    """
    raw_data = fetch_raw_data(TOP_BABY_NAMES_ABS_FILEPATH)
    normalized_data = normalize_data(raw_data, top_baby_names_normalize_row)
    centroids = get_random_centroids(no_of_clusters, get_random_top_baby_names_attribues)
    clusters = get_clusters(centroids, normalized_data, [1], calculate_distance_function)

    for i in range(no_of_iterations):
        centroids = get_new_centroids(clusters, get_new_top_baby_names_centroid, get_random_top_baby_names_attribues)
        clusters = get_clusters(centroids, normalized_data, [1], calculate_distance_function)

    return clusters, centroids
