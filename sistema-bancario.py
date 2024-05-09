menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

#DEPOSITO
#evitar valores negativos
    if opcao == "d":

        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operacao falhou! O valor informado é inválido")
#SAQUE
#3 operacoes de saque
#cada saque com limite de 500
    elif opcao == "s":
          valor = float(input("Informe o valor do saque: "))

          excedeu_saldo = valor > saldo
          execedeu_limite = valor > limite
          excedeu_saques = numero_saques >= LIMITE_SAQUES
          
          if excedeu_saldo:
              print("Operação falhou! Você não tem saldo suficiente.")
          elif execedeu_limite:
              print("Operação falhou! O valor do saque excedeu o limite.")
          elif excedeu_saques:
              print("Operação falhou! Número máximo de saques excedido.")
          elif valor > 0:
              saldo -= valor
              extrato += f"Saque: R$ {valor:.2f}\n"
              numero_saques += 1
          
          else:
              print("Operação falhou! Valor informado inválido.")
#EXTRATO
    elif opcao == "e":
        print("\n==================Extrato===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================================")
#deposito e saque com formatacao R$xxx.xx    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada. ")