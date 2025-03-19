
import pytest
from simple_module import is_even

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-4) == True
    assert is_even(-5) == False

if __name__ == "__main__":
    pytest.main()