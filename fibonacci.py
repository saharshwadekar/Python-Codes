def fibo(x):
    return x if x <= 1 else fibo(x-1)+fibo(x-2)
for i in range(7): print(fibo(i))