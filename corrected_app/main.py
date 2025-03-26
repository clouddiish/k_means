from corrected_app.general.distance_calculation import get_euclidean_distance, get_manhattan_distance
from corrected_app.top_baby_names.top_baby_names_loop import top_baby_names_loop


def main():
    clusters, centroids = top_baby_names_loop(
        no_of_iterations=4, no_of_clusters=10, calculate_distance_function=get_euclidean_distance
    )
    print(f"FINAL CLUSTERS:")
    for i, cluster in enumerate(clusters):
        print(f"CLUSTER NO {i}")
        print(cluster)
    print(f"FINAL CENTROIDS: {centroids}")


if __name__ == "__main__":
    main()
