
import json
import os

def carregar_dados(agencia, conta):
    arquivo = f"extrato_{agencia}_{conta}.json"
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            dados = json.load(f)
            return dados['saldo'], dados['extrato'], dados['numero_saques']
    return 0, [], 0

def salvar_dados(agencia, conta, saldo, extrato, numero_saques):
    arquivo = f"extrato_{agencia}_{conta}.json"
    dados = {'saldo': saldo, 'extrato': extrato, 'numero_saques': numero_saques}
    with open(arquivo, 'w') as f:
        json.dump(dados, f)

def main():
    agencia = input("Informe o número da agência (ex.: 1234): ")
    conta = input("Informe o número da conta (ex.: 56789): ")

    saldo, extrato, numero_saques = carregar_dados(agencia, conta)
    limite_saque = 500
    LIMITE_SAQUES = 3

    while True:
        opcao = input(f"""
Operações disponíveis para Agência {agencia} Conta {conta}:
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=> """)

        if opcao == "1":
            try:
                valor = float(input("Informe o valor do depósito: "))
                if valor > 0:
                    saldo += valor
                    extrato.append(f"Depósito: R${valor:.2f}")
                    print(f"Depósito de R${valor:.2f} realizado com sucesso!")
                    salvar_dados(agencia, conta, saldo, extrato, numero_saques)
                else:
                    print("Valor inválido! O depósito deve ser positivo.")
            except ValueError:
                print("Erro: Digite um valor numérico válido!")

        elif opcao == "2":
            if numero_saques >= LIMITE_SAQUES:
                print("Limite diário de saques atingido (3 saques por dia)!")
            else:
                try:
                    valor = float(input("Informe o valor do saque: "))
                    if valor > 0:
                        if valor <= limite_saque:
                            if valor <= saldo:
                                saldo -= valor
                                extrato.append(f"Saque: R${valor:.2f}")
                                numero_saques += 1
                                print(f"Saque de R${valor:.2f} realizado com sucesso!")
                                salvar_dados(agencia, conta, saldo, extrato, numero_saques)
                            else:
                                print("Saldo insuficiente!")
                        else:
                            print(f"Valor do saque excede o limite de R$ {limite_saque:.2f} por transação!")
                    else:
                        print("Valor inválido! O saque deve ser positivo.")
                except ValueError:
                    print("Erro: Digite um valor numérico válido!")

        elif opcao == "3":
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                print(f"\n==== Extrato (Agência {agencia} Conta {conta}) ====")
                for movimento in extrato:
                    print(movimento)
                print(f"\n\n Saldo atual: R${saldo:.2f}")
                print("==============")

        elif opcao == "0":
            print("Saindo do sistema. Obrigado por usar nosso banco!")
            salvar_dados(agencia, conta, saldo, extrato, numero_saques)
            break

        else:
            print("Operação inválida! Por favor, selecione novamente a opção desejada.")

if __name__ == "__main__":
    main()
