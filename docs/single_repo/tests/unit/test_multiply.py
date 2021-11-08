from src.multiply import multiply

def test_multiply():
    """multiply functionのテスト

    テストだよ
    

    Tests:
        3を入力する。
    Expects:
        あほになること。
    Note:
        注意事項などを記載

    """
    expect = 6

    result = multiply(3, 2)

    assert expect == result