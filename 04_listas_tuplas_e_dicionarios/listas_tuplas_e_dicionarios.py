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