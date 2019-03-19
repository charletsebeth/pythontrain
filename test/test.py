from pythontrain import recursion
from pythontrain import sorting

def test_sum_array():

    """
    make sure sum_array works
    """
    assert sum_array([1, 3, 4, 2, 5]) == 15, 'incorrect'

def test_fibonacci():

    """
    make sure fibonacci function works
    """
    assert fibonacci(3) == 2, 'incorrect'

def test_factorial():

    """
    make sure factorial function works
    """
    assert factorial(0) == 1,'incorrect'
    assert factorial(2) == 2, 'incorrect'

def test_reverse():

    """
    make sure reverse function works
    """
    assert reverse('abc') == 'cba', 'incorrect'

def test_bubble_sort():

    """
    make sure bubble_sort function works
    """
    assert bubble_sort([1,7,5,9,3]) == [1, 3, 5, 7, 9], 'incorrect'


def test_quick_sort():

    """
    make sure bubble_sort function works
    """
    assert merge_sort([1,7,5,9,3]) == [1, 3, 5, 7, 9], 'incorrect'

def test_merge_sort():

    """
    make sure bubble_sort function works
    """
    assert quick_sort([1,7,5,9,3]) == [1, 3, 5, 7, 9], 'incorrect'
