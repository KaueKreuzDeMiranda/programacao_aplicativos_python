# Listas, Tuplas e Dicionários

# 1. Listas

# Listas são utilizadas para armazenar vários valores
# dentro de uma única variável

nomes = ["Ana", "Carlos", "João", "Maria"]
print(nomes)

# 2. Acessando elementos da lista

print("")
print(nomes[0])
print(nomes[1])

# Podemos acessar o último elemento usando -1

print("")
print(nomes[-1])

# 3. Alterando elementos

# As listas são mutáveis, ou seja, os elementos podem ser alterados

print("")
nomes[0] = "Pedro"
print(nomes)

# 4. Adicionando elementos

# append() adiciona um elemento no final da lista

print("")
nomes.append("Lucas")
print(nomes)

# insert() adiciona um elemento em uma posição

nomes.insert(1, "Mariana")
print("")
print(nomes)

# 5. Removendo elementos

# remove() remove um elemento pelo seu valor

nomes.remove("Lucas")
print("")
print(nomes)

# pop() remove um elemento pelo índice

nomes.pop(0)
print("")
print(nomes)

# 6. Tamanho da lista

# len() informa a quantidade de elementos

print("")
print(len(nomes))

# 7. Percorrendo uma lista

print("")
for nome in nomes:
    print(nome)

# 8. Verificando se um elemento existe

print("")
if "João" in nomes:
    print("João está na lista")
else:
    print("João não está na lista")

#9. Lista com diferentes tipos de dados

dados = ["João", 18, 1.75, True]
print("")
print(dados)

# 10. Lista de números

notas = [7.5, 8.0, 6.5, 9.0]
soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)

print("")
print(f"Média: {media:.1f}")

# 11. Tuplas

# Tuplas são semelhantes ás listas
# A principal diferença é que tuplas não podem
# ser alteradas depois de criadas

coordenadas = (10, 20)

print("")
print(coordenadas)

# Acessando elementos

print("")
print(coordenadas[0])
print(coordenadas[1])

# 12. Dicionários

# Dicionários armazenam informações no formato:
# chave: valor

aluno = {
    "nome": "Carlos",
    "idade": 17,
    "nota": 8.5
}

print("")
print(aluno)

# 13. Acessando valores do dicionário

print("")
print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])

# 14. Alterando valores

aluno["nota"] = 9.0
print("")
print(aluno)