from enum import Enum  # importante!

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
        try:
            self.produtos.remove(produto) # produto vendido
        except ValueError:
            print(f"{produto.name} não consta no estoque!")
        else:
            self.produtos_vendidos.append(produto)

    def retornar_produto(self, produto: Produto) -> None:
        """Função que retorna um produto vendido para o estoque, caso este tenha sido vendido.
        """
        try:
            if produto in self.produtos_vendidos:
                self.produtos.append(produto) # produto retornado
            else:
                raise ValueError()
        except ValueError:
            print(f"{produto.name} não foi vendido!")

    def repor_produto(self, produto: Produto) -> None:
        """Função que repõe (aumenta a quantidade de) um produto no estoque.
        """
        self.produtos.append(produto) # produto reposto

    def listar_produtos(self) -> None:
        """Função que lista o estoque de produtos disponíveis.
        """
        print("\n")
        print("="*37)
        print("## ESTOQUE DE PRODUTOS DISPONÍVEIS ##")
        print("="*37, "\n")

        for produto in self.produtos:
            print(f"- Há {self.produtos.count(produto)} {produto.name} no estoque (código: {produto.codigo}, preço: R$ {produto.preco:.2f}, tipo: {produto.tipo})")


# exemplo [melhorar isso...]
produto1 = Produto("PC DELL", 12345, 4500.00, Tipo_Produto.COMPUTADOR)
produto2 = Produto("SANSUNG J2 PRIME", 10010, 1000.00, Tipo_Produto.CELULAR)
produto3 = Produto("NOTEBOOK ACER", 11111, 2000.00, Tipo_Produto.NOTEBOOK)
produto4 = Produto("YURE", 11111, 2000.0, Tipo_Produto.NOTEBOOK)

Inventario().repor_produto(produto1)
Inventario().repor_produto(produto2)
Inventario().repor_produto(produto3)
Inventario().vender_produto(produto2)
Inventario().vender_produto(produto1)
Inventario().retornar_produto(produto3)
Inventario().listar_produtos()


    


