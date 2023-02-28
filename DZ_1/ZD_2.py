a = input('Введите 3-х значное число: ')
sum = 0
if len(a) == 3:
    for i in a:
        sum += int(i)
    print(sum)
else:
    print('Вы ввели не 3-х значное число')