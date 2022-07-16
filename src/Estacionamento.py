from src.Acesso import Acesso
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

    def getPermanencia(self, placa):
        for i in self.acessos:
            # print(f"{i.placa}={i.horaEntrada}")
            if i.placa == placa:
                if i.horaEntrada == "Evento":
                    return [
                        "Evento",
                    ]
                elif i.horaEntrada == "Mensalista":
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

                if t1 > t2:
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
            custoHora = float(tipoAcesso.split(":")[0]) * float(self.valorFracao)
            custoMin = (
                math.ceil(float(tipoAcesso.split(":")[1]) / 15.0) * self.valorFracao
            )
            custoAcesso = custoHora * (1 - (self.valorHoraCheia)) + custoMin
            return custoAcesso

    def GetValorContratante(self, placa):
        return self.GetValorAcesso(placa) * self.retorno