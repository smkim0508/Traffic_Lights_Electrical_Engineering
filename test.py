ans = 1

def test():
    global ans
    ans += 1
    res = ans
    
    return res
    

while(True):
    p = test()
    print(p)


# res = test()
# print(res)
# print(res[1])

# t = 1
# f = 0

# # while not f: print("false")

# while f or t: print("either true")