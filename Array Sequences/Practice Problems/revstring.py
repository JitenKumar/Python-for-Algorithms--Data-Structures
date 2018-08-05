'''
Given a string of words, reverse all the words. For example:

Given:

'This is the best'

Return:

'best the is This'

'''

def rev_words(string):
    return " ".join(reversed(string.split()))
    pass

print(rev_words('    space before'))