def sep(word): 
    return list(word)
    
a = input()
b = sep(a)
c = sep(a)
s = ''
for i in range(0, len(b)):
    c[i] = b[len(b) - 1 - i]
print("Given password: " + s.join(b))
print("Encrypted as: " + s.join(c))
    
