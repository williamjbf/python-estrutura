class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None]*tamanho
        self.__posicao = 0

    def tamanho_vetor(self):
        return len(self.__elementos)

    def __str__(self):
        return ' '.join([str(i) for i in self.__elementos])

    def contem(self, elemento):
        for i in self.__elementos:
            if (i == elemento):
                return True
        return False

    def indice(self, elemento):
        for i in range(self.tamanho_vetor()):
            elem = self.listar_elemento(i)
            if elem == elemento:
                return i
        return -1

    def inseir_elemento_posicao(self, elemento, posicao):
        vetor_inicio = self.__elementos[:posicao]+[None]
        veotor_final = self.__elementos[posicao:]
        vetor_inicio[len(vetor_inicio)-1] = elemento
        self.__elementos = vetor_inicio + veotor_final
        self.__posicao += 1

    def inserir_elemento_final(self, elemento):
        if(self.__posicao >= self.tamanho_vetor()):
            self.__elementos += [None]
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def remover_elemento_indice(self, posicao):
        vetor_inicio = self.__elementos[:posicao]
        veotor_final = self.__elementos[posicao+1:]
        self.__elementos = vetor_inicio + veotor_final
        self.__posicao = -1

    def remover_elemento(self,elemento):
        posicao = self.indice(elemento)
        self.remover_elemento_indice(posicao)
        
    def listar_elemento(self, posicao):
        return self.__elementos[posicao]
