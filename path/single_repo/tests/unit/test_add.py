from src.add import add

def test_add():
    expect = 5

    result = add(3, 2)

    assert expect == result