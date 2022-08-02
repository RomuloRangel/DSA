# Cabecario calculadora
print('*'*20,'Calculadora Python','*'*20)
print("\n "*4)
print('Selecione a Operação desejada:','\n 1 - Adição \n 2 - Subtração \n 3 - Multiplação \n 4 - Divisão \n')
#Armazenando a opção do usuario em uma variavel
op = int(input('Digite a Operação desejada : '))

#Armazenando os valores
var1 = int(input('Digite Primeito Valor : '))
var2 = int(input('Digite o Segundo Valor : '))

#Comparando as decisões com "if"
if op == 1:
        print('O resulta da Soma é : ', var1 + var2)
elif op == 2:
        print ('O resultado da Subtração é : ', var1 - va2)
elif op ==3:
    print('O resultado da Multiplicação é : ', var1 * var2)
else:
    print('O Resultado da Divisão é : ', var1 / var2)