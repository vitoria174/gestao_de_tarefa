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
    sql = "INSERT INTO tarefas(texto,data_criada) VALUES (%s,%s)"
    valores=(tarefas,data)
    cursor.execute(sql,valores)
    tarefa.commit()
    print(cursor.rowcount,"tarefa criada")

#funcao para visualização
def visualizar():
    cont=0
    for ver in lista_tarefas:
        cont+=1
        print(f'{cont}',ver)

#atualizar tarefas
def atualizar():
    num=int(input('Qual tarefa atualizar:'))
    tarefas=str(input('nova tarefa:'))
    lista_tarefas[num]=tarefas
    print(f'tarefa {lista_tarefas[num]} atualizada')
#deletar tarefas
def deletar():
    if len(lista_tarefas) == 0:
        print('nenhuma tarefa criada')
    else:
        print('vou deletar sua tarefa')
        resposta=int(input('Qual tarefa gostaria de deletar?'))
        lista_tarefas.pop(resposta)
        print(lista_tarefas)

#codigo principal
while True:
    print('-'*20)
    print('1-Criar Tarefa\n'
          '2-Visualizar\n'
          '3-Atualizar\n'
          '4-Deletar [Completas]\n'
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
        deletar()
    if escolha ==0:
        break
        


