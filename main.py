from vetores import vetor
from listas import listaLigada, listaDuplamenteLigada
from pilhas import pilha
from filas import fila
from conjuntos import conjunto,conjuntoEspalhamento
from espalhamento import tabelaEspalhamento
from mapas import mapa

print(30*"-", "MENU", 30*"-")
print("1- Vetores")
print("2- Listas Ligadas")
print("3- Listas Duplamente Ligadas")
print("4- Pilhas")
print("5- Filas")
print("6- Sets")
print("7- espalhamento")
print("8- Mapas")
menu = int(input("Digite a opção desejada: "))

if menu == 1:
    vetorTeste = vetor.Vetor(0)
    vetorTeste.inseirElementoPosicao(1, 0)
    vetorTeste.inseirElementoPosicao(2, 1)
    vetorTeste.inseirElementoPosicao(3, 2)
    vetorTeste.inseirElementoPosicao(4, 1)
    vetorTeste.inserirElementoFinal(5)
    # vetorTeste.inserir_elemento_final(1)
    # vetorTeste.inserir_elemento_final(2)
    # vetorTeste.inserir_elemento_final(4)
    # vetorTeste.inserir_elemento_final(3)
    # print(vetorTeste.listar_elemento(0))
    # print(vetorTeste.listar_elemento(1))
    # print(vetorTeste.listar_elemento(2))
    # print(vetorTeste.listar_elemento(3))
    print(vetorTeste.contem(16))
    print(vetorTeste.indice(5))
    print(vetorTeste)
    vetorTeste.removerElementoIndice(2)
    vetorTeste.removerElemento(3)
    print(vetorTeste)

elif menu == 2:
    listaTeste = listaLigada.ListaLigada()
    listaTeste.inserir(1)
    listaTeste.inserir(2)
    listaTeste.inserir(3)
    print(listaTeste)
    listaTeste.inserirPosicao(4, 0)
    listaTeste.inserirPosicao(5, 15)
    listaTeste.inserirPosicao(6, 3)
    print(listaTeste)
    listaTeste.removerPosicao(0)
    listaTeste.removerPosicao(5)
    listaTeste.removerPosicao(2)
    listaTeste.removerElemento(3)
    print(listaTeste)
    print(listaTeste.recuperarElementoNo(2))
    print(listaTeste.contem(4))
    print(listaTeste.indice(3))

elif menu == 3:
    listaTeste = listaDuplamenteLigada.ListaDuplamenteLigada()
    listaTeste = listaLigada.ListaLigada()
    listaTeste.inserir(1)
    listaTeste.inserir(2)
    listaTeste.inserir(3)
    print(listaTeste)
    listaTeste.inserirPosicao(4, 0)
    listaTeste.inserirPosicao(5, 15)
    listaTeste.inserirPosicao(6, 3)
    print(listaTeste)
    listaTeste.removerPosicao(0)
    listaTeste.removerPosicao(5)
    listaTeste.removerPosicao(2)
    listaTeste.removerElemento(3)
    print(listaTeste)
    print(listaTeste.recuperarElementoNo(2))
    print(listaTeste.contem(4))
    print(listaTeste.indice(3))

elif menu == 4:
    pilhaTeste = pilha.Pilha()
    pilhaTeste.empilhar(1)
    pilhaTeste.empilhar(2)
    pilhaTeste.empilhar(3)
    print(pilhaTeste.desempilhar())

elif menu == 5:
    filaTeste = fila.Fila()
    filaTeste.enfileirar(1)
    filaTeste.enfileirar(2)
    filaTeste.enfileirar(3)
    print(filaTeste)
    print(filaTeste.desenfileirar())
    print(filaTeste)

elif menu == 6:
    conjuntoTeste = conjunto.Conjunto()
    conjuntoTeste.inserir(1)
    conjuntoTeste.inserir(2)
    conjuntoTeste.inserir(3)
    print(conjuntoTeste)
    print(conjuntoTeste.inserirPosicao(1,1))
    print(conjuntoTeste.inserirPosicao(1,2))
    print(conjuntoTeste.inserirPosicao(3,4))
    print(conjuntoTeste)

elif menu == 7:
    conjuntoTeste = conjuntoEspalhamento.Conjunto()
    conjuntoTeste.inserir(1)
    conjuntoTeste.inserir(2)
    conjuntoTeste.inserir(3)
    print(conjuntoTeste)
    print(conjuntoTeste.removerElemento(3))
    print(conjuntoTeste)
    conjuntoTeste.inserir('Python')
    conjuntoTeste.inserir('William')
    conjuntoTeste.inserir(11)
    print(conjuntoTeste)

elif menu == 8:
    mapaTeste = mapa.Mapa()
    mapaTeste.adicionar("par",10)
    mapaTeste.adicionar("impar", 15)
    mapaTeste.adicionar("par",4)
    mapaTeste.adicionar("impar",3)
    print(mapaTeste)
    print(mapaTeste.contemChave("par"))
    print(mapaTeste.recuperar("par"))
    print(mapaTeste.remover("par"))
    print(mapaTeste)

else:
    print("Opção invalida")