'''Problem
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.


'''
# PRINT IN ANY ORDER
from collections import Counter,OrderedDict

def count_freq(word):
    return Counter(word)
    
c = count_freq('AAAABBBBCCCCCDDEEEE')
for i in c:
    print(i+str(c[i]),end='')
	

# SOLUTION 


def count_words(s):
    out = ""
    l = len(s)
    if l == 0:
        return ''
    if l == 1:
        return s +'1'
    cnt = 1 
    last = s[0]
    i = 1
    for i in range(1,l):
        if s[i] == s[i-1]:
            cnt +=1 
        else:
            out = out + s[i-1] +str(cnt)
        #i+=1
    out = out + s[i-1] + str(cnt)
    return out
    pass


print(count_words('AAAAABBBBCCCC'))
