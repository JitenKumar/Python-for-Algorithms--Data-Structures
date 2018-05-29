def sumcheck(arr, value):
    '''
    1: SIMPLE APPROACH
    2: USING HASHING
    :param arr: given array
    :param value: matching value
    :return: len or the pairs that lead to the sum
    '''
    tp = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == value:
                print(arr[i], arr[j])
                tp.append((i, j))
    return len(tp)


print(sumcheck([1,3,2,2], 4))


# SECOND APPROACH
def second(arr, val):
    # create a set
    st = set()
    count = 0
    lst = []
    for num in arr:
        if val-num in st:
            count += 1
            lst.append((num, val-num))
        else:
            st.add(num)

    return lst


print(second([1,3,2,2], 4))
