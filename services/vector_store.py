from difflib import get_close_matches

def search_similar(query, items):
    return get_close_matches(query, items, n=5, cutoff=0.2)