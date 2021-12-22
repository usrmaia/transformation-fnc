from string import ascii_lowercase
from os import system

symbols = ascii_lowercase + ">#^&-()"

def verify_syntax(formula):
    for symbol in formula:
        if not symbol in symbols:
            # Se símbolo da formula NÃO faz parte do conjunto de símbolos
            print(f"Símbolo '{symbol}' inválido!")
            return False
    return True

if __name__ == "__main__":
    system("cls")
    #system("clear")
    while True:
        formula = input("Fórmula: ")
        if formula == 'q': break
        print(verify_syntax(formula))