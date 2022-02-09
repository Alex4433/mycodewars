def pig_it(text):
    text = text.split(' ')
    result = ''
    for word in text:
        if word != '!' and word != '?':
            result += word[1:] + word[0] + 'ay' + ' '
        else:
            result += word[0] + ' '
    return result[:-1]


print(pig_it('Pig latin is cool'))

'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''
