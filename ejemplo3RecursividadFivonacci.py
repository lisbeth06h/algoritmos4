def finovacci_simple(n):
    if n <= 1:
        return n
    else:
        return finovacci_simple(n - 1) + finovacci_simple(n - 2)

print(finovacci_simple(5))
