import mysql.connector
import os
# conectar ao mysql
conexao = mysql.connector.connect(
    host='',
    user='',
    password='',
    database='',
)
cursor = conexao.cursor()

# menu
def menu():
    print('-'*22 +' MINHAS TAREFAS '+'-'*22)
    print('1) Criar nova Tarefa')
    print('2) Ver Tarefas')
    print('3) Editar Tarefa')
    print('4) Deletar Tarefa')
    print('5) Sair')
    opcao = int(input('>> '))
    while opcao not in [1, 2, 3, 4, 5]:
        print('Valor inválido...')
        opcao = int(input('\n>> '))
    return opcao

# Criar
def create():
    os.system('cls')
    try:
        tarefa = input('Digite a tarefa: ')
        comando = f'INSERT INTO tarefas (Tarefa) VALUES ("{tarefa}")'
        cursor.execute(comando)
        conexao.commit()
        print("\nNova tarefa foi registrada....\n")
    except:
        print('Houve um erro')

# ler 
def read():
    os.system('cls')
    print('-'*22+'TAREFAS'+'-'*22)
    try:
        comando = f'SELECT * FROM tarefas'
        cursor.execute(comando)
        resultados = cursor.fetchall()
        print('ID | TAREFA')
        for i, resultado in enumerate(resultados):
            print(f'{i+1}  | {resultado[1]}')
        print('-'*51)
    except:
        print('Houve um erro')

#atualizar 
def update():
    os.system('cls')
    id_tarefa = int(input('Digite o id da tarefa: '))
    tarefa = input('Digite a tarefa: ')
    try:
        comando = f'UPDATE tarefas SET Tarefa = "{tarefa}" WHERE idTarefas = {id_tarefa}'
        cursor.execute(comando)
        conexao.commit()
        print('\nTarefa atualizada....\n')
    except:
        print('Houve um erro')

# excluir
def delete():
    os.system('cls')
    id_tarefa = int(input('Digite o id da tarefa: '))
    try:
        comando = f'DELETE FROM tarefas WHERE idTarefas = "{id_tarefa}"'
        cursor.execute(comando)
        conexao.commit()
        print('\nTarefa excluida\n')
    except:
        print('Houve um erro')

while True:
    opcao = menu()
    match opcao:
        case 1:
            create()
        case 2:
            read()
        case 3:
            update()
        case 4:
            delete()
        case 5:
            break
    
cursor.close()
conexao.close()