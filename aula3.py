#

#comparações : == != > < >= <=
#comparação: and or

# var_verdade = True
# var_falso = False

# if var_verdade == True:
#     print('var_verdade é verdadeiro')
# a = input('Digite um Numero: ')
# b = input('Digite um Numero: ')

# if a > b:
#     print(a,'é maior do que ', b)
# else:
#     print(a,'é menor do que ', b)

# if a > b and ('Abacate' == 'Maçã') or 2 == 2:
#     print('Algum é Verdadeiro')
# else:
#     print('Algum é falso')
# print('opcoes: \n 1 = red pill\n 2= Blue pill\n 3 misture as duas kkkk')

# opcao = input('Escolha uma opção: ')

# if opcao == '1':
#     print('Voce virou o rei do capa')
# elif opcao == '2':
#     print('Seu nome agora é juninho')
# elif opcao =='3':
#     print('Voce agr é o juninho rei do capa, Piscou tomou')
# else:
#     print('Coé meno, escolhe uma das 3 opcoes ai')



# if not True:
#     print('Entrou no if')
# else:
#     print('Entrou no else')

'''faca um programa que pergunte a idade o peso e a altura de uma pessoa e decide se ela está apta para ser do Exercito
Para entrar no exercito é preciso ter 18 anos ou mais, pesar mais ou igual 60 kg e medir mais ou igual a 1,70m
'''

print('Ficha de inscrição para o Exercito Brasileiro')
nome = input('Digite seu nome: ')
idade = int (input('Digite sua idade: '))
peso = float (input('Digite seu Peso: '))
altura = float (input('Digite sua altura: '))

if idade >= 18 and peso >= 60.0 and  altura >= 1.70:
    print('Parabens! Voce começa amanha soldado', nome,', estando aqui 5H da madruga voce já está atrasado :)')
else:
    print('Infelizmente voce não tem os requisitos para servir o Exercito brasileiro :/')


#Resolução

# idade = int(input('Escreva sua idade: '))
# peso = float(input('Escreva seu peso: '))
# altura = float(input('Escreva sua altura: '))

# if idade >= 18 and peso >= 60 and altura >= 1.70:
#     print('Voce esta apto a servir o exercito')
# else:
#     print('Voce nao esta apto')
