from src.Acesso import Acesso
from src.Exceptions import DescricaoEmBrancoException
import pytest

def testePlacaBranco():
    with pytest.raises(DescricaoEmBrancoException):
        Acesso("","19:30",'20:30')

def testeEntradaBranco():
    with pytest.raises(DescricaoEmBrancoException):
        Acesso("AM319","",'20:34')

def testeSaidaBranco():
    with pytest.raises(DescricaoEmBrancoException):
        Acesso("AM122","20:34",'')