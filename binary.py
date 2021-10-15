def decTobinary(n):
    if n > 1:
        decTobinary1(n//2)
    s.append(n%2)
    return s
def binaryToDecimal(head):
        
    num = head.val
    while head.next:
        num = num * 2 + head.next.val
        head = head.next
    return num

if __name__ == "__main__":
    s = []
    n = int(input("Enter a number to convert to binary: "))
    decTobinary(n)  
    print("".join(str(x) for x in s))
