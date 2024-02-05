# Definida as funções aritméticas

def adicao(x, y):
    # É usado def para definir FUNÇÕES
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        # Erro de divisão por zerp
        return "Erro: divisão por zero"
    return x / y

while True:
    # Menú para escolha da operação
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Digite a opção (1/2/3/4/5): ")

    # IF referente a escolha do usuário
    if escolha == '5':
        print("Encerrando a calculadora.")
        break

    if escolha not in ('1', '2', '3', '4'):
        print("Opção inválida. Por favor, escolha uma opção válida.")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado: ", adicao(num1, num2))

    # ELIF: Abreviação de Else-If
    elif escolha == '2':
        print("Resultado: ", subtracao(num1, num2))

    elif escolha == '3':
        print("Resultado: ", multiplicacao(num1, num2))

    elif escolha == '4':
        resultado = divisao(num1, num2)
        if resultado == "Erro: divisão por zero":
            print(resultado)
        else:
            print("Resultado: ", resultado)

#  Funções de operação:

# adicao(x, y): Esta função recebe dois números, x e y, e retorna a soma deles.
# subtracao(x, y): Esta função recebe dois números, x e y, e retorna a subtração de x por y.
# multiplicacao(x, y): Esta função recebe dois números, x e y, e retorna o produto deles.
# divisao(x, y): Esta função recebe dois números, x e y, e retorna o resultado da divisão de x por y. Ela também inclui uma verificação para evitar divisões por zero.
# Loop while:

# O programa utiliza um loop while para permitir que o usuário realize múltiplas operações de cálculo até optar por sair.
# Menu de opções:

# O código exibe um menu de opções para o usuário, onde ele pode escolher a operação desejada digitando o número correspondente.
# Leitura da escolha do usuário:

# O programa lê a escolha do usuário com a função input() e armazena a escolha na variável escolha.
# Verificação da escolha do usuário:

# O código verifica se a escolha do usuário é válida (1, 2, 3, 4 ou 5) e exibe mensagens de erro se a escolha não for válida.
# Leitura dos números de entrada:

# O programa lê os dois números de entrada (num1 e num2) utilizando a função input() e os converte em valores float para que as operações matemáticas possam ser realizadas.
# Realização das operações:

# Com base na escolha do usuário, o programa chama a função apropriada (adicao, subtracao, multiplicacao ou divisao) e exibe o resultado da operação.
# Encerramento do programa:

# Se o usuário escolher a opção "5", o programa exibe uma mensagem de encerramento e sai do loop while, encerrando a calculadora.           
   


