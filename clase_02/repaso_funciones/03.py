a = 6

def test():
    a = 7
    def denuevo():
        a = 8
        print(a)
    denuevo()
    print(a)

test()
print(a)

