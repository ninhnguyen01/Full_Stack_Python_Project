import pytest

def addem(one, two):
   return one + two

@pytest.mark.parametrize("one,two,sum",
   [(0,0,0), (0,1,1), (1,1,2), (-1,-1,-2)])
def test_addem(one, two, sum):
   assert addem(one, two) == sum
   