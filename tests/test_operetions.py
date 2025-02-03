from src.math_operations import add,sub
def test_add():
    assert add(2,3)==5
    assert add(a:-1,b:1)==0
    assert add(-2,-8)==-10
    assert add(2,b:-7)==-5
def test_sub():
    assert sub(2,3)==-1
    assert sub(a:-1,b:1)==-2
    assert sub(-2,-8)==6
    assert sub(2,b:-7)==9