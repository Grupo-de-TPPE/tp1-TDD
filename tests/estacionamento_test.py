from src.Estacionamento import Estacionamento

estacionamento = [
    Estacionamento(valorFracao=30, valorHoraCheia=0.15, valorDiariaNoturna=0.45, valorDiariaDiurna=120, mensalidade=600,
                   valorEvento=50, horarios={6, 22}, capacidade=300, retorno=0.5),
    Estacionamento(valorFracao=20, valorHoraCheia=0.1, valorDiariaNoturna=0.3, valorDiariaDiurna=70, mensalidade=455,
                   valorEvento=60, horarios={24, 24}, capacidade=120, retorno=0.6),
    Estacionamento(valorFracao=10, valorHoraCheia=0.0, valorDiariaNoturna=0.4, valorDiariaDiurna=50, mensalidade=350,
                   valorEvento=40, horarios={6, 22}, capacidade=600, retorno=0.7),
]


def testaCadastroUmVeiculo():
    estacionamento[0].AddAcesso('HI139', '08:30', '08:56')
    estacionamento[0].AddAcesso('G49NG', '19:01', '07:50')
    estacionamento[0].AddAcesso('AC50M', '08:30', '18:00')
    estacionamento[0].AddAcesso('RM3A9', '', '')
    estacionamento[0].AddAcesso('AM31J', 'Evento', 'Evento')

    assert (estacionamento[0].getAcessos()) != 0

def testaTipoAcessoPorPlaca():
    estacionamento[0].AddAcesso('AM31J', 'Evento', 'Evento')

    assert estacionamento[0].FindTipoAcesso('AM31J') == 'Evento'

def testaValorAcesso():
    estacionamento[0].AddAcesso('AM31J', 'Evento', 'Evento')

    assert estacionamento[0].GetValorAcesso('AM31J') == 50


def testaValorContratante():
    estacionamento[0].AddAcesso('AM31J', 'Evento', 'Evento')

    assert estacionamento[0].GetValorContratante('AM31J') == 25