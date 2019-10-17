#coding: utf-8
# Desenvolvimento Romullo
# csv_list.py

#Começando com os imports
import csv
import matplotlib.pyplot as plt

__author__ = 'Desenvolvimento Romullo'

#Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
    print("Ok!")

print("")
# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))
print("")

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
print("")
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])
print("")

input("Aperte Enter para continuar...")
print("")



# TAREFA 3
# Vamos mudar o data_list para remover a linha que contém o cabeçalho.
data_list = data_list[1:]

#Criar uma função para adicionar as colunas de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
        Função column_to_list.
        Argumentos:
            data: Parâmetro que pega a lista criada anteriormente a partir do arquivo csv.
            index: Parâmetro que indica o indice.
        Retorna:
            Uma lista de gêneros das primeiras 20 amostras.

        """
    column_list = []
    for genero in data:
        column_list.append(genero[index])
    return column_list

print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."

# -----------------------------------------------------
input("Aperte Enter para continuar...")


# TAREFA 9
# TO-DO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para TO-DO isso, como max() e min().

"""
        Para rodar a TAREFA 9 precisaremos da TAREFA 3,
        Pois na TAREFA 3 foi definido o data_list, onde retiramos o cabeçalho. E na TAREFA 3 criamos o column_to_list.
        Sem isso a TAREFA 9 irá apresentar erro.

        """

trip_duration_list = [int(x) for x in column_to_list(data_list, 2)]
min_trip = trip_duration_list[0]
max_trip = trip_duration_list[0]
mean_trip = 0.
median_trip = 0.

count_trip = 0
total_trip = 0.

for current_trip in trip_duration_list:
  ct = current_trip
  min_trip = min_trip if min_trip < ct else ct
  max_trip = max_trip if max_trip > ct else ct
  total_trip += ct
  count_trip +=1

mean_trip = round(total_trip/count_trip)

def median_calc(lista):
    """
    Função count_user_types.
    Argumentos:
        data_list: Parâmetro que pega a lista.

    Retorna:
        Uma lista com tipos de usuários.

    """

    item_count = len(lista)
    if item_count % 2 == 1:
        return sorted(lista)[item_count//2]
    else:
        return sum(sorted(lista)[item_count//2-1:item_count//2+1])/2.0

median_trip = median_calc(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------
print("")
print("Fim do código!")
print("")
input("Aperte Enter para fechar...")
