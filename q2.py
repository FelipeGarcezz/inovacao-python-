preco_produto = float(input("Digite o preço do produto: "))
frete = 30
imposto = preco_produto/10

def calculaValor():
    if(preco_produto < 100):
        margem = 100/30
        preco_total = preco_produto + frete + imposto
        preco_min = preco_total + preco_total / margem
        print(f"Custo total: {preco_total} \nMargem aplicada: 30%\nPreço mínimo de venda: {preco_min}")
    elif(preco_produto > 500):
        margem = 100/15
        preco_total = preco_produto + frete + imposto
        preco_min = preco_total + preco_total / margem
        print(f"Custo total: {preco_total} \nMargem aplicada: 15%\nPreço mínimo de venda: {preco_min}")
    else:
        margem = 100/20
        preco_total = preco_produto + frete + imposto
        preco_min = preco_total + preco_total / margem 
        print(f"Custo total: {preco_total} \nMargem aplicada: 20%\nPreço mínimo de venda: {preco_min}")

calculaValor()

#custo total < R$100,00: margem 30%
#custo entre 100 e 500: margem 20%
#>500 = 15/100
