# case 1
a = 1
b = 2
c = 3

print(a)
print(b)
print(c)
print("")

temp = c

c = b
b = a
a = temp

print(a)
print(b)
print(c)
print("")


# case 2 
a = 1
b = 2
c = 3

print(a)
print(b)
print(c)
print("")

a, b, c = c, a, b

print(a)
print(b)
print(c)