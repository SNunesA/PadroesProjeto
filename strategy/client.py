from rich import print #pip install rich
# from strategies import encrypt_md5, encrypt_sha1 esta linha nao e mais necessario
from context import HashContext
from strategies import create
# def select_strategy():
#     """ 
#     Helper function - read user choice
#     """
#     print("-"*40)
#     print("Algoritmos Hash disponiveis")
#     print("-"*40)
#     print("""
#     1 - md5
#     2 - sha1
#     """)
    # choice = int(input("Escolha a opção: "))
    # from strategies import MD5Strategy, SHA1Strategy
    # # obs: essa logica poderia ser encapsulada numa factory
    # if choice==1: 
    #     strategy=MD5Strategy()
    # elif choice==2:
    #     strategy=SHA1Strategy()
    # else:
    #     raise ValueError("invalid choice")
    # return strategy

#classe cliente 
if __name__ == "__main__":
    """ Runtime """

    print("-"*40)
    print("Algoritmos Hash disponiveis")
    print("-"*40)
    print("""
    MD5
    SHA1
    SHA256
    """)
    #factory
    strategy = create(input("Digite o Hash:"))
    password = input("Digite a senha: ")

    #print(encrypt_sha1(password))
    #print(encrypt_md5(password))

    context = HashContext(strategy)
    hpass=context.hash(password) #senha criptograda
    print(f"\n[cyan]{hpass}[/]\n")
    print("━"*40)