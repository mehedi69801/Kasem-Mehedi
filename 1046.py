""""
a,b=list(map(int,input().split()))
if(a<b):
    time=b-a
else:
    time=b+24-a
print(f"O JOGO DUROU {time} HORA(S)")
"""


x,y=list(map(int,input().split()))
if (x<y):
    time=y-x
else:
    time=y+24-x
print(f'O JOGO DUROU {time} HORA(S)')
