# O(log n) => log2 8  = 3
#recursive fn

def recurse(n):
    if n == 0:
        return
    recurse(n//2)
    print(n)

recurse(16)    