class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - Quantidade: {self.quantidade}, Preço: R${self.preco:.2f}"

class GerenciadorEstoque:
    def __init__(self):
        self.estoque = {}

    def adicionar_produto(self, nome, quantidade, preco):
        if nome in self.estoque:
            self.estoque[nome].quantidade += quantidade
            print(f"Produto '{nome}' atualizado no estoque.")
        else:
            produto = Produto(nome, quantidade, preco)
            self.estoque[nome] = produto
            print(f"Produto '{nome}' adicionado ao estoque.")

    def remover_produto(self, nome):
        if nome in self.estoque:
            del self.estoque[nome]
            print(f"Produto '{nome}' removido do estoque.")
        else:
            print(f"Produto '{nome}' não encontrado no estoque.")

    def listar_produtos(self):
        if self.estoque:
            print("\nProdutos no estoque:")
            for produto in self.estoque.values():
                print(produto)
        else:
            print("Estoque vazio.")

    def buscar_produto(self, nome):
        if nome in self.estoque:
            print(f"\nProduto encontrado: {self.estoque[nome]}")
        else:
            print(f"Produto '{nome}' não encontrado no estoque.")

def menu():
    estoque = GerenciadorEstoque()

    while True:
        print("\n--- Menu ---")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Listar Produtos")
        print("4. Buscar Produto")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade: "))
            preco = float(input("Digite o preço: R$"))
            estoque.adicionar_produto(nome, quantidade, preco)

        elif opcao == "2":
            nome = input("Digite o nome do produto a ser removido: ")
            estoque.remover_produto(nome)

        elif opcao == "3":
            estoque.listar_produtos()

        elif opcao == "4":
            nome = input("Digite o nome do produto a ser buscado: ")
            estoque.buscar_produto(nome)

        elif opcao == "5":
            print("Saindo do sistema de estoque...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Inicia o menu interativo1
menu()