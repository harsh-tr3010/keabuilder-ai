def semantic_search(q):
    data = [
        "landing page template",
        "sales funnel pro",
        "fitness funnel"
    ]

    result = [x for x in data if q.lower() in x.lower()]

    return {
        "query": q,
        "results": result
    }
