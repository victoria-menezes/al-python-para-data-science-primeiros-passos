# Temos uma tabela de informação de empregos quanto ao cargo, quantidade de pessoas empregadas e o salário correspondente:
# Cargo 	Quantidade 	Salário
# Segurança 	5 	3000
# Docente 	16 	6000
# Diretoria 	1 	12500

q_seguranca = 5
s_seguranca = 3000

q_docente = 16
s_docente = 6000

q_diretoria = 1
s_diretoria = 12500

# Precisamos trabalhar com esses dados fornecendo:

# A quantidade total de empregados;
q_total = q_seguranca + q_docente + q_diretoria
print('q_total = {}'.format(q_total))

# A diferença entre o salário mais baixo e mais alto;
s_diferenca = s_diretoria - s_seguranca
print('s_diferenca = {}'.format(s_diferenca))

# A média ponderada da faixa salarial da escola.
s_media = (q_seguranca*s_seguranca + q_docente*s_docente + q_diretoria*s_diretoria)/q_total
print('s_media = {:.2f}'.format(s_media))
