# Faça um programa que leia algo do teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela

a = input('Digite algo:')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', a.isspace())
# Utilizar vírgula antes de instanciar um método
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print(' É afanúmerico', a.isalnum())
