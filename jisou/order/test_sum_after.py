import pytest

class TestSum:
    
    def test_sum(self):
        assert sum([0, 1, 2, 3, 4]) == 10

    def test_negative(self):
        assert sum([0, 1, 2, 3, 4, -5]) == 5

    def test_type_error(self):
        with pytest.raises(TypeError):
            sum([1, None])