x = "global"

def externa():
    x = "envolvente"

    def interna():
        x = "local"
        print(x)

    interna()
    print(x)

externa()
print(x)
