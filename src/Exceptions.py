class ValorAcessoInvalidoException(Exception):
    """Exceção lançada ao valores inválidos"""
    def __init__(self, message):
        super().__init__(message)
    pass

class DescricaoEmBrancoException(Exception):
    """Exceção lançada ao receber valores vazios"""
    def __init__(self, message=''):
        super().__init__(message)
    pass
