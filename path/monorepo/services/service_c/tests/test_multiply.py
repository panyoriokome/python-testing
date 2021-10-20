from src.multiply import multiply

def test_multiply():
    expect = 6

    result = multiply(3, 2)

    assert expect == result