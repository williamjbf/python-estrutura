from listas import listaLigada

class Fila():
    def __init__(self):
        self.__elementos = listaLigada.ListaLigada()
    
    def enfileirar(self,elemento):
        self.__elementos.inserir(elemento)
    
    def estaVazia(self):
        return self.__elementos.estaVazia()
    
    def desenfileirar(self):
        if self.estaVazia():
            return None
        resultado = self.__elementos.recuperarElementoNo(0)
        self.__elementos.removerPosicao(0)
        return resultado
    
    def __str__(self):
        temp = self.__elementos.__str__()
        return temp