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
            raise ExcecaoTransacaoVenda(produto.name)
            

    def retornar_produto(self, produto: Produto) -> None:
        """Função que retorna um produto vendido para o estoque, caso este tenha sido vendido.
        """
        if produto in self.produtos_vendidos:
            self.produtos.append(produto) # produto retornado
            self.produtos_vendidos.remove(produto)
            print(f"{produto.name} (código: {produto.codigo}) foi retornado (valor: R$ {produto.preco:.2f}).")
        else:
            raise ExcecaoTransacaoRetorno(produto.name)

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

# ----------------------------------------------------------------------------

# exemplos (computadores)
produto1 = Produto("PC DELL", 12345, 5999.90, Tipo_Produto.COMPUTADOR)
produto2 = Produto("PC LENOVO", 55555, 1549.49, Tipo_Produto.COMPUTADOR)

# exemplos (notebooks)
produto3 = Produto("NOTEBOOK ACER", 10000, 3499.99, Tipo_Produto.NOTEBOOK)
produto4 = Produto("NOTEBOOK POSITIVO", 22222, 3000.0, Tipo_Produto.NOTEBOOK)

# exemplos (celulares)
produto5 = Produto("CELULAR SANSUNG", 67676, 1000.00, Tipo_Produto.CELULAR)
produto6 = Produto("CELULAR IPHONE", 10010, 5010.95, Tipo_Produto.CELULAR)
produto7 = Produto("CELULAR MOTOROLA", 99999, 2999.39, Tipo_Produto.CELULAR)

# repondo estoque
Inventario().repor_produto(produto1)
Inventario().repor_produto(produto1)
Inventario().repor_produto(produto1)
Inventario().repor_produto(produto2)
Inventario().repor_produto(produto2)
Inventario().repor_produto(produto3)
Inventario().repor_produto(produto3)
Inventario().repor_produto(produto4)
Inventario().repor_produto(produto4)
Inventario().repor_produto(produto5)
Inventario().repor_produto(produto6)

# listando produtos apos reposição de estoque
Inventario().listar_produtos()

# vendendo produtos
Inventario().vender_produto(produto1)
Inventario().vender_produto(produto1)
Inventario().vender_produto(produto2)
Inventario().vender_produto(produto2)
Inventario().vender_produto(produto5)

# listando produtos após vendas
Inventario().listar_produtos()

# retornando
Inventario().retornar_produto(produto1)
Inventario().retornar_produto(produto5)

# listando produtos após retornos
Inventario().listar_produtos()

# exemplo de erro
Inventario().vender_produto(produto7) # o produto7 não está no estoque
Inventario().retornar_produto(produto4) # o produto4 não foi vendido (não irá funcionar porque a linha anterior já gera uma exceção)
