# gestao de projetos

import mysql.connector
from datetime import date


lista_tarefas=[]
tarefas=[]

#integração do banco de dados
tarefa = mysql.connector.connect(
    host="localhost",
    user="root",
    password="albuquerqu",
    database="banco_tarefa"
)

cursor=tarefa.cursor()


#funçao criar tarefas
def criar():
    tarefas=str(input('Tarefa:'))
    data=date.today()
    sql = "INSERT INTO tarefas(texto,data_criada) VALUES (%s,%s)" #inserir na tabela tarefa
    valores=(tarefas,data) #dados do usuario
    cursor.execute(sql,valores)
    tarefa.commit()
    print(cursor.rowcount,"tarefa criada")

#funcao para visualização
def visualizar():
    cursor.execute('SELECT texto FROM tarefas')
    resultado=cursor.fetchall()

    for x in resultado:
        print(x)

#atualizar tarefas
def atualizar():
    num=int(input('Qual tarefa atualizar:'))
    novatarefa=str(input('Nova tarefa:'))
    sql= f"UPDATE tarefas SET texto = '{novatarefa}' WHERE id='{num}'"
    cursor.execute(sql)
    tarefa.commit()
    print(f'tarefa atualizada')
#deletar tarefas
def deletar():
    if visualizar() == 0:
        print('nenhuma tarefa criada')
        print(visualizar())
    else:
        dele=int(input('Qual tarefa deseja deletar:'))
        print('vou deletar sua tarefa')
        sql=f'DELETE FROM tarefas WHERE id= {dele}'
        cursor.execute(sql)
        tarefa.commit()
def marcar():
    cursor.execute("SELECT * FROM tarefas")
    res=cursor.fetchall()
    
    for x in res:
        print(x)
    
    print('[ID da tarefa]')
    marca=int(input("Marcar tarefa:"))
    
    

#codigo principal
while True:
    print('-'*20)
    print('1-Criar Tarefa\n'
          '2-Visualizar\n'
          '3-Atualizar\n'
          '4-Deletar [Completas]\n'
          '5-Marcar tarefas\n'
          '0-Sair')
    print('-'*20)
    escolha=int(input('Digite uma opção:'))
    if escolha == 1 :
        criar()
    if escolha ==2:
        visualizar()
    if escolha == 3:
        atualizar()
    if escolha == 4:
        marcar()
    if escolha == 5:
        marcar()
    if escolha ==0:
        break



