import random


def get_random_healthcare_noshows_attributes() -> list:
    """Generates a random set of attributes for a healthcare no-show record.

    Returns:
        list: A randomly generated row where:
            - Index 0: Random gender (encoded as 50 or 100).
            - Index 1: Random age between 1 and 99.
            - Index 2: Random neighbourhood index between 1 and 81.
            - Index 3: Random scholarship status (0 or 1).
            - Index 4: Random hypertension status (0 or 1).
            - Index 5: Random diabetes status (0 or 1).
            - Index 6: Random alcoholism status (0 or 1).
            - Index 7: Random handicap status (0 or 1).
            - Index 8: Random SMS received status (0 or 1).
            - Index 9: Random showed up status (0 or 1).
            - Index 10: Random date difference between scheduled day and appointment day (-1 to 98).
    """
    random_attributes = []
    random_attributes.append(random.choice([50, 100]))  # gender
    random_attributes.append(random.randint(1, 99))  # age
    random_attributes.append(random.randint(1, 81))  # neighbourhood
    random_attributes.append(random.choice([0, 1]))  # scholarship
    random_attributes.append(random.choice([0, 1]))  # hipertension
    random_attributes.append(random.choice([0, 1]))  # diabetes
    random_attributes.append(random.choice([0, 1]))  # alcoholism
    random_attributes.append(random.choice([0, 1]))  # handicap
    random_attributes.append(random.choice([0, 1]))  # SMS_received
    random_attributes.append(random.choice([0, 1]))  # showed_up
    random_attributes.append(random.randint(-1, 98))  # date difference between scheduled day and appointment day

    return random_attributes


def get_new_healthcare_noshows_centroid(cluster: list) -> list:
    """Computes the centroid of a cluster of healthcare no-show records.

    Args:
        cluster (list): A list of healthcare no-show records, where each record is a list of attributes.

    Returns:
        list: A centroid row where each index represents the mean value of the corresponding attribute:
            - Index 0: Mean gender value.
            - Index 1: Mean age.
            - Index 2: Mean neighbourhood index.
            - Index 3: Mean scholarship status.
            - Index 4: Mean hypertension status.
            - Index 5: Mean diabetes status.
            - Index 6: Mean alcoholism status.
            - Index 7: Mean handicap status.
            - Index 8: Mean SMS received status.
            - Index 9: Mean showed up status.
            - Index 10: Mean date difference between scheduled day and appointment day.
    """
    new_centroid = []

    sum_gender = 0
    sum_age = 0
    sum_neighbourhood = 0
    sum_scholarship = 0
    sum_hipertension = 0
    sum_diabetes = 0
    sum_alcoholism = 0
    sum_handicap = 0
    sum_sms = 0
    sum_showed = 0
    sum_date_diff = 0

    for row in cluster:
        sum_gender += row[0]
        sum_age += row[1]
        sum_neighbourhood += row[2]
        sum_scholarship += row[3]
        sum_hipertension += row[4]
        sum_diabetes += row[5]
        sum_alcoholism += row[6]
        sum_handicap += row[7]
        sum_sms += row[8]
        sum_showed += row[9]
        sum_date_diff += row[10]

    new_centroid.append(sum_gender / len(cluster))
    new_centroid.append(sum_age / len(cluster))
    new_centroid.append(sum_neighbourhood / len(cluster))
    new_centroid.append(sum_scholarship / len(cluster))
    new_centroid.append(sum_hipertension / len(cluster))
    new_centroid.append(sum_diabetes / len(cluster))
    new_centroid.append(sum_alcoholism / len(cluster))
    new_centroid.append(sum_handicap / len(cluster))
    new_centroid.append(sum_sms / len(cluster))
    new_centroid.append(sum_showed / len(cluster))
    new_centroid.append(sum_date_diff / len(cluster))

    return new_centroid
