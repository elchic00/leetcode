def reverse(s):
    str = ""
    for c in s:
        str = c + str
    return str


s = "string"
print(s)
print(reverse(s))
