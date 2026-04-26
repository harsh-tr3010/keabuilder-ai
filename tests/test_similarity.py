from core.similarity_engine import find_matches

def test_search():
    assert len(find_matches("fitness")) > 0