import pytest

def test_one():
    assert 2 == 2

def test_two():
    assert 3 == 3

@pytest.mark.parametrize(" nb, nb2", [(1,1),(2,2),(3,3),])
def test_paremtrize(nb, nb2):
    assert nb == nb2