import time

def test_dummy():
    time.sleep(3)
    assert True

def test_loop():
    x = 0
    for i in range(100000):
        x += i
    assert x > 0

def test_nested_loops():
    total = 0
    for i in range(2000):
        for j in range(2000):
            total += i + j
    assert total > 0
