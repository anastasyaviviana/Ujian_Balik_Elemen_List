def balikposisi(x):
    reverse=[]
    for i in range (len(x)-1,-1,-1):
        a=x[i]
        reverse.append(a)
    return reverse

print(balikposisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikposisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikposisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))