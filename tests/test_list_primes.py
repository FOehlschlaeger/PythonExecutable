import pytest
from Executable.src.list_primes import get_all_primes, get_all_primes_between


def test_get_all_primes():
    assert get_all_primes(10) == [1, 2, 3, 5, 7]
    assert get_all_primes(100) == [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert get_all_primes(2) == [1, 2]
    with pytest.raises(ValueError): 
        get_all_primes("a")
    with pytest.raises(ValueError): 
        get_all_primes(-10)
    with pytest.raises(ValueError): 
        get_all_primes(1)
    with pytest.raises(ValueError): 
        get_all_primes(0)


def test_get_all_primes_between():
    assert get_all_primes_between(1, 10) == [1, 2, 3, 5, 7]
    with pytest.raises(ValueError): 
        get_all_primes_between(10, 1)
    with pytest.raises(ValueError): 
        get_all_primes_between(10, "a")
    with pytest.raises(ValueError): 
        get_all_primes_between("a", 10)