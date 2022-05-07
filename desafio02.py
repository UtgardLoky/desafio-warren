'''
Desafio 02
Um professor de programação, frustrado com a falta de disciplina de seus alunos,
decidi cancelar a aula se menos de x alunos estiverem presentes quando a aula for iniciada.
O tempo de chegada varia entre:

Normal: tempoChegada <= 0
Atraso: tempoChegada > 0
Construa um algoritmo que dado o tempo de chegada de cada aluno e o limite x de alunos presentes,
 determina se a classe vai ser cancelada ou não ("Aula cancelada” ou “Aula normal”).

Exemplo:

Entrada de dados:
x = 3
tempoChegada = [-2, -1, 0, 1, 2]

Saída de dados:
Aula normal.

Explicação:
Os três primeiros alunos chegaram no horário. Os dois últimos estavam atrasados.
 O limite é de três alunos, portanto a aula não será cancelada.
'''
# Declarações
tempoChegada = [-2, -1, 0, 1, 2]
alunos = 0

# Analisa tempo dos alunos e contabiliza quantidade de alunos chegaram na hora
for x in tempoChegada:
    if x <=0:
        alunos += 1
# Verifica se quórum minimo de alunos foi alcançado e exibe resposta
if alunos >= (len(tempoChegada)/2):
    print(f'Aula normal,{alunos} alunos chegaram no horário ')
else:
    print('Aula cancelada, a turma não atigiu o numero minimo de aluanos')
