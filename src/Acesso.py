from src.Exceptions import DescricaoEmBrancoException, ValorInvalidoException
import datetime
import re


class Acesso:
    def is_time_valid(self, horario):

        if horario.lower() == "evento" or horario.lower() == "mensalista":
            return True

        hora = int(horario.split(":")[0])
        minuto = int(horario.split(":")[1])

        return hora >= 0 and hora <= 23 and minuto >= 0 and minuto <= 59

    def __init__(self, placa, horaEntrada, horaSaida):
        if placa == "":
            raise DescricaoEmBrancoException("placa")
        if horaEntrada == "":
            raise DescricaoEmBrancoException("horaEntrada")
        if horaSaida == "":
            raise DescricaoEmBrancoException("horaSaida")

        if re.match("[a-zA-Z0-9]{6}", placa):
            raise ValorInvalidoException("Placa inválida!")

        if not self.is_time_valid(horaEntrada):
            raise ValorInvalidoException(
                "O valor de horaEntrada não é um valor válido"
            )

        if not self.is_time_valid(horaSaida):
            raise ValorInvalidoException(
                "O valor de horaSaida não é um valor válido"
            )

        self.placa = placa
        self.horaEntrada = horaEntrada
        self.horaSaida = horaSaida
