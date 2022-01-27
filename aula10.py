#entrada e saida de arquivos.

#open('arquivo.txt', 'w')   #metodo leva 2 argumentos, o primeiro é o nome do arquivo e o segundo é o modo de abertura. r = read, w = write, r+ = read write, a = append(adicionar). Todos são para abrir arquivos de textos
                           #b = bytes. Para abrir arquivos que não são de textos, rb=read bytes(faz a leitura) 


# arquivo = open('arquivo.txt', 'w')
# arquivo = open('arquivo.txt', 'a')


# for i in range(0, 1001):
#     arquivo.write("bbbbbbb "+ str(i)+'\n')

# arquivo = open('arquivo.txt', 'r')

# print(arquivo.read())
# for linha in arquivo:
#     print(str(linha))


# arquivo = open('logo.jpg', 'rb')

# print(arquivo.read())