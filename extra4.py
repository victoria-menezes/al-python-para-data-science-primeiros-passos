# Vamos praticar o uso de estruturas de repetição como o while e o for a partir de algumas atividades. Agora que estamos avançando nos conteúdos, podemos tornar os desafios mais interessantes. Para isso, vamos trabalhar com projetos de código!
def requesitar_lista(mensagem, comprimento):
    '''Requesita um input com a mensagem '[mensagem],  separados por vírgula:' e retorna uma lista com o comprimento pedido.
    
    Repete o input caso o usuário não tenha passado a quantidade certa de dados.'''

    lista = []
    while len(lista) != comprimento:
        lista = input('{}, separados por vírgula: '.format(mensagem)).split(',')
    
    return lista

def formatar_lista(lista, type = 'float'):
    '''Converte todos os items de uma lista para a estrutura pedida.
    
    Parameters
    ----------
    lista : list
        Lista a ser formatada.
    type : {'float', 'int', 'str'}
        Tipo a ser convertido.

    Returns
    -------
    lista : list

    '''
    i = 0

    if type == 'float':
        while i < len(lista):
            lista[i] = float(lista[i])
            i+=1
    elif type == 'int':
        while i < len(lista):
            lista[i] = int(lista[i])
            i+=1
    elif type == 'str':
        while i < len(lista):
            lista[i] = str(lista[i])
            i+=1
    else:
        raise ValueError('Tipo inválido.')
    
    return lista

# Primeiro, vamos solucionar alguns problemas para aquecer e nos prepararmos para os projetos.
# Aquecendo na programação
# 1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
nums = requesitar_lista('Digite dois números inteiros',2)
nums = formatar_lista(nums, 'int')
nums.sort()

for i in range(nums[0],nums[1]+1):
    print(i)
# 2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.
bac_A = 4
bac_B = 10
dias = 0

while bac_A < bac_B:
    bac_A *=1.03
    bac_B *=1.015
    dias+=1

print('A: {}\nB: {}\n{} dias.\n'.format(bac_A, bac_B, dias))

# 3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.
notas = []
for i in range(15):
    notas.append(-1)
    while notas[i] > 5 or notas[i] < 0:
        notas[i] = float(input('Insira a nota da pessoa {}: '.format(i+1)))
        if 5 >= notas[i] >= 0:
            break
        print('A nota dever estar entre 0 e 5.')
print('Notas válidas.\n')

# 4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.
valor = 0
contagem = 0
total = 0
while valor != -273:
    valor = float(input('Insira uma temperatura em Celsius: '))
    if valor == -273:
        break
    contagem += 1
    total += valor
print('A média é {}C.\n'.format(total/contagem))

# 5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.
valor = int(input('Calcular fatorial de: '))
fat = 1
for i in range(1,valor+1):
    #print(fat, i)
    fat*=i

print('{}! = {}'.format(valor,fat))

# Momento dos projetos
# 6) Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:
# Tabuada do 2:
# 2 x 1 = 2
# 2 x 2 = 4
# [...]
# 2 x 10 = 20
valor = int(input('Mostrar a tabuada do: '))
i = 1
while i <= 10:
    print('{} x {} = {}'.format(valor, i, valor*i))
    i+=1

# 7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
valor = int(input('Digite um número: '))
primo = True
for i in range(2,valor):
    if valor%i == 0:
        primo = False
        break

print('O número {}{} é primo.'.format(valor, '' if primo else ' não' ))

# 8) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:
# Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
# Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
# Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.

contagem_votos = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0
}


for i in range (0,20):
    voto = -1
    while voto not in contagem_votos:
        voto = input('Insira o voto {}: '.format(i+1))
        if voto in contagem_votos:
            contagem_votos[voto]+=1
            break
        print('Voto inválido. O voto deve ser 1, 2, 3, 4, 5 (nulo) ou 6 (branco).')

print('\nResultados:')

for i, votos in enumerate(contagem_votos):
    if i+1 == 5:
        candidato = 'Nulo'
    elif i+1 == 6:
        candidato = 'Branco'
    else:
        candidato = 'Candidato {}'.format(i+1)
    print('{}: {} votos{}'.format(
        candidato, 
        contagem_votos[str(i+1)], 
        ' ( {:.2f}% )'.format(100*contagem_votos[str(i+1)]/20) if i+1 == 5 or i+1 == 6 else ''))