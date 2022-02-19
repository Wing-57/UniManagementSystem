from enums import rank


def model():
    return {
        "password": str,
        "rank": rank.Rank
    }
