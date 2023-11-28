#Métodos Python Data Model, inicialização: __init__
#Representação: __str__(string), __repr__ (representation, usado para mostrar como o objeto foi criado)
#Containers e sequencia: __contains__, __iter__, __len__, __getitem__
#Númericos: __add__, __sub__, __mul__, __mod__

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    def __str__(self): #O __init__ pelo python sabe que esse método é um inicializador de objeto, agora o __str__ seria um método especial para representar a classe textualmente, pra não precisar usar print, e ficar mais pythonico o código 
       return f'Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}' #Não esquecer de colocar os _ de protected nos que criados pela classe mãe estão protected

class Filme(Programa): #Entre parenteses assim para sinalizar herança
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)#Código para puxar a herança de Programa e ser usada em nome e ano, para pegar os getters e setters e o print
        self.duracao = duracao    

    #Pegando um método da classe mãe, e criando um polimorfismo para ele funcionar diferente em filme e serie, mostrando a duração q é coisa unica do filme, e temporada que é coisa única da série
    def __str__(self):#O __init__ pelo python sabe que esse método é um inicializador de objeto, agora o __str__ seria um método especial para representar a classe textualmente, pra não precisar usar print, e ficar mais pythonico o código 
       return f'Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} - Likes: {self._likes}' #Não esquecer de colocar os _ de protected nos que criados pela classe mãe estão protected
       

class Serie(Programa):#Entre parenteses assim para sinalizar herança
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)#Código para puxar a herança de Programa e ser usada em nome e ano, para pegar os getters e setters e o print
        self.temporadas = temporadas
    
    #Pegando um método da classe mãe, e criando um polimorfismo para ele funcionar diferente em filme e serie, mostrando a duração q é coisa unica do filme, e temporada que é coisa única da série
    def __str__(self):#O __init__ pelo python sabe que esse método é um inicializador de objeto, agora o __str__ seria um método especial para representar a classe textualmente, pra não precisar usar print, e ficar mais pythonico o código 
       return f'Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self._likes}' #Não esquecer de colocar os _ de protected nos que criados pela classe mãe estão protected

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome.title()
        self._programas = programas

    #Método que representa o comportamento de uma sequencia que consegue ser iterável para usar for, for in
    #A vantagem é que não precisar herdar nada de ngm, não precisa dizer que é daquele tipo, mas tem que se comportar como algo daquele tipo,  um objeto daquele tipo (duck type)
    def __getitem__(self, item): #Função do python para a classe voltar a ser um iterável
        return self._programas[item] #Retornando um itém para a lista de programa interno

    def __len__(self):
        return len(self._programas)

    #Código substituido pelo print(f'Tamanho da playlist é de: {len(playlist_fim_de_semana)}'), pois agora que herdamos da list transformando os programas em list, podemos usar o len e saber diretamente a quantidade, não precisando dessa def
    #def tamano(self):
    #    return len(self.programas) #Retornando a quantidade de programas que vão ter na Playlist 

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 4)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series) 

print(f'Tamanho da playlist é de: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa) #Apenas rodando entre o a classe do filme e da série, assim rodando a herença da classe mãe, e o __str__ que seria um método especial também
   #Não precisa mais fazer programa.imprime por exemplo para chamar o método imprime para retornar o nome do filme, ano e etc, por ser um método especial, apenas rodando a classe, ele já roda sozinholista = [1, 2, 4, 5]

print(f'Tá ou não ta? {vingadores in playlist_fim_de_semana}')

