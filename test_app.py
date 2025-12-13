import time

def test_dummy():
    time.sleep(3)
    assert True

def test_loop():
    x = 0
    for i in range(100000):
        x += i
    assert x > 0
