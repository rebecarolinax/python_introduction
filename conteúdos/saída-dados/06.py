# Tipos Primitivos

# INPUT: Ler pelo teclado: Recebe os valores
# PRINT: Ler na tela: Exibe os resultados

# Para que em uma soma o + não sirva como concatenação, usar um tipo primitivo
# (USAR INT) Para definir que os valores que o usuário colocar são números

# Tipos
# INT - Número inteiro
# Float - Números reais flutuantes (possui o ".")
# Bool - Aceita apenas dois valores (TRUE ou FALSE)
# String - Qualquer palavra representada por "" ou ''

# MODO ERRADO
# irá retornar um valor concatenado
# exemplo: 5+2 = 52

# print('A soma vale',S)

# MODO CORRETO
# irá retornar um valor somado
# exemplo: 5+2= 7

# print('A soma vale()'.FORMAT(s)) - o () representa o método

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
# ESPECIFICAR INT PARA QUE NÃO HAJA CONCATENAÇÃO

# type: qual o tipo primitivo do valor
# print(type(n1))
s = n1 + n2
# print('A soma entre...')

# Para concatenação do print, usar {}
print('A soma entre {} e {} vale {}'.format(n1,n2,s))
# Acima, novo método de concatenar na atual versão do Python

n = float(input('Digite um valor:'))
# Converte para float ou qualquer tipo primitivo que desejar
print(n)

# Método isnumeric(retorna se é um número) e isalpha(retorna se é uma palavra) e isalnum(retorna se é números ou palavras)
