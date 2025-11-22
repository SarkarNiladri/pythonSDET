import pytest

@pytest.mark.xfail
@pytest.mark.great
def test_greater(input_value):    
    assert input_value>100

@pytest.mark.skip
@pytest.mark.great
def test_equal(input_value):
    
    assert input_value>=100

@pytest.mark.other
def test_lesser(input_value):    
    assert input_value<200