def binary(n):
    if n > 1:
        binary(n//2)
    s.append(n%2)
    return s

if __name__ == "__main__":
    s = []
    n = int(input("Enter a number to convert to binary: "))
    binary(n)  
    print("".join(str(x) for x in s))
