#Implement a method to find the number of occurrences of any given word in a book. A word is represented as a string and a book is represented as an array / list of strings.
#Optimize the method to be called multiple times.
def Occurrences(word, book):
    if book is None or len(book) == 0:
        return -1
    count = 0
    for word in book:
        if word.lower().strip() == word.lower().strip():
            count +=1
    return count

Book = [" The", "dog", "jumped", "in", "the", "dog", "house" ]
print(Occurrences("the",Book))
#Word: "dog"  →  Occurrences: 2
