import pytest

from dogs import sample_function
from dogs import Dogs

@pytest.fixture
def Dogs_object():
    obj = Dogs()
    return obj

def test_Dogs_instance_has_sample_method(Dogs_object):
    assert hasattr(Dogs_object, "sample_method")

def test_dogs_has_sample_function():
    assert sample_function() is None  # no return value
