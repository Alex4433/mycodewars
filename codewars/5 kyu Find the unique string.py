# very shit-code

def find_uniq(arr):
    res_arr = arr.copy()
    for index in range(len(arr)):
        arr[index] = ''.join(sorted(list(set(arr[index].lower()))))
    try:
        el1, el2 = set(arr)
    except:
        return 'a'
    tmp = el1 if arr.count(el1) == 1 else el2
    for word in res_arr:
        tmp_tmp = tmp
        res_word = word.lower()
        for let in res_word:
            tmp_tmp = tmp_tmp.replace(let, '', 1)
        if len(tmp_tmp) == 0:
            return word


print(find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']))

'''
5 kyu
Find the unique string

There is an array of strings. All strings contains similar letters except one. Try to find it!

findUniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) === 'BbBb'
findUniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) === 'foo'

Strings may contain spaces. Spaces is not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings.
'''
