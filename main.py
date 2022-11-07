altura_metros: float
peso_quilos: float

def imprime_menu():
    print("\nOpções:\n"
          "0: Sair\n"
          "1:Calcular IMC\n")


def calcula_imc(altura, peso):
    return peso / altura ** 2


def resultado_estado_de_saude(imc):
    if imc < 16:
        return "Magreza grave"
    elif imc < 17:
        return "Magreza moderada"
    elif imc < 18.5:
        return "Magreza leve"
    elif imc < 25:
        return "Saudável"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade Grau I"
    elif imc < 40:
        return "Obesidade Grau II (severa)"
    else:
        return "Obesidade Grau III (mórbida)"

imprime_menu()
opcao = float(input())
while opcao != 0:
    altura_metros = float(input("insira a altura em metros"))
    peso_quilos = float(input("insira o peso em quilos"))
    imc = calcula_imc(altura_metros, peso_quilos)
    print(imc)
    print(resultado_estado_de_saude(imc))
    imprime_menu()
    opcao = input()