from math import sqrt

while True:
    a_in = input('Input a number or print "stop" to exit: ')
    if a_in.lower() == 'stop':
        break
    a = int(a_in)
    op = input('Input operation "+, -, /, *, %, //, **, sqrt": ')
    while op not in ('+', '-', '*', '//', '%', '**', 'sqrt'):
        print('Uncorrect opearation!!!')
        print('Input again: ', end='')
        op = input()
    if op == 'sqrt':
        print(f'√{a} = {sqrt(a)}')
        continue
    b = int(input('Input second number: '))
    if op == '+':
        print(f'{a} + {b} = {a + b}')
    elif op == '-':
        print(f'{a} - {b} = {a - b}')
    elif op == '/':
        if b != 0:
            print(f'{a} / {b} = {a / b}')
        else:
            print('Second number is zero!')
    elif op == '*':
        print(f'{a} * {b} = {a * b}')
    elif op == '//':
        if b != 0:
            print(f'{a} // {b} = {a // b}')
        else:
            print('Second number is zero!')
    elif op == '%':
        if b != 0:
            print(f'{a} % {b} = {((a % b) + b) % b}')
        else:
            print('Second number is zero!')
    elif op == '**':
        print(f'{a} ** {b} = {a**b}')
