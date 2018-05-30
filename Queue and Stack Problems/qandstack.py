# balanced parenthesis

'''
Given a string of opening and closing parentheses,
check whether it’s balanced. We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}.
Assume that the string doesn’t contain any other character than these, no spaces words or numbers. As a reminder,
balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example ‘([])’
is balanced but ‘([)]’ is not.
 assume the input string has no spaces.

'''

def balance_parent(string):
    # if contain odd length then no balanced
    if len(string)%2 !=0:
        return False

    stack = []

    opening_par = set('([{')

    matching_par = set([('(',')'),('{','}'),('[',']')])

    for b in string:
        if b in opening_par:
            #add it to stack
            stack.append(b)
        else:
            if len(stack)==0:
                return False
            last_open = stack.pop()

            if(last_open,b) not in matching_par:
                return False
    return len(stack) == 0

print(balance_parent('(){}'))

print(balance_parent('{(){[]}}'))

# IMPLEMENTING A QUEUE USING TWO STACKS

'''
Logic
Enqueue:
Stack1 for adding the elements into the stack
push elements into the stack

Deque
Stack 2 for this operation
if len of stack 1 and stack 2 is empty then show an error that no element exist
other wise if :
stack 2 is empty and stack 1 is not 
them:
Ccpy all the elements from the stack1 to stack2

then pop the element from the stack 2
'''

class custom_queue_two_stack(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,element):
        self.stack1.append(element)

    def dequeue(self):

        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


q = custom_queue_two_stack()

for i in range(5):
    q.enqueue(i)

print(q.dequeue())
