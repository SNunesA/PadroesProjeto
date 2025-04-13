from context import FreteContext, select_strategy

if __name__ == "__main__":
    """ Runtime """
    valor=float(input("Digite o valor do produto:"))
    peso=int(input("Digite o peso do produto:"))
    strategy = select_strategy()
    context = FreteContext(strategy)
    
    total=context.calcular(valor,peso)
    print("Valor total:R$",total)
    
    