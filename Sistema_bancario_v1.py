
def main():
    saldo = 0
    limite_saque = 500
    LIMITE_SAQUES = 3
    extrato = []
    numero_saques = 0

    while True:
        opcao = input("""
Operações disponíveis:
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=> """)

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor inválido! O depósito deve ser positivo.")

        elif opcao == "2":
            if numero_saques >= LIMITE_SAQUES:
                print("Limite diário de saques atingido (3 saques por dia)!")
            else:
                valor = float(input("Informe o valor do saque: "))
                if valor > 0:
                    if valor <= limite_saque:
                        if valor <= saldo:
                            saldo -= valor
                            extrato.append(f"Saque: R$ {valor:.2f}")
                            numero_saques += 1
                            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                        else:
                            print("Saldo insuficiente!")
                    else:
                        print(f"Valor do saque excede o limite de R$ {limite_saque:.2f} por transação!")
                else:
                    print("Valor inválido! O saque deve ser positivo.")

        elif opcao == "3":
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                print("\n========= Extrato Bancário =========")
                for movimento in extrato:
                    print(movimento)
                print(f"\nSaldo atual: R$ {saldo:.2f}")
                print("====================================")

        elif opcao == "0":
            print("Saindo do sistema. Obrigado por usar nosso banco!")
            break

        else:
            print("Operação inválida! Por favor, selecione novamente a opção desejada.")

if __name__ == "__main__":
    main()
