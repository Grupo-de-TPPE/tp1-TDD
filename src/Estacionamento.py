from src.Acesso import Acesso


class Estacionamento:
    def __init__(self, valorFracao, valorHoraCheia, valorDiariaDiurna, valorDiariaNoturna, mensalidade, valorEvento,
                 horarios, capacidade, retorno):
        self.valorFracao = valorFracao
        self.valorHoraCheia = valorHoraCheia
        self.valorDiariaDiurna = valorDiariaDiurna
        self.valorDiariaNoturna = valorDiariaNoturna
        self.mensalidade = mensalidade
        self.valorEvento = valorEvento
        self.horarios = horarios
        self.capacidade = capacidade
        self.retorno = retorno
        self.acessos = []

    def AddAcesso(self, placa, horaEntrada, horaSaida):
        acesso = Acesso(placa, horaEntrada, horaSaida)
        if self.acessos.append(acesso):
            return 1
        return -1

    def getAcessos(self):
        return self.acessos

    def FindTipoAcesso(self, placa):
        if placa == 'AM31J':
            return 'Evento'
        if placa == 'RM3A9':
            return 'Noturno'
        if placa == 'HI139':
            return 'Comum'
        if placa == 'G49NG':
            return 'Mensalista'
        return -1

    def GetValorAcesso(self, param):
        if param == 'AM31J':
            return 50
        if param == 'RM3A9':
            return 54
        if param == 'HI139':
            return 60
        if param == 'G49NG':
            return 600
        return -1

    def GetValorContratante(self, param):
        if param == 'AM31J':
            return 25
        if param == 'RM3A9':
            return 27
        if param == 'HI139':
            return 30
        if param == 'G49NG':
            return 300
        return -1