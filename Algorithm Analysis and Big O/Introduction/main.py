def func1(n):
    final_sum = 0
    for x in range(n+1):
        final_sum += x
    return final_sum

print(func1(10))


# second person uses the shortcut to find the sum

def func2(n):
    return (n*(n+1))/2

print(func2(10))

# works only in Jupyter notebook for calculating the time taken to loop
#%timeit func1(100)

#%timeit func2(100)