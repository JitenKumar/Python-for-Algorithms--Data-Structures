def anagram(string1, string2):
    '''
    approach :
    1: remove the spaces and make it a simple string
    2: check the length of both strings:
        if equal then proceed:
            store the count of fisrt strings in a counter:
                run the second string and if letter is there then decrease its count
                    they are anagram:
                else:
                    simply return false
        else:
            print not anagram:

    :param s: first string
    :param t: second string
    :return: boolean that whether they are anagram or not
    '''
    string1 = string1.replace(' ', '')
    string2 = string2.replace(' ', '')
    # if len of both are not equal
    if len(string1) != len(string2):
        return False
    # start a counter
    cnt = {}

    for letter in string1:
        # if already there then incrase the count by 1
        if letter in cnt:
            cnt[letter] += 1
        else:
            cnt[letter] = 1
    # start for the second string
    for letter in string2:
        # if already there then incrase the count by 1
        if letter in cnt:
            cnt[letter] -= 1
        else:
            # simply return False
            return False
    # check that all letters been cleared or not

    if len(cnt)!=0:
        return True
    else:
        return False


print(anagram('god', 'dog'))
print(anagram('clint eastwood', 'old west action'))
print(anagram('aa', 'bb'))
print(anagram('go go go','gggooo'))
print(anagram('123', '1 2'))



