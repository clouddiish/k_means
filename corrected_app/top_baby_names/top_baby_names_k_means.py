import random


def get_random_top_baby_names_attribues() -> list:
    random_attributes = []
    random_attributes.append(random.randint(2, 102))  # state
    random_attributes.append(random.choice([50, 100]))  # sex
    random_attributes.append(random.randint(0, 102))  # year
    if random_attributes[1] == 50:
        random_attributes.append(random.randint(1, 56))  # female name
    else:
        random_attributes.append(random.randint(57, 96))  # male name
    random_attributes.append(random.uniform(0.18, 140.0))  # occurences
    return random_attributes
