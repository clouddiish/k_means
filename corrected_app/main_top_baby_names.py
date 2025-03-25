from corrected_app.general.data_processing import fetch_raw_data, normalize_data
from corrected_app.general.k_means import get_random_centroids, get_clusters, get_new_centroids
from corrected_app.top_baby_names.top_baby_names_k_means import (
    get_random_top_baby_names_attribues,
    get_new_top_baby_names_centroid,
)
from corrected_app.top_baby_names.top_baby_names_normalization import top_baby_names_normalize_row
from corrected_app.utils.logger import logger


def main(no_of_iterations: int, no_of_clusters: int) -> None:
    raw_data = fetch_raw_data("./raw_data/top_baby_names_by_state_midi.txt")
    normalized_data = normalize_data(raw_data, top_baby_names_normalize_row)
    centroids = get_random_centroids(no_of_clusters, get_random_top_baby_names_attribues)
    clusters = get_clusters(centroids, normalized_data, [1])

    for i in range(no_of_iterations):
        centroids = get_new_centroids(clusters, get_new_top_baby_names_centroid, get_random_top_baby_names_attribues)
        logger.debug(f"Centroids: {centroids}")
        clusters = get_clusters(centroids, normalized_data, [1])


main(4, 4)
