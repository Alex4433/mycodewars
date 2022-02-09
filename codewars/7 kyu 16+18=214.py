def add(a, b):
    a = str(a)
    b = str(b)
    if len(b) > len(a):
        a, b = b, a
    stroka = ''

    for i in range(len(a)):
        i = -1 - i
        try:
            tmp = int(a[i]) + int(b[i])
        except:
            tmp = int(a[i])
        tmp = str(tmp)
        stroka = tmp + stroka
    return int(stroka)


a = 122
b = 81
print(add(a, b))

'''
For this kata you will have to forget how to add two numbers.

It can be best explained using the following meme:

Dayane Rivas adding up a sum while competing in the Guatemalan television show "Combate" in May 2016

In simple terms, our method does not like the principle of carrying over numbers and just writes down every number it calculates :-)

You may assume both integers are positive integers.
Examples
16+1821426+39515122+811103\large \begin{array}{lll} & 1 & 6 \\ + & 1 & 8 \\ \hline & 2 & 1 4 \\ \end{array} \qquad \large \begin{array}{lll} & 2 & 6 \\ + & 3 & 9 \\ \hline & 5 & 15 \\ \end{array} \qquad \large \begin{array}{lll} & 1 & 2 & 2 \\ + & & 8 & 1 \\ \hline & 1 & 10 & 3 \\ \end{array}+​112​6814​​+​235​6915​​+​11​2810​213​​
'''
