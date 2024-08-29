equipamentos = []

def cadastrar_equipamento():
    nome = input("Digite o nome do equipamento: ")
    tipo = input("Digite o tipo de equipamento (Computador, Dispositivo de Rede, etc.): ")
    descricao = input("Digite uma breve descrição do equipamento: ")
    equipamento = {
        "nome": nome,
        "tipo": tipo,
        "descricao": descricao
    }
    equipamentos.append(equipamento)
    print("Equipamento cadastrado com sucesso!")

def buscar_equipamento():
    nome = input("Digite o nome do equipamento que deseja buscar: ")
    for equipamento in equipamentos:
        if equipamento["nome"] () == nome():
            print(f"Nome: {equipamento['nome']}")
            print(f"Tipo: {equipamento['tipo']}")
            print(f"Descrição: {equipamento['descricao']}")
            return
    print("Equipamento não encontrado.")

def gerar_relatorio():
    if not equipamentos:
        print("Nenhum equipamento cadastrado.")
    else:
        print("\nRelatório de Equipamentos")
        print("-" * 30)
        for equipamento in equipamentos:
            print(f"Nome: {equipamento['nome']}")
            print(f"Tipo: {equipamento['tipo']}")
            print(f"Descrição: {equipamento['descricao']}")
            print("-" * 30)

def menu():
    while True:
        print("\n1. Cadastrar Equipamento")
        print("2. Buscar Equipamento")
        print("3. Gerar Relatório")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_equipamento()
        elif opcao == "2":
            buscar_equipamento()
        elif opcao == "3":
            gerar_relatorio()
        elif opcao == "4":
            print("programa encerrado!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()