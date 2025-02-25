import pytest
from datetime import date

def triple(x):  # Function to test
    return x * 3

test_data = [(5, 15), ('a', 'aaa'), (0, 0), (1000, 3000), ([True], [True, True, True])]  # List of values for testing containing input and expected result

@pytest.mark.parametrize("input,result", test_data)  # Parametrize the test with the test data; the first argument is a string defining parameters to the test and mapping them to the test data
def test_triple(input, result):  # The test expects two parameters (which come from each element of test data)
    print("input {} result {}:".format(input, result))  # The test expects two parameters (which come from each element of test data)
    assert triple(input) == result   # Test the function with the parameters

def test_triple_raises_err_on_invalid_args():
    with pytest.raises(TypeError):
        triple("a", "b")

# def test_president_dob(president):
#     assert isinstance(president(date)) or date is None