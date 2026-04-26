from core.router import route_task

def test_image():
    assert route_task("Image") == "Replicate"