# Prosess 01
import math
x1,y1=tuple(map(float,input().split()))
x2,y2=tuple(map(float,input().split()))

total=math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
print(f'{total:.4f}')