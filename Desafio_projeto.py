menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 100
limite = 500
extrato = ""

numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n")
            print("\n")
            print("========================================")
            print("=============== DEPÓSITO ===============")
            print("\n")
            print(f"Foi depositado R$ {valor:.2f} em sua conta!\n")
            print("\n")
            print("========================================")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n")
            print("\n")
            print("=====================================")
            print("=============== SAQUE ===============")
            print("\n")
            print("Operação falhou! Saldo suficiente.")
            print("\n")
            print("======================================")
            

        elif excedeu_limite:
            print("\n")
            print("\n")
            print("=====================================")
            print("=============== SAQUE ===============")
            print("\n")
            print("Operação falhou! Execeu o limite de saque.")
            print("\n")
            print("======================================")
            

        elif excedeu_saques:
            print("\n")
            print("\n")
            print("=====================================")
            print("=============== SAQUE ===============")
            print("\n")
            print("Operação falhou! Saques excedido.")
            print("\n")
            print("======================================")
            

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n")
            print("\n")
            print("=====================================")
            print("=============== SAQUE ===============")
            print("\n")
            print(f"Valor de saque foi de R$ {valor:.2f}\n")
            print("Obrigado por usar nosso sistema bancário!")
            print("\n")
            print("======================================")

        else:
            print("Valor inválido. Tente novamente.")

    elif opcao == "3":
        print("\n")
        print("=========================================")
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        print("\n")
        print("saindo...")
        print("=========================================")
        print("\n=======================================")
        print("Obrigado por usar nosso sitema bancário!")
        print("                 👍😊")
        print("\n")
        print("\n")
        print("==========================================")
        
        break
        
    else:
        print("Opção inválida, tente novamente.")



