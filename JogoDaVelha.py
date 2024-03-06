import time
from ascii import apresentacao

def tabuleiro(elemento :list)-> None:
    """Metodo para fazer o tabuleiro,possui uma lista de 'strings'
    como argumento para mostrar o tabuleiro"""
    print()
    print(f"{elemento[0]} | {elemento[1]} | {elemento[2]}")
    print(f"{elemento[3]} | {elemento[4]} | {elemento[5]}")
    print(f"{elemento[6]} | {elemento[7]} | {elemento[8]}")

print(apresentacao)
print("Clique ENTER para começar o jogo:")
input()

print("Carregando...")

time.sleep(2)

def nomear_jogador(numero: int , simbolo: str) -> str:
    """verifica se o nome do jogador é valido"""
    while True:
        print(f"\nJogador {numero}({simbolo}), digite seu nome:")
        nome_jogador = input().title()
        if nome_jogador != "":
            return nome_jogador

        print("nome invalido,digite novamente: ")

jogador1 = nomear_jogador("circulo",1)
jogador2 = nomear_jogador("x",2)

print("Como funciona: ")
print("Cada casa é numerada,Veja como é: ")

tabuleiro([numbers for numbers in range(1, 10)])

print("Para ganhar é necessario ter o seu simbolo em 3 casas consecutivos!")

time.sleep(3)

print(f"Jogador{jogador1}(circulo) vs {jogador2}(x)")


