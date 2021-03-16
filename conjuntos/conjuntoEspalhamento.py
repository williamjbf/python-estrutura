from espalhamento import tabelaEspalhamento

class Conjunto():
    def __init__(self):
        self.__elementos = tabelaEspalhamento.TabelaEspalhamento()

    def inserir(self, elemento):
        self.__elementos.inserir(elemento)

    def __str__(self):
        return self.__elementos.__str__()

    def contem(self, elemento):
        return self.__elementos.contem(elemento)

    def estaVazia(self):
        return self.__elementos.tamanho == 0

    def removerElemento(self, elemento):
        self.__elementos.remover(elemento)



