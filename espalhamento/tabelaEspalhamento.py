from listas import listaLigada

class TabelaEspalhamento():
    def __init__(self):
        self.__elementos = listaLigada.ListaLigada()
        self.__numeroCategorias = 10
        self.__tamanho = 0

        for i in range(self.__numeroCategorias):
            self.__elementos.inserir(listaLigada.ListaLigada())
    
    @property
    def estaVazia(self):
        return self.__tamanho

    def __str__(self):
        return self.__elementos.__str__()

    def __gerarNumeroEspalhamento(self, elemento):
        return hash(elemento) % self.__numeroCategorias

    def inserir(self,elemento):
        if self.contem(elemento):
            return False
        numeroEspalhamento = self.__gerarNumeroEspalhamento(elemento)
        categoria = self.__elementos.recuperarElementoNo(numeroEspalhamento)
        categoria.inserir(elemento)
        self.__tamanho +=1
        return True

    def remover(self,elemento):
        numeroEspalhamento = self.__gerarNumeroEspalhamento(elemento)
        categoria = self.__elementos.recuperarElementoNo(numeroEspalhamento)
        categoria.removerElemento(elemento)

    def contem(self,elemento):
        numeroEspalhamento = self.__gerarNumeroEspalhamento(elemento)
        categoria = self.__elementos.recuperarElementoNo(numeroEspalhamento)
        return categoria.contem(elemento)