# Vamos praticar o uso de vários tipos de variáveis e da função input a partir de algumas atividades. Solucione os problemas propostos em código.

# Coleta e amostragem de dados
# Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
altura = input('Digite sua altura (metros): ')
print('Olá, {}! Você tem {} anos e {} metros.\n'.format(nome, idade, altura))



# Calculadora com operadores
# Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.
val1 = float(input('Valor 1: '))
val2 = float(input('Valor 2: '))
val3 = float(input('Valor 3: '))
print('{} + {} = {}'.format(val1,val2,val1+val2))

# Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.
print('{} + {} + {} = {}'.format(val1, val2, val3, val1+val2+val3))

# Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.
print('{} - {} = {}'.format(val1, val2, val1-val2))

# Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
print('{} x {} = {}'.format(val1, val2, val1*val2))

# Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores.
# Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores.
# Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores.
# Deixe claro que o valor do denominador não pode ser 0.

numerador = float(input('Numerador: '))
for i in range(10):
    denominador = float(input('Denominador: '))
    if denominador != 0 :
        break
    else:
        print('O denominador não pode ser 0.')
    if i+1 == 10:
        exit()
print('{} / {} = {}'.format(numerador, denominador, numerador/denominador))
print('{} / {} = {:.0f}, resto {:.0f}\n'.format(numerador, denominador, numerador//denominador, numerador%denominador))

# Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
operador = float(input('Operador: '))
potencia = float(input('Potência: '))
print('{}^{} = {}\n'.format(operador, potencia, operador**potencia))

# Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
print('Média: {:.1f}'.format((nota1+nota2+nota3)/3))

# Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.
print('Média ponderada (peso 1, 2, 3 e 4) de 5, 12, 20 e 15: {}'.format((5*1+12*2+20*3+15*4)/10))

# Editando textos
# Crie um código que solicite uma frase e depois imprima a frase na tela.
frase = input('Frase: ')
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
print(frase.upper())
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.
print(frase.lower())
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.
print(str(frase.strip()))
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
print((frase.lower().strip()))
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.
print((frase.replace('e', 'f')))
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
print((frase.replace('a', '@')))
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
print((frase.replace('s', '$')))


