"""Módulo Principal"""

import comercio as cmc

if __name__ == "__main__":
    # exemplos (computadores)
    produto1 = cmc.Produto("PC DELL", 12345, 5999.90, cmc.Tipo_Produto.COMPUTADOR)
    produto2 = cmc.Produto("PC LENOVO", 55555, 1549.49, cmc.Tipo_Produto.COMPUTADOR)

    # exemplos (notebooks)
    produto3 = cmc.Produto("NOTEBOOK ACER", 10000, 3499.99, cmc.Tipo_Produto.NOTEBOOK)
    produto4 = cmc.Produto("NOTEBOOK POSITIVO", 22222, 3000.0, cmc.Tipo_Produto.NOTEBOOK)

    # exemplos (celulares)
    produto5 = cmc.Produto("CELULAR SANSUNG", 67676, 1000.00, cmc.Tipo_Produto.CELULAR)
    produto6 = cmc.Produto("CELULAR IPHONE", 10010, 5010.95, cmc.Tipo_Produto.CELULAR)
    produto7 = cmc.Produto("CELULAR MOTOROLA", 99999, 2999.39, cmc.Tipo_Produto.CELULAR)

    # repondo estoque
    cmc.Inventario().repor_produto(produto1)
    cmc.Inventario().repor_produto(produto1)
    cmc.Inventario().repor_produto(produto1)
    cmc.Inventario().repor_produto(produto2)
    cmc.Inventario().repor_produto(produto2)
    cmc.Inventario().repor_produto(produto3)
    cmc.Inventario().repor_produto(produto3)
    cmc.Inventario().repor_produto(produto4)
    cmc.Inventario().repor_produto(produto4)
    cmc.Inventario().repor_produto(produto5)
    cmc.Inventario().repor_produto(produto6)

    # listando produtos apos reposição de estoque
    cmc.Inventario().listar_produtos()

    # vendendo produtos
    cmc.Inventario().vender_produto(produto1)
    cmc.Inventario().vender_produto(produto1)
    cmc.Inventario().vender_produto(produto2)
    cmc.Inventario().vender_produto(produto2)
    cmc.Inventario().vender_produto(produto5)

    # listando produtos após vendas
    cmc.Inventario().listar_produtos()

    # retornando
    cmc.Inventario().retornar_produto(produto1)
    cmc.Inventario().retornar_produto(produto5)

    # listando produtos após retornos
    cmc.Inventario().listar_produtos()

    # exemplo de erro
    cmc.Inventario().vender_produto(produto7) # o produto7 não está no estoque
    cmc.Inventario().retornar_produto(produto4) # o produto4 não foi vendido (não irá funcionar porque a linha anterior já gera uma exceção)
