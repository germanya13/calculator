def calculate():
    operation = input('''
Digite a operação matemática que deseja concluir:
+ para addition
- para subtraction
* para multiplication
/ para division
''')

    number_1 = int(input('Digite o primeiro número: '))
    number_2 = int(input('Digite o segundo número: ' ))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não digitou um operador válido, por favor execute o programa novamente.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Deseja calcular novamente?
Digite Y para SIM ou N para NÃO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('ate mais.')
    else:
        again()

calculate()