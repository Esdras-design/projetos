def calcular():
    while True:
        # Solicita uma operação do usuário
        expressao = input("Digite uma expressão (ou 'sair' para encerrar): ")

        if expressao.lower() == 'sair':
            print("Calculadora encerrada.")
            break

        try:
            # Avalia a expressão matemática e exibe o resultado
            resultado = eval(expressao)
            print(f"Resultado: {resultado}")
        except Exception as e:
            print(f"Erro na expressão: {e}. Tente novamente.")

# Chama a função para rodar a calculadora
calcular()