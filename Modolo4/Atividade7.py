def testar():
    a = 10
    copia = locals()
    copia["a"] = 99

    print(a)
    print(copia["a"])

testar()
