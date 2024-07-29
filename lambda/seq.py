def seq(n):
    if n == 0:
        return 2
    
    if n == 1:
        return 5
    
    return 3 * seq(n - 1) - 2 * seq(n - 2);

for i in range(16):
    print(f"{i}: {seq(i)}")
