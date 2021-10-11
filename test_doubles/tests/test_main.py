from unittest.mock import Mock
import pytest
from src.main import most_common_word
from src.main import most_common_word_in_web_page

def test_most_common_word_in_web():
    excepct = 'Python'

    mock_requests = Mock()
    mock_requests.get.return_value.text = 'programming'

    # unittest.mock.patch.objectを使ってConnectionにパッチを当てる
    # with unittest.mock.patch.object(requests, "get"):
    most_common = most_common_word_in_web_page(
        ['python', 'Python', 'programming'],
        'https://python.org/',
        user_agent=mock_requests
    )
    assert most_common == excepct

def test_most_common_word():
    assert most_common_word(['a', 'b', 'c'], 'abbbcc') \
            == 'b', 'most_common_word with unique answer'

def test_most_common_word_empty_candidate():
    from pytest import raises
    with raises(Exception):
        most_common_word([], 'abc')
        pytest.fail("empty word raises")

def test_most_common_ambiguous_result():
    assert most_common_word(['a', 'b', 'c'], 'ab') \
        in ('a', 'b'), "there might be a tie"