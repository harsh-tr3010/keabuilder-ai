import numpy as np
import faiss

assets = [
    "sales funnel template",
    "fitness landing page",
    "real estate lead funnel",
    "agency onboarding funnel",
    "blue modern logo"
]


def text_to_vector(text):
    """
    Simple deterministic demo embedding
    """
    vec = np.zeros(32, dtype="float32")

    for i, ch in enumerate(text.lower()[:32]):
        vec[i] = ord(ch) / 255.0

    return vec


# Build index
vectors = np.array(
    [text_to_vector(x) for x in assets]
).astype("float32")

index = faiss.IndexFlatL2(32)
index.add(vectors)


def semantic_search(query):
    q = np.array([text_to_vector(query)]).astype("float32")

    distances, ids = index.search(q, 3)

    results = []

    for i in ids[0]:
        results.append(assets[i])

    return {
        "query": query,
        "results": results
    }