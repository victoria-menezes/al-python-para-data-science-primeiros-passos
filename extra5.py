from funcoes import requesitar_lista, formatar_lista
# Vamos praticar o uso de estruturas de dados, como as listas e os dicionários, a partir de algumas atividades. Agora que estamos avançando nos conteúdos, podemos tornar os desafios mais interessantes. Para isso, vamos trabalhar com projetos de código!

# Primeiro, vamos solucionar alguns problemas para aquecer e nos prepararmos para os projetos.
# Aquecendo na programação
# 1) Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Com esses valores, faça um programa que calcule a média de gastos. Dica: use as funções built-in sum() e len().
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
media = sum(gastos)/len(gastos)
print('A média de gastos é {}.\n'.format(media))

# 2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.
gastos_altos = 0
for i in gastos:
    if i > 3000:
        gastos_altos+=1
print('{:.2f}% dos gastos foram acima de R$3000.\n'.format(100*gastos_altos/len(gastos)))

# 3) Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].
lista = requesitar_lista('Digite 5 números', 5)
lista = formatar_lista(lista, 'int')
print(lista)

# 4) Imprima a lista em ordem inversa à enviada.
print(lista[::-1])

# 5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.
numero = input('Digite um número: ')
numero = int(numero)
primos = []

for n in range(1,numero+1):
    primo = True
    for i in range(2,n):
        if n%i == 0:
            primo = False
            break
    if primo:
        primos.append(n)

primos.remove(1)
primos = formatar_lista(primos, 'str')

print('Primos entre 1 e {}: {}'.format(numero, ', '.join(primos)))

# 6) Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.
data = input('Digite uma data no formato DD/MM/YYYY: ')
data = data.split('/')
data = formatar_lista(data, 'int')

dia = data[0]
mes = data[1]
ano = data[2]

ano_bissexto = False

if ano%4 == 0:
    ano_bissexto = True
    if ano%100 == 0:
        if ano%400:
            ano_bissexto = True
        else:
            ano_bissexto = False

meses_dias = {
    '1':31,
    '2':29 if ano_bissexto else 28,
    '3':31,
    '4':30,
    '5':31,
    '6':30,
    '7':31,
    '8':31,
    '9':30,
    '10':31,
    '11':30,
    '12':31
}

print('A data é válida.\n' if dia <= meses_dias[str(mes)] else 'A data é inválida.\n')



# Momento dos projetos
# 7) Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias por dia (em milhares) e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).


bacterias_diarias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
crescimento_diario = []
crescimento = 0

for n, bac in enumerate(bacterias_diarias):
    if n == 0:
        crescimento_diario.append(0)
        continue
    crescimento = (bacterias_diarias[n] - bacterias_diarias[n-1])/bacterias_diarias[n-1]
    crescimento_diario.append(crescimento*100)


txt = ', '.join(['{:05.2f}%'.format(c) for c in crescimento_diario])
print('O crescimento foi:\n{}'.format(txt))

# 8) Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.
ids = requesitar_lista('Digite 10 IDs', 10)
ids = formatar_lista(ids, 'int')
doces_qtd = 0
amargos_qtd = 0

for i in ids:
    if i%2==0:
        doces_qtd+=1
    else:
        amargos_qtd+=1

print('{} produtos doces\n{} produtos amargos'.format(doces_qtd, amargos_qtd))


# 9) Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.
# Gabarito da prova:
# 01 - D
# 02 - A
# 03 - C
# 04 - B
# 05 - A
# 06 - D
# 07 - C
# 08 - C
# 09 - A
# 10 - B

respostas_aluno = []
opcoes = ['A', 'B', 'C', 'D']
gabarito = {
    1:'D',
    2: 'A',
    3: 'C',
    4: 'B',
    5: 'A',
    6: 'D',
    7: 'C',
    8: 'C',
    9: 'A',
    10: 'B'
}
nota = 0

for i in range(1,11):
    r = 'Z'
    while True:
        r = input('Questão {:02d}: '.format(i)).upper()
        if r not in opcoes:
            print('ERRO: Opção inválida. Por favor digite A, B, C ou D.')
            continue
        break
    respostas_aluno.append(r)

for i, resposta in enumerate(respostas_aluno, 1):
    if gabarito[i] == resposta:
        nota +=1

print('Sua nota é {:.1f}.\n'.format(nota))

