import sys
anon = []
def x(x = lambda: sys.argv[1]):
    for char in x():
        anon.append(char)
    class x:
        x = lambda x: print(x, end="")
    (list(map(x.x, anon)))
x()
print()