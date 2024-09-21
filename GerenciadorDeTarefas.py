
# Crie um programa para gerenciar uma lista de tarefas. O programa deve ser
# executado continuamente e deve oferecer as seguintes funcionalidades:

# Adicionar Tarefa

# Remover Tarefa

# Exibir Tarefas

# Buscar Tarefa

# Contar Tarefas

# Substituir Tarefa

# Inverter Ordem das Tarefas

# Implemente cada funcionalidade como uma função


def adicionar_Tarefa(listaTodasTarefas):
    tarefa = input()
    listaTodasTarefas.append(tarefa)
    return listaTodasTarefas
        
def remover_Tarefa(listaTodasTarefas):
    for _ in listaTodasTarefas:
        tarefa = input()
        listaTodasTarefas.remove(tarefa)
    return listaTodasTarefas 
       
def exibir_Tarefas(listaTodasTarefas):
    return listaTodasTarefas
    
def buscar_Tarefas(listaTodasTarefas):
    tarefa = input()
    if tarefa in listaTodasTarefas:
        print(f"Essa tarefa existe")
    else:
        print(f"Essa tarefa não existe")
   
def contarTarefas(listaTodasTarefas):
   print(f"Existem {len(listaTodasTarefas)} Tarefas")

def substituir_Tarefa(listaTodasTarefas,i,tarefa_nova):
    tarefa = input()
    if tarefa in listaTodasTarefas:        
        print(f"Agora digite a nova tarefa: ")        
        tarefa_nova = input()
        i = listaTodasTarefas.index(tarefa)
        listaTodasTarefas[i] = tarefa_nova    
        print(f"Tarefa '{tarefa}' substituída por '{tarefa_nova}'.")
    else:
        print(f"Essa tarefa não existe")
        
def Inverter_Ordem_das_Tarefas(listaTodasTarefas):
    listaTodasTarefas.reverse()
    print(f"Ordem das tarefas invertida.")

listaTodasTarefas = []
tarefa = ''
tarefa_nova = ''
i = ''

while True:
    
    print("Selecione um numero para a função desejada: ")
    print("1 - Adicionar Tarefa")
    print("2 - Remover Tarefa")
    print("3 - Exibir Tarefas")
    print("4 - Buscar Tarefa")
    print("5 - Contar Tarefas")
    print("6 - Substituir Tarefa")
    print("7 - Inverter Ordem das Tarefas")
    print("0 - Interromper o programa")
    
    funcaoSelecionada = int(input())
    
    if funcaoSelecionada == 0:
        break
    
    elif funcaoSelecionada == 1:
        print("Digite a Nova Tarefa: ")
        adicionar_Tarefa(listaTodasTarefas)
        if tarefa != 0:
            print("Tarefa Adicionada com sucesso")
    
    elif funcaoSelecionada == 2:
        print("Digite tarefa para remover: ")
        remover_Tarefa(listaTodasTarefas)
        if tarefa != 0:
            print("Tarefa Removida com sucesso")
    
    elif funcaoSelecionada == 3:
        print("Lista com todas as tarefas")
        exibir_Tarefas(listaTodasTarefas)
        print(listaTodasTarefas)
        
    elif funcaoSelecionada == 4:
        print("Digite a tarefa Que deseja: ")
        buscar_Tarefas(listaTodasTarefas)
        
    elif funcaoSelecionada == 5:
        contarTarefas(listaTodasTarefas)
    
    elif funcaoSelecionada == 6:
        print("Digite a tarefa Que deseja substituir: ")
        substituir_Tarefa(listaTodasTarefas,i,tarefa_nova)
    
    elif funcaoSelecionada == 7:
        Inverter_Ordem_das_Tarefas(listaTodasTarefas)
    

