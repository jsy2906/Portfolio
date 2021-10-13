def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i] == a[j]:
                result.add(a[i])
    return result
