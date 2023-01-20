Banknotes=int(input())
print(Banknotes)
for tuple in [100,50,20,10,5,2,1,]:
    print(f"{Banknotes//tuple} nota(s) de R$ {tuple},00")
    Banknotes%=tuple