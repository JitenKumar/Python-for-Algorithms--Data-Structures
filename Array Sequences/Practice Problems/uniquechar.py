'''
Unique Characters in String
Problem
Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.
'''

# solution 

def unique_char(string):
    s = set()
    for i in string:
        if i in s:
            return False
        else:
            s.add(i)
    return True
    
print(unique_char('ABCDEFGHI'))