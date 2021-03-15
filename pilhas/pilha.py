from listas import listaDuplamenteLigada

class Pilha():
    def __init__(self):
        self.__elementos = listaDuplamenteLigada.ListaDuplamenteLigada()

    def empilhar(self,elemento):
        self.__elementos.inserir(elemento)

    def estaVazia(self):
        return self.__elementos.estaVazia()

    def desempilhar(self):
        if self.estaVazia():
            return None
        resultado = self.__elementos.recuperarElementoNo(self.__elementos.tamanho -1)
        self.__elementos.removerPosicao(self.__elementos.tamanho -1)
        return resultado