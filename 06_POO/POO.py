# 1. Classe

class Celular:
    def __init__ (self, marca, modelo, cor, bateria):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

# 2. Métodos

    def ligar(self):
        if self.bateria == 0:
            print("Sem bateria! Coloque para recarregar!")
        else:
            self.ligado = True
            print("ligado")

    def desligar(self):
        self.ligado = False
        print("Desligado")

# 3. Objeto

celular1 = Celular("Xiaomi", "Galaxy S25 Ultra", "branco", 54)
celular2 = Celular("Iphone", "18 Pro Max", "Beringela",37)

# 4. Acessando e alterando atributos
print(celular1.marca)
print(celular1.modelo)
print(celular2.bateria)

# 5. Chamando métodos
celular2.ligar()
celular2.desligar()

# 6. Atividades

class Cachorro:
    def __init__ (self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print("\n" , self.nome , " diz: Au au!")

    def mostrarInfo(self):
        print("\nNome: " , self.nome)
        print("Raça: " , self.raca)
        print("Idade: " , self.idade)

cachorro1 = Cachorro("Rex", "cachorro", 10)
cachorro2 = Cachorro("Cleber", "cachorro bravo", 33)

cachorro1.latir()
cachorro2.latir()
cachorro1.mostrarInfo()
cachorro2.mostrarInfo()

cachorro1.idade = 2
cachorro1.mostrarInfo()
