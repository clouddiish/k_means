import random


def get_random_top_baby_names_attribues() -> list:
    """Generates a random set of attributes for baby names.

    The attributes include:
    - A random state identifier (integer between 2 and 102).
    - A randomly chosen sex identifier (50 for female, 100 for male).
    - A random birth year (integer between 0 and 102).
    - A random name identifier, based on the selected sex.
    - A random number of occurrences (float between 0.18 and 140.0).

    Returns:
        list: A list representing a randomly generated baby name attribute set.
    """
    random_attributes = []
    random_attributes.append(random.randint(2, 102))  # state
    random_attributes.append(random.choice([50, 100]))  # sex
    random_attributes.append(random.randint(0, 102))  # year
    if random_attributes[1] == 50:
        random_attributes.append(random.randint(1, 56))  # female name
    else:
        random_attributes.append(random.randint(57, 96))  # male name
    random_attributes.append(random.uniform(0.18, 140.0))  # occurrences
    return random_attributes


def get_new_top_baby_names_centroid(cluster: list) -> list:
    """Computes the new centroid for a cluster of baby name data points.

    The centroid represents the average characteristics of the cluster.
    It is calculated based on the following attributes:
    - The average state identifier.
    - The dominant gender in the cluster.
    - The average year of birth.
    - The most representative name identifier for the dominant gender.
    - The average occurrences.

    Args:
        cluster (list): A list of data points, where each data point is a list containing:
            - State identifier (int)
            - Sex identifier (int, 50 for female, 100 for male)
            - Year (int)
            - Name identifier (int)
            - Occurrences (float)

    Returns:
        list: A list representing the computed centroid for the given cluster.
    """
    new_centroid = []

    sum_state = 0
    num_fem_name = 0
    num_male_name = 0
    sum_year = 0
    sum_fem_name = 0
    sum_male_name = 0
    sum_occurence = 0

    for row in cluster:
        sum_state += row[0]
        if row[1] == 50:
            num_fem_name += 1
            sum_fem_name += row[3]
        else:
            num_male_name += 1
            sum_male_name += row[3]
        sum_year += row[2]
        sum_occurence += row[4]

    new_centroid.append(sum_state // len(cluster))

    if num_fem_name >= num_male_name:
        new_centroid.append(50)
    else:
        new_centroid.append(100)

    new_centroid.append(sum_year // len(cluster))

    if num_fem_name >= num_male_name:
        new_centroid.append(sum_fem_name // num_fem_name)
    else:
        new_centroid.append(sum_male_name // num_male_name)

    new_centroid.append(sum_occurence / len(cluster))

    return new_centroid
