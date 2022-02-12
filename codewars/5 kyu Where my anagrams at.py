def anagrams(word, words):
    res = []
    for words_item in words:
        if len(words_item) != len(word):
            continue
        el = words_item
        for letter in word:
            words_item = words_item.replace(letter, '', 1)
        if len(words_item) == 0:
            res.append(el)
    return res


print(anagrams('abba',
               ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa',
                'babaa']))
# ['crazer', 'carer', 'racer'] non true
# ['carer', 'racer'] true
# ['crazer', 'carer'] non true


# ('abba', ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa'])


'''

5 kyu
Where my anagrams at?

What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

'''
