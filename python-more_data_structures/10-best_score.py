def best_score(a_dictionary):
    if not a_dictionary:
        return None
    kmax = max(a_dictionary, key=a_dictionary.get)
    return kmax
