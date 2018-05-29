# examples of Big O
def print_twice(lst):
    for val in lst:
        print(val)
    for val in lst:
        print(val)
print_twice([1,2,3,4])
# Big o will be n + n =2n


def func2(lst):
    #this is O(1)
    print(lst[1])
    mid = int(len(lst)/2)
    # this is o(n/2) ... or (1/2 * n)
    for val in lst[:mid]:
        print(val)

    for i in range(10):
        print("Jiten " + str(i) + " Times")


lst = [1,2,3,4,5,6,7,8,9,10]

print(func2(lst))

# best cases and worst cases


def matching(lst,item):
    for it in lst:
        if it == item:
            return True
    return False
print(matching(lst,11)) # o(n)
print(matching(lst,1)) # 0(1)

# space and time complexity

def spacecomp(num):
    for i in range(num): # time complexity = o(n)
        print("Hello world") # space complexity  o(1)

print(spacecomp(10))