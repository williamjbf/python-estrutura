from arvores import noArvores

class NoArvoreInteiro(noArvores.NoArvore):
    def __init__(self,valor):
        super().__init__(valor)

    def peso(self):
        return self.valor