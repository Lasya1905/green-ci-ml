import time
import math

def test_dummy():
    time.sleep(3)
    assert True

def test_loop():
    x = 0
    for i in range(100000):
        x += i
    assert x > 0

def test_nested_loops():
    s = 0
    for i in range(2000):
        for j in range(2000):
            s += i + j
    assert s > 0

def test_memory():
    data = [i for i in range(500_000)]
    assert len(data) > 0


def test_math():
    total = 0
    for i in range(300_000):
        total += math.sqrt(i)
    assert total > 0

def test_mixed():
    time.sleep(2)
    x = sum(i for i in range(500_000))
    assert x > 0

def test_combo():
    data = [i*i for i in range(700_000)]
    total = sum(data)
    assert total > 0

def test_file_io():
    with open("temp_test.txt", "w") as f:
        for i in range(200_000):
            f.write(str(i))

    with open("temp_test.txt", "r") as f:
        data = f.read()

    assert len(data) > 0