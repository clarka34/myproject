from myproject.basic_utils import multiple_by_10
from numpy import inf

def test_multiply_by_10():
    assert multiple_by_10(3) == 30
    assert multiple_by_10(-1) == -10
    assert multiple_by_10(inf) == inf
    assert multiple_by_10(-inf) == -inf
