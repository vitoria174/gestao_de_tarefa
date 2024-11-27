#gestao de tarefas

lista_tarefas=[]


#funçao das escolhas
def criar():
    tarefa=str(input('Tarefa:'))
    dados={'[]':tarefa}

    lista_tarefas.append(dados)
    print(lista_tarefas)

#funcao para visualização
def visualizar():
    for ver in lista_tarefas:
        print(ver)

#codigo principal
while True:
    print('1-Criar Tarefa\n'
          '2-Visualizar\n'
          '3-Atualizar\n'
          '4-Deletar [Completas]\n'
          '0-Sair')
    escolha=int(input('Digite uma opção:'))
    if escolha == 1 :
        criar()
    if escolha ==2:
        visualizar()
    if escolha ==0:
        break