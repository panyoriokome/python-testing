"""モジュールの説明タイトル

* ソースコードの一番始めに記載すること
* importより前に記載する

Todo:
    TODOリストを記載
    * conf.pyの``sphinx.ext.todo`` を有効にしないと使用できない
    * conf.pyの``todo_include_todos = True``にしないと表示されない

"""

from src.add import add

def test_add():
    """add functionのテスト

    テストだよ
    Tests:
        3を入力する。
    Expects:
        あほになること。

    Note:
        注意事項などを記載

    """
    expect = 5

    result = add(3, 2)

    assert expect == result