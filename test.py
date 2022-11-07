def test():
    a = 3
    b = 4
    return a, b

res = test()
print(res)
print(res[1])

t = 1
f = 0

# while not f: print("false")

while f or t: print("either true")