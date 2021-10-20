from src.substruct import substruct

def test_substruct():
    expect = 1

    result = substruct(3, 2)

    assert expect == result