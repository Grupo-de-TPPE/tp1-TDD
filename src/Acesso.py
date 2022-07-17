from src.Exceptions import DescricaoEmBrancoException


class Acesso():
    def __init__(self, placa, horaEntrada, horaSaida):
        if(placa == ""):
            raise DescricaoEmBrancoException
        if(horaEntrada == ""):
            raise DescricaoEmBrancoException
        if(horaSaida == ""):
            raise DescricaoEmBrancoException    
        self.placa = placa
        self.horaEntrada = horaEntrada 
        self.horaSaida = horaSaida