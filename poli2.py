def Reinas(n):
    reinas = {}
    contador = 0
    for i in range(n):
        for j in range(n):
            reinas[contador] = [i,j]
            contador += 1
    print(reinas)
    for i in reinas: 
        for t in range(n):
            print(i[t])
        

print(Reinas(2))