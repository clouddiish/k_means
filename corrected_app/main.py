from corrected_app.top_baby_names.top_baby_names_k_means import get_random_top_baby_names_attribues
from corrected_app.top_baby_names.top_baby_names_normalization import top_baby_names_normalize_row
from corrected_app.utils.data_processing import fetch_raw_data, normalize_data
from corrected_app.utils.k_means import get_random_centroids, get_clusters

data = normalize_data(fetch_raw_data("./raw_data/top_baby_names_by_state_midi.txt"), top_baby_names_normalize_row)

initial_centroids = get_random_centroids(4, get_random_top_baby_names_attribues)
clusters = get_clusters(initial_centroids, data, [])

print(clusters)
