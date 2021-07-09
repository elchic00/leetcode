def fib(n: int) -> int:
    first,sec = 0 , 1
    for _ in range(1,n):
        first,sec=sec,first+sec
    return sec if n>0 else 0

n=int(input("Enter the value of 'n': "))
print("Fibonacci number:", end=" ")
print(fib(n))
