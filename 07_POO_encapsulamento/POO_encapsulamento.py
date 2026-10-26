# 1. Encapsulamento
# Proteger o salário para que ele só mude seguindo regras

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario # Privado = dois sublinhados

    def __str__(self):
        return f"\nSou {self.nome} e ganho R${self.__salario}"

    @property
    def salario(self):
        return self.__salario

    def darAumento(self, porcentagem):
        if porcentagem > 100 or porcentagem <= 0:
            return "\nAumento inválido!"

        self.__salario *= (1 + porcentagem / 100)

        return f"\n{self.nome} recebeu {porcentagem}% de aumento"

funcionario1 = Funcionario("Cleber", 3000)
print(funcionario1)

funcionario1.darAumento(100)
print(funcionario1)

# 0 try/except é um bloco usado
# para tratar erro

try:
    funcionario1.salario = 10000
except AttributeError:
    print("\nNão é permitido alterar o salário diretamente")

try:
    print(funcionario1.__salario)
except AttributeError:
    print("\nO atributo __salario não pode ser acessado de fora.")