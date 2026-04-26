from core.lead_engine import classify

def test_hot():
    assert classify(80) == "Hot"