"""Módulo que contém as classes e métodos do sistema de comércio"""

from enum import Enum  # importante!
import exceptions as excpt

class Tipo_Produto(Enum):
    CELULAR = 1
    NOTEBOOK = 2
    COMPUTADOR = 3


class Produto:
    def __init__(self, name: str, codigo: int, preco : float, tipo: Tipo_Produto) -> None:
        self.name = name
        self.codigo = codigo
        self.preco = preco
        self.tipo = tipo


# produto tipo 1
class Celular(Produto):
    def __init__(self, name: str, codigo: int, preco: float, tipo: Tipo_Produto) -> None:
        super().__init__(name, codigo, preco, tipo)


# produto tipo 2
class Laptop(Produto):
    def __init__(self, name: str, codigo: int, preco: float, tipo: Tipo_Produto) -> None:
        super().__init__(name, codigo, preco, tipo)


# produto tipo 3
class Computador(Produto):
    def __init__(self, name: str, codigo: int, preco: float, tipo: Tipo_Produto) -> None:
        super().__init__(name, codigo, preco, tipo)


class Inventario:
    produtos = [] # lista que conterá o estoque dos produtos disponíveis
    produtos_vendidos = [] # lista que conterá o conjunto de produtos vendidos

    def vender_produto(self, produto: Produto) -> None:
        """Função que vende um produto do estoque, caso este exista.
        """
        if produto in self.produtos:
            self.produtos.remove(produto) # produto vendido
            self.produtos_vendidos.append(produto)
            print(f"{produto.name} (código: {produto.codigo}) foi vendido por R$ {produto.preco:.2f}.")
        else:
            raise excpt.ExcecaoTransacaoVenda(produto.name)
            

    def retornar_produto(self, produto: Produto) -> None:
        """Função que retorna um produto vendido para o estoque, caso este tenha sido vendido.
        """
        if produto in self.produtos_vendidos:
            self.produtos.append(produto) # produto retornado
            self.produtos_vendidos.remove(produto)
            print(f"{produto.name} (código: {produto.codigo}) foi retornado (valor: R$ {produto.preco:.2f}).")
        else:
            raise excpt.ExcecaoTransacaoRetorno(produto.name)

    def repor_produto(self, produto: Produto) -> None:
        """Função que repõe (aumenta a quantidade de) um produto no estoque.
        """
        self.produtos.append(produto) # produto reposto
        print(f"{produto.name} (código: {produto.codigo}) foi reposto no estoque por R$ {produto.preco:.2f} (quantidade: {self.produtos.count(produto)}).")

    def listar_produtos(self) -> None:
        """Função que lista o estoque de produtos disponíveis.
        """
        print("\n")
        print("="*37)
        print("## ESTOQUE DE PRODUTOS DISPONÍVEIS ##")
        print("="*37, "\n")

        for produto in set(self.produtos):
            print(f"- Há {self.produtos.count(produto)} {produto.name} no estoque (código: {produto.codigo}, preço: R$ {produto.preco:.2f}, tipo: {produto.tipo})")

        print("\n")
