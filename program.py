class Tarefa:
  def __init__(self, descricao):
    self.descricao = descricao
    self.realizada = False

lista = []
qtdTarefasRealizadas = 0

def adicionarTarefa():
  tarefa = input("Digite a tarefa a ser adicionada: ")
  lista.append(Tarefa(tarefa))

qtdTarefas = int(input("Quantas tarefas serão realizadas? "))

for i in range(qtdTarefas):
  adicionarTarefa()

listaRealizadas = list(filter(lambda x: x.realizada == False, lista))

print("")

def mostrarLista():
  print("\nLista de tarefas:")
  for i in range(len(lista)):
    if (lista[i].realizada):
      print((i + 1), '-', ''.join([u'\u0336{}'.format(c) for c in lista[i].descricao]))
    else: 
      print((i + 1), '-', lista[i].descricao)

mostrarLista()

while (len(listaRealizadas) > 0):
  numTarefa = int(input("\nQual tarefa foi realizada? "))
  lista[numTarefa - 1].realizada = True
  listaRealizadas = list(filter(lambda x: x.realizada == False, lista))
  mostrarLista()
