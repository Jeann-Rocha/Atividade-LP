from enum import Enum

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


class Celular(Produto):
    def __init__(self, name: str, codigo: int, preco: float, tipo: Tipo_Produto) -> None:
        super().__init__(name, codigo, preco, tipo)


class Laptop(Produto):
    def __init__(self, name: str, codigo: int, preco: float, tipo: Tipo_Produto) -> None:
        super().__init__(name, codigo, preco, tipo)


class Computador(Produto):
    def __init__(self, name: str, codigo: int, preco: float, tipo: Tipo_Produto) -> None:
        super().__init__(name, codigo, preco, tipo)


class Inventario():
    produtos = []

    def vender_produto(self, produto: Produto) -> None:
        """Função que vende um produto do estoque, caso este exista.
        """
        try:
            self.produtos.remove(produto)
        except ValueError:
            print(f"{produto.name} não consta no estoque!")

    def retornar_produto(self, produto: Produto) -> None:
        """Função que retorna um produto vendido para o estoque, caso este tenha sido vendido.
        """
        pass

    def repor_produto(self, produto: Produto) -> None:
        """Função que repõe (aumenta a quantidade de) um produto no estoque.
        """
 
        self.produtos.append(produto.name)

    def listar_produtos(self) -> None:
        """Função que lista o estoque de produtos disponíveis.
        """
        print("="*37)
        print("## ESTOQUE DE PRODUTOS DISPONÍVEIS ##")
        print("="*37, "\n")

        for p in self.produtos:
            print(f"- Há {self.produtos.count(p)} {p.name} no estoque (código: {p.codigo}, preço: {p.preco})")


# exemplo
produto1 = Produto("PC DELL", 12345, 4500.00, Tipo_Produto.COMPUTADOR)
produto2 = Produto("SANSUNG J2 PRIME", 10010, 1000.00, Tipo_Produto.CELULAR)
produto3 = Produto("NOTEBOOK ACER", 11111, 2000.0, Tipo_Produto.NOTEBOOK)
produto4 = Produto("YURE", 11111, 2000.0, Tipo_Produto.NOTEBOOK)

Inventario().repor_produto(produto1)
Inventario().repor_produto(produto2)
Inventario().repor_produto(produto3)
Inventario().vender_produto(produto4)
Inventario().listar_produtos()


    


