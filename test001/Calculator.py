#!/usr/bin/python3
# Programmer : Saw Aung Zay Oo
# Date : 2-19910
while 1:
    fnum = float(input('Enter First number.'))
    operator = input('Enter Operator')
    snum = float(input('Enter Second number.'))
    if operator == '+' :
        result = fnum+snum
    elif operator == '-':
        result = fnum-snum
    elif operator == '*':
        result = fnum*snum
    elif operator == '/':
        result = fnum/snum
    elif operator == '%':
        result = fnum%snum
    else:
        print('incoorect')

    print(result)