list = [1, 2]
result = [2]
while True:
    res = list[-1] + list[-2]
    list.append(res)
    if res % 2 == 0:
        result.append(res)
    if res > 4000000:
        break
print(result)

'''


Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
'''
