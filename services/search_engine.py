def search_assets(q):
    data = ["sales funnel","fitness page","real estate leads"]
    return [x for x in data if q.lower() in x.lower()]
