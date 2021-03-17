class Arvore():
    def __init__(self, raiz=None):
        self.__raiz = raiz

    @property
    def raiz(self):
        return self.__raiz

    def inserirElemento(self, no):
        no.noDireito = None
        no.noEsquerdo = None
        if(self.__raiz == None):
            self.__raiz = no
        else:
            self.__inserir(self.__raiz, no)

    def __inserir(self, referencia, novoNo):
        if referencia.peso() < novoNo.peso():
            if referencia.noDireito == None:
                referencia.noDireito = novoNo
            else:
                self.__inserir(referencia.noDireito, novoNo)
        else:
            if referencia.noEsquerdo == None:
                referencia.noEsquerdo = novoNo
            else:
                self.__inserir(referencia.noEsquerdo, novoNo)

    def buscar(self, noBusca):
        return self.__buscar(self.__raiz, noBusca)

    def __buscar(self, referencia, noBusca):
        if referencia.valor == noBusca.valor:
            return referencia
        else:
            if referencia.peso() < noBusca.peso():
                if referencia.noDireito == None:
                    raise ValueError("Elemento não encontrado")
                else:
                    print("Navegando pela direita do nó", referencia.valor.__str__())
                    return self.__buscar(referencia.noDireito, noBusca)
            else:
                # Esquerda do nó
                if referencia.noEsquerdo == None:
                    raise ValueError("Elemento não encontrado")
                else:
                    print("Navegando pela esquerda do nó", referencia.valor.__str__())
                    return self.__buscar(referencia.noEsquerdo, noBusca)

    def em_ordem(self):
        self.__em_ordem(self.__raiz)

    def __em_ordem(self, referencia):
        if referencia.noEsquerdo != None:
            self.__em_ordem(referencia.noEsquerdo)
            print(referencia.valor.__str__())
            if referencia.noDireito != None:
                self.__em_ordem(referencia.noDireito)
        else:
            print(referencia.valor.__str__())
            if referencia.noDireito != None:
                self.__em_ordem(referencia.noDireito)

    def pre_ordem(self):
        self.__pre_ordem(self.__raiz)

    def __pre_ordem(self, referencia):
        print(referencia.valor.__str__())
        if referencia.noEsquerdo != None:
            self.__pre_ordem(referencia.noEsquerdo)
            if referencia.noDireito != None:
                self.__pre_ordem(referencia.noDireito)
        else:
            if referencia.noDireito != None:
                self.__pre_ordem(referencia.noDireito)

    def pos_ordem(self):
        self.__pos_ordem(self.__raiz)

    def __pos_ordem(self, referencia):
        if referencia.noEsquerdo != None:
            self.__pos_ordem(referencia.noEsquerdo)
            if referencia.noDireito != None:
                self.__pos_ordem(referencia.noDireito)
            print(referencia.valor.__str__())
        else:
            if referencia.noDireito != None:
                self.__pos_ordem(referencia.noDireito)
                print(referencia.valor.__str__())
            else:
                print(referencia.valor.__str__())

    def altura(self):
        return self.__altura(self.__raiz)

    def __altura(self, referencia):
        if referencia == None:
            return -1
        alturaEsquerda = self.__altura(referencia.noEsquerdo)
        alturaDireita = self.__altura(referencia.noDireito)
        return (alturaEsquerda + 1) if alturaEsquerda > alturaDireita else (alturaDireita + 1)

    def __str__(self):
        return "[(X)]" if self.__raiz == None else self.__raiz.__str__()