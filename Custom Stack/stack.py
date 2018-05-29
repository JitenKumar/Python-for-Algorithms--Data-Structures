class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def push(self,item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

# creating a stack
st = Stack()

st.push(12)
st.push(1233)
st.push(544)
st.push(444)
st.push(432234)
print(st.items)

st.pop()
print(st.items)
print(st.size())
print(st.peek())
print(st.isEmpty())
