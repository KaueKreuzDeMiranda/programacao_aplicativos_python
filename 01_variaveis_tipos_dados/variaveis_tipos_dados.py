nome = "Cleber"
idade = 18
altura = 1.75
aprovado = True

print(nome)
print(idade)
print(altura)
print(aprovado)

print(f"\n{type(nome)}")
print(type(idade))
print(type(altura))
print(type(aprovado))

nome = input("\nDigite seu nome: ")
print(f"\nOlá {nome}")

idade = int(input("\nDigite sua idade: "))
print(f"\nSua idade é {idade}")

altura = float(input("\nDigite sua altura: "))
print(f"\nSua altura é {altura}")

print(f"\nMeu nome é {nome}, eu tenho {idade} anos de idade e {altura} de altura!")

numero1 = 10
numero2 = 3

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print(f"\nSoma: {soma}\nSubtração: {subtracao}\nMultiplicacao: {multiplicacao}\nDivisao: {divisao}")

restoDiv = numero1 % numero2
potenciacao = numero1 ** numero2

print(f"Resto da divisao: {restoDiv}\nPotenciação: {potenciacao}")