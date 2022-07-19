from src.Acesso import Acesso
from src.Exceptions import DescricaoEmBrancoException
from src.Exceptions import ValorInvalidoException
import pytest

@pytest.mark.excecao
def testePlacaBranco():
    with pytest.raises(DescricaoEmBrancoException):
        Acesso("","19:30","20:30")

@pytest.mark.excecao
def testeEntradaBranco():
    with pytest.raises(DescricaoEmBrancoException):
        Acesso("AM319","","20:34")

@pytest.mark.excecao
def testeSaidaBranco():
    with pytest.raises(DescricaoEmBrancoException):
        Acesso("AM122","20:34","")

@pytest.mark.excecao
def testeValoresInvalidos():
    with pytest.raises(ValorInvalidoException):
        Acesso("AM12","25:00","20:34")

@pytest.mark.excecao
def testeValoresInvalidos():
    with pytest.raises(ValorInvalidoException):
        Acesso("AM12","25:00","20:50")
        Acesso("AM12","20:60","20:50")
        Acesso("AM12","23:00","25:50")
        Acesso("AM12","21:00","20:611")
        Acesso("AM12","-21:00","20:11")