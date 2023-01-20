x,y= list(map(int,input().split ()))

price= [0,4,4.50,5,2,1.50]

pay=price[x]*y

print(f'Total: R$ {pay:.2f}')
