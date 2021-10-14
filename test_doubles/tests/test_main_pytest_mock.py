import pytest
from src.main import most_common_word
from src.main import most_common_word_in_web_page
from src.main import most_common_word_in_web_page2
from unittest.mock import Mock, patch

def test_most_common_word_in_web():
    from unittest.mock import Mock
    excepct = 'Python'

    mock_requests = Mock()
    mock_requests.get.return_value.text = 'programming Python Python'

    # unittest.mock.patch.objectを使ってConnectionにパッチを当てる
    # with unittest.mock.patch.object(requests, "get"):
    most_common = most_common_word_in_web_page(
        ['python', 'Python', 'programming'],
        'https://python.org/',
        user_agent=mock_requests
    )
    assert most_common == excepct
    assert mock_requests.get.call_count == 1
    assert mock_requests.get.call_args[0][0] == 'https://python.org/'

def test_most_common_word_in_web2(mocker):
    excepct = 'Python'

    requests_mock = mocker.patch('src.main.requests.get', return_value='programming Python Python')
    most_common = most_common_word_in_web_page2(
        ['python', 'Python', 'programming'],
        'https://python.org/'
    )
    assert most_common == excepct
    assert requests_mock.get.call_count == 1
    assert requests_mock.get.call_args[0][0] == 'https://python.org/'

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
