# Função para gerenciar colaboradores
def gerenciar_colaboradores():
    colaboradores = {}

    while True:
        print("\nMenu de Colaboradores:")
        print("1. Adicionar colaborador")
        print("2. Remover colaborador")
        print("3. Listar colaboradores")
        print("4. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do colaborador: ")
            senha = input("Digite a senha: ")
            colaboradores[nome] = senha
            print("Colaborador adicionado com sucesso!")

        elif opcao == "2":
            nome = input("Digite o nome do colaborador que deseja remover: ")
            if nome in colaboradores:
                del colaboradores[nome]
                print("Colaborador removido com sucesso!")
            else:
                print("Colaborador não encontrado.")

        elif opcao == "3":
            print("\nLista de colaboradores:")
            for nome, senha in colaboradores.items():
                print(f"Nome: {nome}, Senha: {senha}")

        elif opcao == "4":
            break

        else:
            print("Opção inválida. Tente novamente.")

# Função para login
def login(colaboradores):
    while True:
        nome = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")

        if nome in colaboradores and colaboradores[nome] == senha:
            print("Login bem-sucedido!")
            return nome
        else:
            print("Credenciais inválidas. Tente novamente.")

# Função para cadastrar livros
def cadastrar_livros():
    livros = []

    while True:
        print("\nMenu de Cadastro de Livros:")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            ano = input("Digite o ano de publicação: ")
            livros.append({"Título": titulo, "Autor": autor, "Ano": ano})
            print("Livro cadastrado com sucesso!")

        elif opcao == "2":
            print("\nLista de livros cadastrados:")
            for livro in livros:
                print(f"Título: {livro['Título']}, Autor: {livro['Autor']}, Ano: {livro['Ano']}")

        elif opcao == "3":
            break

        else:
            print("Opção inválida. Tente novamente.")

# Função principal
def main():
    colaboradores = {"admin": "admin"}  # Colaborador padrão para iniciar o sistema
    usuario_logado = None

    while True:
        if usuario_logado:
            print(f"\nBem-vindo, {usuario_logado}!")
        else:
            print("\nBem-vindo! Faça login para continuar.")

        print("\nMenu Principal:")
        print("1. Login")
        print("2. Gerenciar colaboradores")
        print("3. Cadastrar livros")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario_logado = login(colaboradores)
        elif opcao == "2":
            gerenciar_colaboradores()
        elif opcao == "3":
            cadastrar_livros()
        elif opcao == "4":
            print("Obrigado por usar o sistema de gerenciamento de livros. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
