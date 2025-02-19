# Vamos praticar o uso de estruturas condicionais como o if, else e elif a partir de algumas atividades. Agora que estamos avançando nos conteúdos, podemos tornar os desafios mais interessantes: vamos trabalhar com projetos de código! Solucione os problemas de aquecimento para se preparar para os projetos:
def requesitar_lista(mensagem, comprimento):
    '''Requesita um input com a mensagem '[mensagem],  separados por vírgula:' e retorna uma lista com o comprimento pedido.
    
    Repete o input caso o usuário não tenha passado a quantidade certa de dados.'''

    lista = []
    while len(lista) != comprimento:
        lista = input('{}, separados por vírgula: '.format(mensagem)).split(',')
    
    return lista

def formatar_lista(lista):
    '''Converte todos os items de uma lista em float.'''
    i = 0
    while i < len(lista):
        lista[i] = float(lista[i])
        i+=1
    return lista

# Aquecendo na programação
# Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
num1 = float(input('Número 1: '))
num2 = float(input('Número 2: '))
print('{} > {}'.format(num1, num2) if num1>num2 else '{} > {}'.format(num2,num1))
print()

# Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).
percentual = float(input('Percentual de crescimento: '))
print('Houve um crescimento.' if percentual>0 else 'Houve um decrescimento.')
print()

# Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
vogais = ['a', 'e', 'i', 'o', 'u']
letra = '...'
while len(letra) > 1:
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Digite apenas UM caractere.')
print(letra, 'é vogal.' if letra in vogais else 'não é vogal.')

# Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
precos = []
while len(precos) != 3:
    precos = input('Digite três preços de carro, separados por vírgula: ').split(',')

# i = 0
# while i < len(precos):
#     precos[i] = float(precos[i])
#     i+=1
precos = formatar_lista(precos)

print('Mais barato: {}\n'.format(min(precos)))

# Escreva um programa que leia três números e os exiba em ordem decrescente.
numeros = requesitar_lista('Digite três números', 3)
numeros = formatar_lista(numeros)

numeros.sort(reverse=True)
print(*numeros, sep = ' > ')
print()

# Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.
respostas = {
    'manhã':'Bom dia!',
    'tarde':'Boa tarde!',
    'noite':'Boa noite!'}
turno = ''

while turno not in respostas:
    turno = input('Em qual turno estuda? ').lower()
    if turno not in respostas:
        print('Resposta inválida.')

print(respostas[turno])
print()


# Momento dos projetos
# Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.
nums = requesitar_lista('Digite dois números', 2)
nums = formatar_lista(nums)

operacoes = {
    '+':nums[0]+nums[1],
    '-':nums[0]-nums[1],
    '*':nums[0]*nums[1],
    '/': 'Inválido, o denominador não pode ser 0.' if nums[1] == 0 else nums[0]/nums[1]
}

operacao = ''
while operacao not in operacoes:
    operacao = input('Digite o tipo de operação (+, -, *, /): ')

resultado = operacoes[operacao]
print('O resultado {} é {}, {} e {}\n'.format(resultado, 'par' if resultado%2==0 else 'ímpar', 'positivo' if resultado>=0 else 'negativo', 'inteiro' if resultado%1==0 else 'decimal'))

# 11) Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes.
lados = requesitar_lista('Digite três comprimentos de lados', 3)
lados = formatar_lista(lados)

if (lados[0] + lados[1] > lados[2]) and (lados[0] + lados[2] > lados[1]) and (lados[1] + lados[2] > lados[0]):
    if lados[0] == lados[1] == lados[2]:
        tipo = 'equilátero'
    elif lados[0] == lados [1] or lados[0] == lados[2] or lados[1] == lados[2]:
        tipo = 'isósceles'
    else:
        tipo = 'escaleno'
    print ('O triângulo é {}.'.format(tipo))
else:
    print('Esses lados não formam um triângulo válido.\n')

# 12) Um estabelecimento está vendendo combustíveis com descontos variados.
# Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro.
# Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro.
# O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. 
# Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:
# O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
# O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
combustivel_preco = {
    'e': {
        'preco':1.7,
        'desconto':0.02,
        'desconto_15':0.04
        },
    'd': {
        'preco':2.0,
        'desconto':0.03,
        'desconto_15':0.05
        }
    }
tipo = ''
while tipo not in combustivel_preco:
    tipo = input('Digite o tipo de combustível (D = diesel, E = etanol): ').lower()
    if tipo not in combustivel_preco:
        print('Inválido. Tente novamente.')
quantidade = float(input('Digite a quantidade de litros vendidos: '))

preco = combustivel_preco[tipo]['preco']
if quantidade > 15:
    desconto = combustivel_preco[tipo]['desconto_15']
else:
    desconto = combustivel_preco[tipo]['desconto']

valor = preco*quantidade*(1 - desconto)
print('O valor a ser pago é R${:.2f}.\n'.format(valor))


# 13) Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:
# Para variação acima de 20%: bonificação para o time de vendas.
# Para variação entre 2% e 20%: pequena bonificação para time de vendas.
# Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
# Para bonificações abaixo de -10%: corte de gastos.

def requesitar_lista(mensagem, comprimento):
    '''Requesita um input com a mensagem '[mensagem],  separados por vírgula:' e retorna uma lista com o comprimento pedido.
    
    Repete o input caso o usuário não tenha passado a quantidade certa de dados.'''

    lista = []
    while len(lista) != comprimento:
        lista = input('{}, separados por vírgula: '.format(mensagem)).split(',')
    
    return lista

def formatar_lista(lista):
    '''Converte todos os items de uma lista em float.'''
    i = 0
    while i < len(lista):
        lista[i] = float(lista[i])
        i+=1
    return lista

vendas = requesitar_lista('Digite as quantidades de vendas para 2022 e 2023', 2)
vendas = formatar_lista(vendas)

variacao = (vendas[1] - vendas[0])/vendas[0]*100
if variacao >=20:
    txt = 'Bonificação para o time de vendas.'
elif variacao >=2:
    txt = 'Pequena bonificação para o time de vendas.'
elif variacao >= -10:
    txt = 'Planejamento de políticas de incentivo às vendas.'
else:
    txt = 'Corte de gastos.'

print('A variação foi de {:.2f}%, e o recomendado é: {}'.format(variacao, txt))