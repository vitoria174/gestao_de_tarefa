#gestao de tarefas

lista_tarefas=[]
tarefas=[]

#funçao das escolhas
def criar():
    tarefas=str(input('Tarefa:'))
    lista_tarefas.append(tarefas)
    print(f'tarefa {tarefas} criada')


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
    print(lista_tarefas)
#deletar tarefas
def deletar():
    if len(lista_tarefas) == 0:
        print('nenhuma tarefa criada')
    else:
        print('vou deletar sua tarefa')
        resposta=str(input('Qual tarefa gostaria de deletar?'))
        print('Tarefa deletada!')

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