#criar um ssistema bancario com as operacoes:sacar, depositar e visualizar extrato. 

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo= 0
limite= 500
extrato= ""
numero_saques= 0
LIMITE_SAQUES= 3


while True:

    opcao=input(menu)

    if opcao=="d":
        valor=float(input("Informe o valor do deposito:  "))

        if valor> 0:
            saldo+= valor

            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Operacao falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor= float(input("Informe o valor do saque: "))

        excedeu_saldo= valor>saldo

        excedeu_limite= valor>limite

        excedeu_saques= numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operacaco falhou! Voce nao tem saldo suficiente.")


        elif excedeu_limite:
            print("Operacao falhou! O valor do saque escede o limite.")

        elif excedeu_saques:
            print("Operacao falhou! Número máximo de saques excedido.")

        elif valor> 0:
            saldo -= valor
            extrato +=f"Saque: R${ valor:.2f}"
            numero_saques += 1

        else:
            print("Operaco falhou! O valor informado é inválido.")

    elif opcao == "e":
        
        print("\n =========EXTRATO========")
        print("Nao foram realizadas movimentacoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================")
        

    elif opcao =="q":
        break
    else:
        print("Operacao inválida, por favor selecione novamente a operacao desejada.")