# 1.Estruturas condicionais

nota = 6

if nota >= 7:
    print("\nAprovado")
elif nota >= 5:
    print("\nRecuperação")
else:
    print("\nReprovado")

# 2.Condicionais e operadores lógicos

idade = 20
ingresso = True

if idade >= 18 and ingresso:
    print("\nEntrada permitida!\n")
else:
    print("\nEntrada recusada!\n")

# 3.Estrutura de repetição

contador = 1

while contador <= 5:
    print(contador)
    contador += 1

# 4.Estrutura de repetição for

print("")

for i in range(1, 6):
    print(i)

# 5. Percorrendo uma lista

print("")

nomes = ["Ana", "Carlos", "João", "Maria"]

for i in nomes:
    print(i)

# 6. Break, Continue e Pass

print("")

for i in range (1, 11):
    if i == 6:
        break
        #continue
        #pass

    print(i)