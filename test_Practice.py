import pytest
import math
# run with: pytest -v -s test_Practice.py

@pytest.mark.squre
def test_sqrt():
    num = 25
    assert math.sqrt(num)==5


@pytest.mark.other
def testsqure():
    assert 7*7 == 50




