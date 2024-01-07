"""Módulo de Exceções Próprias"""

class ExcecaoTransacaoVenda(Exception):
    """Exceção para vendas de produtos que não constam no estoque.
    """
    mensagem = " não consta no estoque!"

    def __init__(self, name: str) -> None:
        super().__init__(name + self.mensagem)


class ExcecaoTransacaoRetorno(Exception):
    """Exceção para retorno de produtos que não foram vendidos.
    """
    mensagem = " não foi vendido!"

    def __init__(self, name: str) -> None:
        super().__init__(name + self.mensagem)