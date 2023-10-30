from enum import Enum

class Tipo_Produto(Enum):
    CELULAR = 1
    NOTEBOOK = 2
    COMPUTADOR = 3


class Produto:
    def __init__(self, produto: str, codigo: int, preco : float, tipo: Tipo_Produto) -> None:
        self.produto = produto
        self.codigo = codigo
        self.preco = preco
        self.tipo = tipo


class Celular(Produto):
    def __init__(self, produto: str, codigo: int, preco: float, tipo: Tipo_Produto) -> None:
        super().__init__(produto, codigo, preco, tipo)


class Laptop(Produto):
    def __init__(self, produto: str, codigo: int, preco: float, tipo: Tipo_Produto) -> None:
        super().__init__(produto, codigo, preco, tipo)


class Computador(Produto):
    def __init__(self, produto: str, codigo: int, preco: float, tipo: Tipo_Produto) -> None:
        super().__init__(produto, codigo, preco, tipo)


class Inventario():
    def __init__(self) -> None:
        self.produtos = []

    def vender_produto(self, produto: Produto) -> None:
        """Função que vende um produto do estoque, caso este exista.
        """
        try:
            self.produtos.remove(produto)

        except KeyError:
            print(f"{produto} não consta no estoque!")

    def retornar_produto(self, produto: Produto) -> None:
        """Função que retorna um produto vendido para o estoque, caso este tenha sido vendido.
        """
        pass

    def repor_produto(self, produto: Produto) -> None:
        """Função que repõe (aumenta a quantidade de) um produto no estoque.
        """
 
        self.produtos.append(produto)

    def listar_produtos(self) -> None:
        """Função que lista o estoque de produtos disponíveis.
        """
        pass

    


