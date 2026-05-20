# ====================================
# CONVERSOR DE TEMPERATURA
# Exercício - Engenharia de Software
# Aula 02 - Levantamento de Requisitos
# ====================================
#
# Requisitos Funcionais (RF):
#   RF01: O sistema deve converter temperaturas de Celsius para Fahrenheit
#   RF02: O sistema deve converter temperaturas de Fahrenheit para Celsius
#   RF03: O sistema deve permitir múltiplas conversões sem reiniciar
#   RF04: O sistema deve exibir o resultado formatado com unidade (°C / °F / K)
#
# Requisitos Não-Funcionais (RNF):
#   RNF01: O resultado deve ser exibido imediatamente após a entrada (< 1s)
#   RNF02: A interface deve ser simples e intuitiva (menu com opções numeradas)
#   RNF03: O sistema deve aceitar apenas entradas numéricas válidas (validação)
# ====================================


def celsius_para_fahrenheit(celsius):
    """
    RF01: Converter Celsius para Fahrenheit
    Fórmula: F = (C × 9/5) + 32
    """
    return (celsius * 9 / 5) + 32


def fahrenheit_para_celsius(fahrenheit):
    """
    RF02: Converter Fahrenheit para Celsius
    Fórmula: C = (F - 32) × 5/9
    """
    return (fahrenheit - 32) * 5 / 9


def celsius_para_kelvin(celsius):
    """
    BÔNUS: Converter Celsius para Kelvin
    Fórmula: K = C + 273.15
    """
    return celsius + 273.15


def ler_temperatura(unidade):
    """
    RNF03: Validação de entrada — aceita apenas números.
    Solicita ao usuário uma temperatura até que um valor válido seja digitado.
    """
    while True:
        try:
            valor = float(input(f"Digite a temperatura em {unidade}: "))
            return valor
        except ValueError:
            print("!!  Entrada inválida! Digite apenas números (ex: 25 ou 98.6).\n")


def exibir_menu():
    """Exibe o menu de opções de conversão."""
    print("\nEscolha a conversão:")
    print("  1 - Celsius → Fahrenheit")
    print("  2 - Fahrenheit → Celsius")
    print("  3 - Celsius → Kelvin")
    print("  0 - Sair")


#Programa

print("=" * 40)
print("     CONVERSOR DE TEMPERATURA")
print("=" * 40)

while True:
    exibir_menu()

    opcao = input("Opção: ").strip()

    if opcao == "0":
        print("\nAté mais! ")
        print("=" * 40)
        break

    elif opcao == "1":
        # RF01 — Celsius → Fahrenheit
        temp = ler_temperatura("Celsius")
        resultado = celsius_para_fahrenheit(temp)
        print("=" * 40)
        print(f"  {temp}°C = {resultado:.1f}°F")
        print("=" * 40)

    elif opcao == "2":
        # RF02 — Fahrenheit → Celsius
        temp = ler_temperatura("Fahrenheit")
        resultado = fahrenheit_para_celsius(temp)
        print("=" * 40)
        print(f"  {temp}°F = {resultado:.1f}°C")
        print("=" * 40)

    elif opcao == "3":
        # BÔNUS — Celsius → Kelvin
        temp = ler_temperatura("Celsius")
        resultado = celsius_para_kelvin(temp)
        print("=" * 40)
        print(f"  {temp}°C = {resultado:.2f} K")
        print("=" * 40)

    else:
        print("!!  Opção inválida! Escolha 0, 1, 2 ou 3.\n")