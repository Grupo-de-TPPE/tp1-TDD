from src.Acesso import Acesso
from src.Exceptions import DescricaoEmBrancoException, ValorInvalidoException
import re
import datetime
import math


class Estacionamento:
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
            self.valorHoraCheia = float(valorHoraCheia)/100
        except:
            raise ValorInvalidoException("Valor hora cheia inválido")

        try:
            self.valorDiariaDiurna = float(valorDiariaDiurna)
        except:
            raise ValorInvalidoException("Valor diária Diurna inválido")

        try:
            self.valorDiariaNoturna = float(valorDiariaNoturna)/100
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
            self.retorno = float(retorno)/100
        except:
            raise ValorInvalidoException("retorno")
        self.acessos = []
        self.total = 0

    def AddAcesso(self, placa, horaEntrada, horaSaida):
        acesso = Acesso(placa, horaEntrada, horaSaida)
        if self.acessos.append(acesso):
            return 1
        return -1

    def getAcessos(self):
        return self.acessos

    def getPermanencia(self, placa):
        for i in self.acessos:
            if i.placa == placa:
                if i.horaEntrada.lower() == "evento":
                    return [
                        "Evento",
                    ]
                elif i.horaEntrada.lower() == "mensalista":
                    return [
                        "Mensalista",
                    ]

                entrada = datetime.time(
                    hour=int(i.horaEntrada.split(":")[0]),
                    minute=int(i.horaEntrada.split(":")[1]),
                )
                saida = datetime.time(
                    hour=int(i.horaSaida.split(":")[0]),
                    minute=int(i.horaSaida.split(":")[1]),
                )
                t1 = datetime.timedelta(hours=entrada.hour, minutes=entrada.minute)
                t2 = datetime.timedelta(hours=saida.hour, minutes=saida.minute)
                delta = t2 - t1
                if t1 > t2 and t1 > self.horarios[4] and t2 < self.horarios[5]:
                    return [
                        "Noturna",
                    ]
                if delta.seconds > 32400:
                    return [
                        "Diurna",
                    ]

                return [delta.seconds // 3600, delta.seconds % 3600 // 60]

    def FindTipoAcesso(self, placa):
        permanencia = self.getPermanencia(placa)
        if permanencia[0] == "Evento":
            return "Evento"
        elif permanencia[0] == "Noturna":
            return "Noturna"
        elif permanencia[0] == "Diurna":
            return "Diurna"
        elif permanencia[0] == "Mensalista":
            return "Mensalista"
        elif permanencia[1] > 45:
            return f"{permanencia[0]+1}:{0}"
        else:
            return f"{permanencia[0]}:{permanencia[1]}"

    def GetValorAcesso(self, placa):
        tipoAcesso = self.FindTipoAcesso(placa)
        if tipoAcesso == "Evento":
            return self.valorEvento
        elif tipoAcesso == "Noturna":
            return self.valorDiariaNoturna * self.valorDiariaDiurna
        elif tipoAcesso == "Diurna":
            return self.valorDiariaDiurna
        elif tipoAcesso == "Mensalista":
            return self.mensalidade
        else:
            custoHora = float(tipoAcesso.split(":")[0]) * float(self.valorFracao) * 4
            custoMin = (
                math.ceil(float(tipoAcesso.split(":")[1]) / 15.0) * self.valorFracao
            )
            custoAcesso = custoHora * (1 - (self.valorHoraCheia)) + custoMin
            return round(custoAcesso, 2)

    def GetValorContratante(self, placa):
        return round(self.GetValorAcesso(placa) * self.retorno, 2)

    def GetTotalApurado(self):
        for i in self.acessos:
            self.total += self.GetValorContratante(i.placa)
        return round(self.total, 2)
