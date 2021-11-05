import pytest

class TestSum:
    def setup(self):
        self.data = [0, 1, 2, 3]
    
    def test_sum(self):
        self.data.append(4)
        actual = sum(self.data)
        assert actual == 10

    def test_negative(self):
        self.data.append(-5)
        actual = sum(self.data)
        assert actual == 5

    def test_type_error(self):
        self.data.append(None)
        with pytest.raises(TypeError):
            sum(self.data)