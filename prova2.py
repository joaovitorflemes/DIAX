import json

equipamentos = []

def carregar_dados():
    global equipamentos
    try:
        with open('equipamentos.json', 'r') as f:
            equipamentos = json.load(f)
    except FileNotFoundError:
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

def salvar_dados():
    with open('equipamentos.json', 'w') as f:
        json.dump(equipamentos, f, indent=4)


def buscar_equipamento():
    nome = input("Digite o nome do equipamento que deseja buscar: ")
    for equipamento in equipamentos:
        if equipamento["nome"] () == nome():
            print(f"Nome: {equipamento['nome']}")
            print(f"Tipo: {equipamento['tipo']}")
            print(f"Descrição: {equipamento['descricao']}")
            return
    print("Equipamento não encontrado.")

def excluir_equipamento():
    nome = input("Digite o nome do equipamento que deseja excluir: ").strip()
    global equipamentos
    equipamentos = [equipamento for equipamento in equipamentos if equipamento["nome"].lower() != nome.lower()]
    salvar_dados()
    print("Equipamento excluído com sucesso!")

def editar_equipamento():
    nome = input("Digite o nome do equipamento que deseja editar: ").strip()
    equipamento = buscar_equipamento(nome)
    
    if equipamento:
        print(f"Dados atuais do equipamento:")
        print(f"Nome: {equipamento['nome']}")
        print(f"Tipo: {equipamento['tipo']}")
        print(f"Descrição: {equipamento['descricao']}")
        
        novo_nome = input("Digite o novo nome do equipamento (deixe em branco para manter o nome atual): ").strip()
        novo_tipo = input("Digite o novo tipo de equipamento (deixe em branco para manter o tipo atual): ").strip()
        nova_descricao = input("Digite a nova descrição do equipamento (deixe em branco para manter a descrição atual): ").strip()

        if novo_nome:
            equipamento['nome'] = novo_nome
        if novo_tipo:
            equipamento['tipo'] = novo_tipo
        if nova_descricao:
            equipamento['descricao'] = nova_descricao
        
        salvar_dados()
        print("Equipamento editado com sucesso!")
    else:
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
        print("3. Editar Equipamento")
        print("4. Excluir Equipamento")
        print("5. Gerar Relatório")
        print("6. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_equipamento()
        elif opcao == "2":
            buscar_equipamento_input()
        elif opcao == "3":
            editar_equipamento()
        elif opcao == "4":
            excluir_equipamento()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()