from vetores import vetor
from listas import lista_ligada

print(30*"-", "MENU", 30*"-")
print("1- Vetores")
print("2- Listas Ligadas")
menu = int(input("Digite a opção desejada: "))

if menu == 1:
    vetor_teste = vetor.Vetor(0)
    vetor_teste.inseir_elemento_posicao(1, 0)
    vetor_teste.inseir_elemento_posicao(2, 1)
    vetor_teste.inseir_elemento_posicao(3, 2)
    vetor_teste.inseir_elemento_posicao(4, 1)
    vetor_teste.inserir_elemento_final(5)
    # vetor_teste.inserir_elemento_final(1)
    # vetor_teste.inserir_elemento_final(2)
    # vetor_teste.inserir_elemento_final(4)
    # vetor_teste.inserir_elemento_final(3)
    # print(vetor_teste.listar_elemento(0))
    # print(vetor_teste.listar_elemento(1))
    # print(vetor_teste.listar_elemento(2))
    # print(vetor_teste.listar_elemento(3))
    print(vetor_teste.contem(16))
    print(vetor_teste.indice(5))
    print(vetor_teste)
    vetor_teste.remover_elemento_indice(2)
    vetor_teste.remover_elemento(3)
    print(vetor_teste)

elif menu ==2:
    lista_teste = lista_ligada.ListaLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(2)
    lista_teste.inserir(3)
    print(lista_teste)
    lista_teste.inserirPosicao(4,0)
    lista_teste.inserirPosicao(5,15)
    lista_teste.inserirPosicao(6,3)
    print(lista_teste)
    lista_teste.removerPosicao(0)
    lista_teste.removerPosicao(5)
    lista_teste.removerPosicao(2)
    lista_teste.removerElemento(3)
    print(lista_teste)
    print(lista_teste.recuperarElementoNo(2))
    print(lista_teste.contem(4))
    print(lista_teste.indice(3))