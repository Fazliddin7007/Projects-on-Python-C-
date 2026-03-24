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
    if op in ('/', '//', '%'):
        while b == 0:
            print('Your number is zero')
            print('Input again: ', end='')
            b = int(input())
    if op == '+':
        print(f'{a} + {b} = {a + b}')
    elif op == '-':
        print(f'{a} - {b} = {a - b}')
    elif op == '/':
        print(f'{a} / {b} = {a / b}')
    elif op == '*':
        print(f'{a} * {b} = {a * b}')
    elif op == '//':
        print(f'{a} // {b} = {a // b}')
    elif op == '%':
        print(f'{a} % {b} = {((a % b) + b) % b}')
    elif op == '**':
        print(f'{a} ** {b} = {a**b}')
