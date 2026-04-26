from services.vector_store import search_similar

def find_matches(query):
    items = [
        "Fitness landing page",
        "Real estate lead funnel",
        "Ecommerce checkout funnel",
        "Law consultation funnel",
        "Course webinar funnel"
    ]
    return search_similar(query, items)