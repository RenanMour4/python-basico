# Tratamentos de erros
import time
# try:
#     a = 2/0
#     aesfs
#     print("deu certo")
# except ZeroDivisionError:
#     print("Divisão por 0")
# except NameError:
#     print("erro de sintaxe")

# try:
#     a = 2/0
# except Exception as erro:
#     print("Aconteceu um erro: ", erro)

def abre_arquivo():
    try:
        open('Arquivodoido.txt')
        return True
    except Exception as erro:
        print('Acontecru um erro:', erro)
        return False

while not abre_arquivo():
    print('Tentando abrir o arquivo')
    time.sleep(5)

print('Conseguiu abrir o arquivo')
    