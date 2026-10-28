# Atividades

# 1.
print("Atividade 1:")

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

# 2.
print("\nAtividade 2:\n")

class Livro:
    def __init__ (self, titulo, autor, totalPaginas):
        self.titulo = titulo
        self.autor = autor
        self.totalPaginas = totalPaginas
        self.paginasLidas = 0

    def ler(self, paginas):
        self.paginasLidas = min(self.paginasLidas + paginas, self.totalPaginas)

    def porcentagemLida(self):
        return (self.paginasLidas * 100) / self.totalPaginas

    def paginasRestantes(self):
        return self.totalPaginas - self.paginasLidas

    def terminou(self):
        return self.paginasLidas == self.totalPaginas

livro1 = Livro("Dom Casmurro", "Machado de Assis", 256)
livro1.ler(64)
print(livro1.porcentagemLida())
print(livro1.paginasRestantes())
print(livro1.terminou())

# 3.
print("\nAtividade 3:")

class ContaBancaria:
    def __init__ (self, titular):
        self.titular = titular
        self.saldoConta = 0

    def depositar(self, valor):
        self.saldoConta += valor

    def sacar(self, valor):
        if valor <= self.saldoConta:
            self.saldoConta -= valor

    def extrato(self):
        return f"\nTitular: {self.titular}\nSaldo da conta: {self.saldoConta}"

conta1 = ContaBancaria("Cleber")
print(conta1.extrato())
conta1.depositar(100)
print(conta1.extrato())
conta1.sacar(50)
print(conta1.extrato())
conta1.sacar(1000)
print(conta1.extrato())

# 4.
print("\nAtividade 4:")

class Personagem:
    def __init__ (self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.vida = 100
        self.nivel = 1

    def receberDano(self, dano):
        self.vida = max(0, self.vida - dano)

        if self.vida > 0:
            return f"\nVida: {self.vida}"
        else:
            return f"\n{self.nome} foi derrotado!"

    def curar(self, vida):
        self.vida = min(self.vida + vida, 100)

        return f"\nVida: {self.vida}"

    def subirNivel(self):
        self.nivel += 1
        self.vida = 100

        return f"\nNível: {self.nivel}\nVida: {self.vida}"

    def status(self):
        return f"\nNome: {self.nome}\nClasse: {self.classe}\nVida: {self.vida}\nNível: {self.nivel}"

pers1 = Personagem("Jacinto", "Guerreiro")
print(pers1.receberDano(50))
print(pers1.curar(10))
print(pers1.subirNivel())
print(pers1.status())
print(pers1.receberDano(100))

# 5.
print("\nAtividade 5:")

class Produto:
    def __init__ (self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def subTotal(self):
        return self.preco * self.quantidade

    def mostrar(self):
        return f"\nNome: {self.nome}\nPreço: {self.preco}\nQuantidade: {self.quantidade}\nSubtotal: {self.subTotal():.2f}"

class Carrinho:
    def __init__ (self):
        self.itens = []

    def adicionar(self, Produto):
        self.itens.append(Produto)
        return "\nProduto adicionado com sucesso!"

    def total(self):
        total = 0

        for i in self.itens:
            total += i.subTotal()

        return f"\nTotal: {total}"

    def mostrar(self):
        for i in self.itens:
            print(i.mostrar())
            print(i.subTotal())

        print(self.total())

produto1 = Produto("Abacate", 5, 5)
produto2 = Produto("Banana", 3, 10)
produto3 = Produto("Abacaxi", 8, 9)
produto4 = Produto("Laranja", 4, 2)
carrinho = Carrinho()

carrinho.adicionar(produto1)
carrinho.adicionar(produto2)
carrinho.adicionar(produto3)
carrinho.adicionar(produto4)

print(carrinho.total())
carrinho.mostrar()