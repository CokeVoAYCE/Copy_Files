import time

def recursion(depth):
    if depth == 3:
        return -1
    if depth == 2:
        return -2
    if depth == 1:
        return 3
    else:
        return recursion(depth-1) + 2 * recursion(depth-2) - 3 * recursion(depth-3)

for n in range(1,41):
    start = time.time()
    val = recursion(n)
    duration = time.time() - start
    print(f'Normal Calculation for n={n} took {duration:.2f}s  Result: {val}')
else:
    print(f'The end.')
