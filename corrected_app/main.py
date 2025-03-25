from corrected_app.general.k_means import get_euclidean_distance
from corrected_app.top_baby_names.top_baby_names_loop import top_baby_names_loop


def main():
    clusters, centroids = top_baby_names_loop(4, 4, get_euclidean_distance)
    print(f"CLUSTERS: {clusters}")
    print(f"CENTROIDS: {centroids}")


if __name__ == "__main__":
    main()