# 10) Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).
meses_temperatura = {
    1: {'nome':'Janeiro','temperatura':0},
    2: {'nome':'Fevereiro','temperatura':0},
    3: {'nome':'Março','temperatura':0},
    4: {'nome':'Abril','temperatura':0},
    5: {'nome':'Maio','temperatura':0},
    6: {'nome':'Junho','temperatura':0},
    7: {'nome':'Julho','temperatura':0},
    8: {'nome':'Agosto','temperatura':0},
    9: {'nome':'Setembro','temperatura':0},
    10: {'nome':'Outubro','temperatura':0},
    11: {'nome':'Novembro','temperatura':0},
    12: {'nome':'Dezembro','temperatura':0}
}

media = 0

for i in meses_temperatura:
    meses_temperatura[i]['temperatura'] = float(input('Temperatura do mês de {}: '.format(meses_temperatura[i]['nome'])))
    media += meses_temperatura[i]['temperatura']

media = media/12
meses_acima_media = []

for i in meses_temperatura:
    if meses_temperatura[i]['temperatura'] > media:
        meses_acima_media.append(meses_temperatura[i]['nome'])

txt = ', '.join(['{}'.format(m) for m in meses_acima_media])
txt = txt[::-1]
txt = txt.replace(' ,', ' e ', 1)
txt = txt[::-1]
print('Os meses acima da média ({:.1f}C) são {}.\n'.format(media, txt))

# 11) Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:
dic = {
    'Produto A': 300,
    'Produto B': 80,
    'Produto C': 60,
    'Produto D': 200,
    'Produto E': 250,
    'Produto F': 30
    }
# Escreva um código que calcule o total de vendas e o produto mais vendido.
print('O total de vendas é {} e o produdo mais vendido é o {}.\n'.format(sum(dic.values()), max(dic, key=dic.get)))


# 12) Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:
# '''
# Tabela de votos da marca
# Design 1 - 1334 votos
# Design 2 - 982 votos
# Design 3 - 1751 votos
# Design 4 - 210 votos
# Design 5 - 1811 votos
# '''
# Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.
marca_votos = {
    'Design 1': 1334,
    'Design 2': 982,
    'Design 3': 1751,
    'Design 4': 210,
    'Design 5': 1811
}

print('O vencedor é {}, que recebeu {} votos.\n'.format(max(marca_votos, key=marca_votos.get), max(marca_votos.values())))

# 13) As pessoas colaboradoras de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do salário devido ao ótimo desempenho do time.
# O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar nos recursos.
# Assim, foi encaminhada para você uma lista com os salários que receberão o abono:
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
# O abono de cada colaborador(a) não pode ser inferior a 200.
# Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento.
# Depois, informe o total de gastos com o abono, quantos(as) colaboradores(as) receberam o abono mínimo e qual o maior valor de abono fornecido.

salarios_abono = {}
for s in salarios:
    salarios_abono[s] = max(s*0.1, 200)

print('O total de gastos será de R${:05.2f}, e o maior abono será de R${:05.2f}.\n'.format(sum(salarios_abono.values()), max(salarios_abono.values())))


# 14) Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta. A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área dessa floresta e armazenou essas informações em um dicionário. Nele, a chave descreve a área dos dados e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.

diversidade_biologica = {
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
    }

# Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica. Dica: use as funções built-in sum() e len().
area_max_diversidade = ''
media_max_especies = 0
for area, especies in diversidade_biologica.items():
    media = sum(especies)/len(especies)
    print(f'{area} tem {media:.1f} espécies em média.')
    if media > media_max_especies:
        area_max_diversidade = area
        media_max_especies = media

print('A {} é a área com mais diversidade biológica, com uma média de {:.1f} espécies.\n'.format(area_max_diversidade, media_max_especies))

# 15) O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:
setor_idades = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
    }
# Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.

soma_idades_total = 0
qtd_colaboradores_total = 0

for setor, idades in setor_idades.items():
    qtd_colaboradores = len(idades)
    soma_idades = sum(idades)
    
    print(f'A idade média do {setor} é {soma_idades/qtd_colaboradores:.1f}')

    qtd_colaboradores_total += qtd_colaboradores 
    soma_idades_total += soma_idades

media_total = soma_idades_total/qtd_colaboradores_total
print(f'A idade média de todos os setores é {media_total:.1f}')

qtd_acima_media = 0
for setor, idades in setor_idades.items():
    qtd_acima_media_setor = 0
    for i in idades:
        if i > media_total:
            qtd_acima_media_setor+=1
    print(f'O {setor} tem {qtd_acima_media_setor} colaboradores com idade acima da média.')
    qtd_acima_media += qtd_acima_media_setor
print(f'Existem {qtd_acima_media} colaboradores com idade acima da média no total.')
