from listas.noDuplamenteLigado import No


class ListaDuplamenteLigada():
    def __init__(self):
        self.__primeiroNo = None
        self.__ultimoNo = None
        self.__tamanho = 0

    def inserir(self, elemento):
        novoNo = No(elemento)
        if self.estaVazia():
            self.__primeiroNo = novoNo
            self.__ultimoNo = novoNo
        else:
            self.__ultimoNo.proximo = novoNo
            novoNo.anterior = self.__ultimoNo
            self.__ultimoNo = novoNo
        self.__tamanho += 1

    def inserirPosicao(self, elemento, posicao):
        if posicao == 0:
            novoNo = No(elemento)
            self.__primeiroNo = self.__primeiroNo.anterior = novoNo
            novoNo.proximo = self.__primeiroNo
            self.__primeiroNo = novoNo
        elif posicao >= self.__tamanho:
            novoNo = No(elemento)
            self.__ultimoNo.proximo = novoNo
            novoNo.anterior = self.__ultimoNo
            self.__ultimoNo = novoNo
        else:
            noAtual = self.recuperarNo(posicao)
            noAnterior = noAtual.anterior
            novoNo = No(elemento)
            noAnterior.proximo = novoNo
            novoNo.proximo = noAtual
            noAtual.anterior = novoNo
            novoNo.anterior = noAnterior
        self.__tamanho += 1

    def contem(self, elemento):
        for i in range(self.__tamanho):
            noAtual = self.recuperarNo(i)
            if noAtual.elemento == elemento:
                return True
            else:
                return False

    def indice(self, elemento):
        for i in range(self.__tamanho):
            noAtual = self.recuperarNo(i)
            if noAtual.elemento == elemento:
                return i
        return -1

    def estaVazia(self):
        return self.__tamanho == 0

    def __str__(self):
        temp = self.__primeiroNo
        elementos = ''
        while(temp):
            elementos = f'{elementos} {temp.elemento}'
            temp = temp.proximo
        return elementos

    def recuperarElementoNo(self, posicao):
        no = self.recuperarNo(posicao)
        if no != None:
            return no.elemento
        return None

    def recuperarNo(self, posicao):
        resultado = 0
        for i in range(posicao+1):
            if i == 0:
                resultado = self.__primeiroNo
            else:
                resultado = resultado.proximo
        return resultado

    def removerPosicao(self, posicao):
        if posicao == 0:
            proximoNo = self.__primeiroNo.proximo
            self.__primeiroNo.proximo = None
            proximoNo.anterior = None
            self.__primeiroNo = proximoNo
        elif posicao == self.__tamanho -1:
            penultimoNo = self.__ultimoNo.anterior
            penultimoNo.proximo = None
            self.__ultimoNo.anterior=None
            self.__ultimoNo = penultimoNo
        else:
            noRemover = self.recuperarNo(posicao)
            noAnterior = noRemover.anterior
            noProximo = noRemover.proximo
            noAnterior.proximo = noProximo
            noProximo.anterior = noAnterior
            noRemover.proximo = None
            noRemover.anterior = None
        self.__tamanho -= 1

    def removerElemento(self, elemento):
        noRemover = self.indice(elemento)
        if noRemover == -1:
            return-1
        self.removerPosicao(noRemover)
