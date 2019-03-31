import random as rd

def embaralha(palavra):
    r = list(palavra)
    rd.shuffle(r)
    return ''.join(r)

lista = ['abacaxi', 'sapato', 'balão', 'macaco', 'tigre', 'blusa']

sorteado = rd.choice(lista)

resp = ''

print("-----JOGUINHO EMBARALHA-----")
print("\nSerá mostrada uma palavra com as letras embaralhadas e você terá que acertar qual palavra é!\n")

print("Palavra Ebaralhada: %s\n" %embaralha(sorteado))
while resp != sorteado:
    resp = input("Que palavra é: ")
    if resp == sorteado:
        print("\nAcertou Mizeravi! Quem te ensinou!?")
    else:
        print("\nErooou!")

print("\nFim de jogo")