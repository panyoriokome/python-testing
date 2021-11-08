from src.substruct import substruct

def test_substruct():
    """substruct functionのテスト

    テストだよ
    Tests:
        3を入力する。
    Expects:
        あほになること。
    Note:
        注意事項などを記載

    """
    expect = 1

    result = substruct(3, 2)

    assert expect == result