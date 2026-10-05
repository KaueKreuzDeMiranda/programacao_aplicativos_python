# Oque é uma função:

# Uma função é um bloco de código criado para realizar
# uma determinação tarefa.
# Ela permite organizar e reutilizar código

# 1. Criando uma função

# Utilize a palavra def para criar uma função

def saudacao():
    print("Olá, seja bem vindo")

saudacao()

# 2. Função com parâmetro

def saudacao(nome):
    print(f"\nOlá, {nome}")

saudacao("Ana")
saudacao("Carlos")

# 3. Mais de um parâmetro
def apresentar(nome , idade):
    print(f"\nnome: {nome}")
    print(f"idade: {idade}")

apresentar("Maria" , 17)

# 4. Função com cálculo
def somar(numero1 , numero2):
    resultado = numero1 + numero2
    print(f"\nResultado: {resultado}")

somar(21, 12)

# 5. Retornando um valor
# O return devolve um valor para o local onde
# a função foi chamada.

def somar(numero1 , numero2):
    return numero1 + numero2

resultado = somar(21 , 12)
print("\n" , resultado)

# 6. Função com condição

def verificarIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

resultado = verificarIdade(20)
print("\n" , resultado)

# 7. Parâmetro com valor padrão
# Podemos definir um valor padrão para um parâmetro

def saudacao(nome = "Aluno"):
    print(f"\nOlá , {nome}")

saudacao()
saudacao("João")

# 8. Varios parâmetros
def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

print("\n" , calcularMedia(21, 12, 9))

# 9. Funções para organizar um programa

def cadastrarProduto():
    nome = input("\nDigite o nome do produto:")
    preco = float(input("\nDigite o preço:"))
    return nome, preco

def exibirProduto(nome, preco):
    print("\n==== Produto ====")
    print(f"nome {nome}")
    print(f"Preço: R${preco}")

nome , preco = cadastrarProduto()
exibirProduto(nome , preco)