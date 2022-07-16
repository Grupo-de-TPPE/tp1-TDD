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

def testaTipoAcessoPorPlaca1():
    estacionamento[0].AddAcesso('AM31J', 'Evento', 'Evento')
    assert estacionamento[0].FindTipoAcesso('AM31J') == 'Evento'

def testaTipoAcessoPorPlaca2():
    estacionamento[0].AddAcesso('RM3A9', '', '')
    assert estacionamento[0].FindTipoAcesso('RM3A9') == 'Noturno'

def testaTipoAcessoPorPlaca3():
    estacionamento[0].AddAcesso('G49NG', '19:01', '07:50')
    assert estacionamento[0].FindTipoAcesso('G49NG') == 'Mensalista'

def testaTipoAcessoPorPlaca4():
    estacionamento[0].AddAcesso('HI139', '08:30', '08:56')
    assert estacionamento[0].FindTipoAcesso('HI139') == 'Comum'

def testaValorAcesso1():
    estacionamento[0].AddAcesso('AM31J', 'Evento', 'Evento')
    assert estacionamento[0].GetValorAcesso('AM31J') == 50

def testaValorAcesso2():
    estacionamento[0].AddAcesso('RM3A9', '', '')
    assert estacionamento[0].GetValorAcesso('RM3A9') == 54

def testaValorAcesso3():
    estacionamento[0].AddAcesso('G49NG', '19:01', '07:50')
    assert estacionamento[0].GetValorAcesso('G49NG') == 600

def testaValorAcesso4():
    estacionamento[0].AddAcesso('HI139', '08:30', '08:56')
    assert estacionamento[0].GetValorAcesso('HI139') == 60

def testaValorContratante1():
    estacionamento[0].AddAcesso('AM31J', 'Evento', 'Evento')
    assert estacionamento[0].GetValorContratante('AM31J') == 25

def testaValorContratante2():
    estacionamento[0].AddAcesso('RM3A9', '', '')
    assert estacionamento[0].GetValorContratante('RM3A9') == 27

def testaValorContratante3():
    estacionamento[0].AddAcesso('G49NG', '19:01', '07:50')
    assert estacionamento[0].GetValorContratante('G49NG') == 300

def testaValorContratante4():
    estacionamento[0].AddAcesso('HI139', '08:30', '08:56')
    assert estacionamento[0].GetValorContratante('HI139') == 30