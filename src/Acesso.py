from src.Exceptions import DescricaoEmBrancoException, ValorInvalidoException
import datetime
import re


class Acesso:

    MINUTO_EM_SEGUNDOS = 60
    HORA_EM_SEGUNDOS = MINUTO_EM_SEGUNDOS * 60
    MINIMO_PARA_DIARIA = 9
    DIARIA_EM_SEGUNDOS = MINIMO_PARA_DIARIA * HORA_EM_SEGUNDOS
    FORMATO_PLACA_REGEX = "[a-zA-Z0-9]{6}"

    def __init__(self, placa, horaEntrada, horaSaida):

        for params in list(locals().keys()):
            if params != 'self' and locals()[params] == "":
                raise DescricaoEmBrancoException(params)

        if re.match(self.FORMATO_PLACA_REGEX, placa):
            raise ValorInvalidoException("Placa inválida!")

        if not self.isTimeValid(horaEntrada):
            raise ValorInvalidoException(
                "O valor de horaEntrada não é um valor válido"
            )

        if not self.isTimeValid(horaSaida):
            raise ValorInvalidoException(
                "O valor de horaSaida não é um valor válido"
            )

        self.placa = placa
        self.horaEntrada = horaEntrada
        self.horaSaida = horaSaida

    def isTimeValid(self, horario):

        if horario.lower() == "evento" or horario.lower() == "mensalista":
            return True

        hora = int(horario.split(":")[0])
        minuto = int(horario.split(":")[1])

        return hora >= 0 and hora <= 23 and minuto >= 0 and minuto <= 59
    
    def calculate(self, hora1, hora2):

        if self.horaEntrada.lower() == "evento" or self.horaEntrada.lower() == "mensalista" :
            return [
                self.horaEntrada.lower().capitalize()
            ]

        entrada = datetime.time(
            hour=int(self.horaEntrada.split(":")[0]),
            minute=int(self.horaEntrada.split(":")[1]),
        )
        saida = datetime.time(
            hour=int(self.horaSaida.split(":")[0]),
            minute=int(self.horaSaida.split(":")[1]),
        )

        t1 = datetime.timedelta(hours=entrada.hour, minutes=entrada.minute)
        t2 = datetime.timedelta(hours=saida.hour, minutes=saida.minute)

        if t1 > t2 and t1 > hora1 and t2 < hora2:
            return [
                "Noturna",
            ]

        delta = t2 - t1

        if delta.seconds > self.DIARIA_EM_SEGUNDOS:
            return [
                "Diurna",
            ]

        return [delta.seconds // self.HORA_EM_SEGUNDOS, delta.seconds % self.HORA_EM_SEGUNDOS // self.MINUTO_EM_SEGUNDOS]