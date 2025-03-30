neighbourhoods = {
    "AEROPORTO": 1,
    "ANDORINHAS": 2,
    "ANTÔNIO HONÓRIO": 3,
    "ARIOVALDO FAVALESSA": 4,
    "BARRO VERMELHO": 5,
    "BELA VISTA": 6,
    "BENTO FERREIRA": 7,
    "BOA VISTA": 8,
    "BONFIM": 9,
    "CARATOÍRA": 10,
    "CENTRO": 11,
    "COMDUSA": 12,
    "CONQUISTA": 13,
    "CONSOLAÇÃO": 14,
    "CRUZAMENTO": 15,
    "DA PENHA": 16,
    "DE LOURDES": 17,
    "DO CABRAL": 18,
    "DO MOSCOSO": 19,
    "DO QUADRO": 20,
    "ENSEADA DO SUÁ": 21,
    "ESTRELINHA": 22,
    "FONTE GRANDE": 23,
    "FORTE SÃO JOÃO": 24,
    "FRADINHOS": 25,
    "GOIABEIRAS": 26,
    "GRANDE VITÓRIA": 27,
    "GURIGICA": 28,
    "HORTO": 29,
    "ILHA DAS CAIEIRAS": 30,
    "ILHA DE SANTA MARIA": 31,
    "ILHA DO BOI": 32,
    "ILHA DO FRADE": 33,
    "ILHA DO PRÍNCIPE": 34,
    "ILHAS OCEÂNICAS DE TRINDADE": 35,
    "INHANGUETÁ": 36,
    "ITARARÉ": 37,
    "JABOUR": 38,
    "JARDIM CAMBURI": 39,
    "JARDIM DA PENHA": 40,
    "JESUS DE NAZARETH": 41,
    "JOANA D´ARC": 42,
    "JUCUTUQUARA": 43,
    "MARIA ORTIZ": 44,
    "MARUÍPE": 45,
    "MATA DA PRAIA": 46,
    "MONTE BELO": 47,
    "MORADA DE CAMBURI": 48,
    "MÁRIO CYPRESTE": 49,
    "NAZARETH": 50,
    "NOVA PALESTINA": 51,
    "PARQUE INDUSTRIAL": 52,
    "PARQUE MOSCOSO": 53,
    "PIEDADE": 54,
    "PONTAL DE CAMBURI": 55,
    "PRAIA DO CANTO": 56,
    "PRAIA DO SUÁ": 57,
    "REDENÇÃO": 58,
    "REPÚBLICA": 59,
    "RESISTÊNCIA": 60,
    "ROMÃO": 61,
    "SANTA CECÍLIA": 62,
    "SANTA CLARA": 63,
    "SANTA HELENA": 64,
    "SANTA LUÍZA": 65,
    "SANTA LÚCIA": 66,
    "SANTA MARTHA": 67,
    "SANTA TEREZA": 68,
    "SANTO ANDRÉ": 69,
    "SANTO ANTÔNIO": 70,
    "SANTOS DUMONT": 71,
    "SANTOS REIS": 72,
    "SEGURANÇA DO LAR": 73,
    "SOLON BORGES": 74,
    "SÃO BENEDITO": 75,
    "SÃO CRISTÓVÃO": 76,
    "SÃO JOSÉ": 77,
    "SÃO PEDRO": 78,
    "TABUAZEIRO": 79,
    "UNIVERSITÁRIO": 80,
    "VILA RUBIM": 81,
}

bools = {"FALSE": 0, "TRUE": 1}

genders = {"F": 0, "M": 1}


def healthcare_noshows_normalize_row(raw_row: list) -> list:
    """Normalizes the healthcare no-show dataset for consistent processing.

    Args:
        raw_row (list): A list containing raw healthcare no-show data.

    Returns:
        list: A normalized row where:
            - Index 0: Encoded gender value.
            - Index 1: Age (unchanged).
            - Index 2: Encoded neighbourhood value.
            - Index 3: Encoded scholarship status.
            - Index 4: Encoded hypertension status.
            - Index 5: Encoded diabetes status.
            - Index 6: Encoded alcoholism status.
            - Index 7: Encoded handicap status.
            - Index 8: Encoded SMS received status.
            - Index 9: Encoded showed up status.
            - Index 10: Date difference between scheduled day and appointment day.
    """
    normalized_row = []
    normalized_row.append(genders[raw_row[2]])  # gender
    normalized_row.append(int(raw_row[5]))  # age
    normalized_row.append(neighbourhoods[raw_row[6]])  # neighbourhood
    normalized_row.append(bools[raw_row[7]])  # scholarship
    normalized_row.append(bools[raw_row[8]])  # hipertension
    normalized_row.append(bools[raw_row[9]])  # diabetes
    normalized_row.append(bools[raw_row[10]])  # alcoholism
    normalized_row.append(bools[raw_row[11]])  # handcap
    normalized_row.append(bools[raw_row[12]])  # SMS_received
    normalized_row.append(bools[raw_row[13]])  # showed_up
    normalized_row.append(int(raw_row[14]))  # date difference between scheduled day and appointment day

    return normalized_row


def healthcare_noshows_denormalize_row(normalized_row: list) -> list:
    """Reverses the normalization process to retrieve approximate original values.

    Args:
        normalized_row (list): A list containing normalized healthcare no-show data.

    Returns:
        list: An approximate original row where:
            - Index 0: Closest matching gender.
            - Index 1: Age (unchanged).
            - Index 2: Closest matching neighbourhood name.
            - Index 3: Scholarship status.
            - Index 4: Hypertension status.
            - Index 5: Diabetes status.
            - Index 6: Alcoholism status.
            - Index 7: Handicap status.
            - Index 8: SMS received status.
            - Index 9: Showed up status.
            - Index 10: Date difference between scheduled day and appointment day.
    """

    def find_closest_value(dictionary, target_value):
        return min(dictionary, key=lambda k: abs(dictionary[k] - target_value))

    original_row = []
    original_row.append(find_closest_value(genders, normalized_row[0]))  # gender
    original_row.append(normalized_row[1])  # age remains unchanged
    original_row.append(find_closest_value(neighbourhoods, normalized_row[2]))  # neighbourhood
    original_row.append(find_closest_value(bools, normalized_row[3]))  # scholarship
    original_row.append(find_closest_value(bools, normalized_row[4]))  # hypertension
    original_row.append(find_closest_value(bools, normalized_row[5]))  # diabetes
    original_row.append(find_closest_value(bools, normalized_row[6]))  # alcoholism
    original_row.append(find_closest_value(bools, normalized_row[7]))  # handicap
    original_row.append(find_closest_value(bools, normalized_row[8]))  # SMS_received
    original_row.append(find_closest_value(bools, normalized_row[9]))  # showed_up
    original_row.append(normalized_row[10])  # date difference remains unchanged

    return original_row
