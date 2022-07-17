from src.Exceptions import DescricaoEmBrancoException, ValorAcessoInvalidoException
import datetime
import re

class Acesso():

    def is_time_valid(self, horario):

        if not horario[0].isnumeric():
            return True

        hora = int(horario.split(":")[0])
        minuto = int(horario.split(":")[1])

        return hora >= 0 and hora <= 23 and minuto >= 0 and minuto <= 59

    def __init__(self, placa, horaEntrada, horaSaida):
        if(placa == ""):
            raise DescricaoEmBrancoException('placa')
        if(horaEntrada == ""):
            raise DescricaoEmBrancoException('horaEntrada')
        if(horaSaida == ""):
            raise DescricaoEmBrancoException('horaSaida')

        if(re.match("((0-9)(a-z)(A-Z)){5}",placa)):
            raise ValorAcessoInvalidoException('Placa inválida!')
        
        if not self.is_time_valid(horaEntrada):
            raise ValorAcessoInvalidoException('O valor de horaEntrada não é um valor válido')
            
        if not self.is_time_valid(horaSaida):
            raise ValorAcessoInvalidoException('O valor de horaSaida não é um valor válido')
        
        self.placa = placa
        self.horaEntrada = horaEntrada 
        self.horaSaida = horaSaida

