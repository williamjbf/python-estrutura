from abc import ABC, abstractmethod


class NoArvore(ABC):
    def __init__(self, valor, noEsquerdo=None, noDireito=None):
        self._valor = valor
        self.__noEsquerdo = noEsquerdo
        self.__noDireito = noDireito

    @property
    def valor(self):
        return self._valor

    @property
    def noEsquerdo(self):
        return self.__noEsquerdo

    @property
    def noDireito(self):
        return self.__noDireito

    @noEsquerdo.setter
    def noEsquerdo(self, noEsquerdo):
        self.__noEsquerdo = noEsquerdo

    @noDireito.setter
    def noDireito(self, noDireito):
        self.__noDireito = noDireito

    @abstractmethod
    def peso(self):
        pass

    def __str__(self):
        temp =("[(X)]" if self.__noEsquerdo == None else f'[({self.__noEsquerdo.__str__()})]') + \
               (f'[({self.valor.__str__()}') + \
               ("[(X)]" if self.__noDireito == None else f'[({self.__noDireito.__str__()})]')
        return temp
