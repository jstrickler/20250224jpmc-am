import pytest

@pytest.mark.alpha  # Mark with label alpha
def test_one():
    assert 1
    
# pytest.mark(test_one, "alpha")

@pytest.mark.alpha  # Mark with label alpha
@pytest.mark.gamma
def test_two():
    assert 1

@pytest.mark.beta  # Mark with label beta
def test_three():
    assert 1

