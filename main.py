from vetores import vetor

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
