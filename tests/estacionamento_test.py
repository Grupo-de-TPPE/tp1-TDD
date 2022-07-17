import datetime
import pytest
from optparse import Values
from src.Estacionamento import Estacionamento

estacionamento = [
    Estacionamento(valorFracao=30, valorHoraCheia=0.15, valorDiariaNoturna=0.45, valorDiariaDiurna=120, mensalidade=600,
                   valorEvento=50, horarios=(6, 22, 19, 8, datetime.timedelta(hours=19), datetime.timedelta(hours=8)), capacidade=300, retorno=0.5),
    Estacionamento(valorFracao=20, valorHoraCheia=0.1, valorDiariaNoturna=0.3, valorDiariaDiurna=70, mensalidade=455,
                   valorEvento=60, horarios=(24, 24, 21, 7, 21, 7), capacidade=120, retorno=0.6),
    Estacionamento(valorFracao=10, valorHoraCheia=0.0, valorDiariaNoturna=0.4, valorDiariaDiurna=50, mensalidade=350,
                   valorEvento=40, horarios=(6, 22, 20, 8, 20, 8), capacidade=600, retorno=0.7),
]

def testaCadastroUmVeiculo():
    estacionamento[0].AddAcesso('HI139', '08:30', '08:56')
    estacionamento[0].AddAcesso('G49NG', 'Mensalista', 'Mensalista')
    estacionamento[0].AddAcesso('AC50M', '08:30', '18:00')
    estacionamento[0].AddAcesso('RM3A9', '20:00', '07:00')
    estacionamento[0].AddAcesso('AM31J', 'Evento', 'Evento')

    assert (estacionamento[0].getAcessos()) != 0

@pytest.mark.parametrize('expected, values',[('Noturna',['RM3A9', '20:00', '07:00']),('Mensalista',['G49NG', 'Mensalista', 'Mensalista']),('0:26',['HI139', '08:30', '08:56']),
('Evento',['AM31J', 'Evento', 'Evento'])])
def testaTipoAcessoPorPlaca1(expected, values):
    estacionamento[0].AddAcesso(values[0], values[1], values[2])
    assert estacionamento[0].FindTipoAcesso(values[0]) == expected

@pytest.mark.parametrize('expected, values',[(50, ['AM31J', 'Evento', 'Evento']),(54,['RM3A9', '20:00', '07:00']),
(600,['G49NG', 'Mensalista', 'Mensalista']),(60,['HI139', '08:30', '08:56'])])
def testaValorAcesso(expected, values):
    estacionamento[0].AddAcesso(values[0], values[1], values[2])
    assert estacionamento[0].GetValorAcesso(values[0]) == expected


@pytest.mark.parametrize('expected, values', [(25,['AM31J','Evento', 'Evento']),(27,['RM3A9', '20:00', '07:00']),(300,['G49NG', 'Mensalista', 'Mensalista']),
(30,['HI139', '08:30', '08:56']),(45,['AM321', '8:00','8:45'])])
def testaValorContratante(expected, values):
    estacionamento[0].AddAcesso(values[0], values[1], values[2])
    assert estacionamento[0].GetValorContratante(values[0]) == expected


