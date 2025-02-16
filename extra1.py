# Vamos praticar o uso da função print com algumas atividades. Para isso, solucione os problemas propostos em código:

# Imprima a frase Escola de Dados da Alura!.
print('Escola de Dados da Alura!\n')

# Imprima seu nome e seu sobrenome seguindo a estrutura abaixo:
# Nome: [seu nome]
# Sobrenome: [seu sobrenome]
nome = 'Victoria'
sobrenome = 'Menezes'
print('Nome: {}\nSobrenome: {}\n'.format(nome, sobrenome))

# Imprima o seu primeiro nome letra a letra. Por exemplo, meu nome é Mirla, então eu obtenho a seguinte saída:
# M
# I
# R
# L
# A
for i in 'Victoria'.upper():
    print(i)
print()

# Imprima o dia do seu nascimento em formato dia mês ano. Lembrando que os valores de dia e ano não podem estar entre aspas. Supondo uma data de aniversário dia 28 de fevereiro de 2003, o formato deve estar como no exemplo abaixo:
# 28 fevereiro 2003
dia = 28
mes = 'fevereiro'
ano = 2003
print('{} {} {}\n'.format(dia, mes, ano))

# Imprima, em um único print, o atual ano que você está fazendo esse curso. O valor do ano deve ser um dado numérico e a saída do print deve ser a seguinte:
# Ano atual: [ano]
ano_atual = 2024
print('Ano atual: {}'.format(ano_atual))