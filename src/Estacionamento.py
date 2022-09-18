from src.Acesso import Acesso
from src.Exceptions import DescricaoEmBrancoException, ValorInvalidoException
import re
import datetime
import math

class Estacionamento:
    FRACAO_DE_HORA = 15.0
    QUANTIDADE_DE_FRACAO_POR_HORA = 60 / FRACAO_DE_HORA
    MINIMO_PARA_HORA_CHEIA = (QUANTIDADE_DE_FRACAO_POR_HORA - 1) * FRACAO_DE_HORA
    PORCENTAGEM = 100
    
    def __init__(
        self,
        valorFracao,
        valorHoraCheia,
        valorDiariaDiurna,
        valorDiariaNoturna,
        mensalidade,
        valorEvento,
        horarios,
        capacidade,
        retorno,
    ):
        if valorFracao == "":
            raise DescricaoEmBrancoException("valorFracao")
        elif valorHoraCheia == "":
            raise DescricaoEmBrancoException("valorHoraCheia")
        elif valorDiariaDiurna == "":
            raise DescricaoEmBrancoException("valorDiariaDiurna")
        elif valorDiariaNoturna == "":
            raise DescricaoEmBrancoException("valorDiariaNoturna")
        elif mensalidade == "":
            raise DescricaoEmBrancoException("mensalidade")
        elif valorEvento == "":
            raise DescricaoEmBrancoException("valorEvento")
        elif horarios == "":
            raise DescricaoEmBrancoException("horarios")
        elif capacidade == "":
            raise DescricaoEmBrancoException("capacidade")
        elif retorno == "":
            raise DescricaoEmBrancoException("retorno")

        try:
            self.valorFracao = float(valorFracao)
        except:
            raise ValorInvalidoException("Valor Fração inválido")

        try:
            self.valorHoraCheia = float(valorHoraCheia)/self.PORCENTAGEM
        except:
            raise ValorInvalidoException("Valor hora cheia inválido")

        try:
            self.valorDiariaDiurna = float(valorDiariaDiurna)
        except:
            raise ValorInvalidoException("Valor diária Diurna inválido")

        try:
            self.valorDiariaNoturna = float(valorDiariaNoturna)/self.PORCENTAGEM
        except:
            raise ValorInvalidoException("Valor diária Noturna inválido")

        try:
            self.mensalidade = float(mensalidade)
        except:
            raise ValorInvalidoException("Valor acesso mensalidade inválido")

        try:
            self.valorEvento = float(valorEvento)
        except:
            raise ValorInvalidoException("Valor acesso evento inválido")

        for i in range(6):
            if not re.match("[0-1][0-9]|[2][0-3]:[0-5][0-9]", str(horarios[i])):
                raise ValorInvalidoException(
                    str(i + 1) + "º hora inválida: " + str(horarios[i])
                )

        try:
            horarios[4] = datetime.timedelta(
                hours=int(horarios[4][0:2]), minutes=int(horarios[4][3:5])
            )
        except:
            raise ValorInvalidoException(
                "4º hora inválida: " + str(horarios[4])
            )

        try:
            horarios[5] = datetime.timedelta(
                hours=int(horarios[5][0:2]), minutes=int(horarios[5][3:5])
            )
        except:
            raise ValorInvalidoException(
                "5º hora inválida: " + str(horarios[5])
            )
        self.horarios = horarios

        try:
            self.capacidade = int(capacidade)
        except:
            raise ValorInvalidoException("capacidade")

        try:
            self.capacidade = int(capacidade)
        except:
            raise ValorInvalidoException("capacidade")

        try:
            self.retorno = float(retorno)/self.PORCENTAGEM
        except:
            raise ValorInvalidoException("retorno")
        self.acessos = []
        self.total = 0

    def addAcesso(self, placa, horaEntrada, horaSaida):
        acesso = Acesso(placa, horaEntrada, horaSaida)
        if self.acessos.append(acesso):
            return 1
        return -1

    def getAcessos(self):
        return self.acessos

    def getPermanencia(self, placa):
        for i in self.getAcessos():
            if i.placa == placa:
                return i.calculate(self.horarios[4], self.horarios[5])

    def findTipoAcesso(self, placa):
        permanencia = self.getPermanencia(placa)
        if permanencia[0] == "Evento":
            return "Evento"
        elif permanencia[0] == "Noturna":
            return "Noturna"
        elif permanencia[0] == "Diurna":
            return "Diurna"
        elif permanencia[0] == "Mensalista":
            return "Mensalista"
        elif permanencia[1] > self.MINIMO_PARA_HORA_CHEIA:
            return f"{permanencia[0]+1}:{0}"
        else:
            return f"{permanencia[0]}:{permanencia[1]}"

    def getValorContratante(self, placa):
        return round(self.getValorAcesso(placa) * self.retorno, 2)

    def calcularCustoHora(self, tipoAcesso):
        return float(tipoAcesso.split(":")[0]) * float(self.valorFracao) * self.QUANTIDADE_DE_FRACAO_POR_HORA

    def calcularCustoMinuto(self, tipoAcesso):
        return math.ceil(float(tipoAcesso.split(":")[1]) / self.FRACAO_DE_HORA) * self.valorFracao
    
    def calcularCustoAcesso(self, tipoAcesso):
        return self.calcularCustoHora(tipoAcesso) * (1 - (self.valorHoraCheia)) + self.calcularCustoMinuto(tipoAcesso)
    
    def getValorAcesso(self, placa):
        tipoAcesso = self.findTipoAcesso(placa)
        if tipoAcesso == "Evento":
            return self.valorEvento
        elif tipoAcesso == "Noturna":
            return self.valorDiariaNoturna * self.valorDiariaDiurna
        elif tipoAcesso == "Diurna":
            return self.valorDiariaDiurna
        elif tipoAcesso == "Mensalista":
            return self.mensalidade
        else:
            return round(self.calcularCustoAcesso(tipoAcesso), 2)

    def getTotalApurado(self):
        for i in self.acessos:
            self.total += self.getValorContratante(i.placa)
        return round(self.total, 2)
