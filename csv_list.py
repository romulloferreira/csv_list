#coding: utf-8
#Começando com os imports
import csv
import matplotlib.pyplot as plt

#Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
    print("Ok!")

#Criar uma função para adicionar as colunas de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    column_list = []
    for genero in data:
        column_list.append(genero[index])
    return column_list[1:]

print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."

# -----------------------------------------------------
input("Aperte Enter para continuar...")
