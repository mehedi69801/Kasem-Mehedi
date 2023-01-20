#value = input()
#value_list = value.split()

#A = value_list[0]
#B = value_list[1]
#C = value_list[2]
A,B,C=list(map(float,input().split()))
pi = 3.14159

triangle_area = 0.5 *(A) * (C)
circle_area = pi * (C) * (C)
trapezium_area = (((A) + (B))/2) * (C)
square_area = (B)*(B)
rectangle_area = (A) * (B)

print("TRIANGULO: %.3f"%triangle_area)
print("CIRCULO: %.3f"%circle_area)
print("TRAPEZIO: %.3f"%trapezium_area)
print("QUADRADO: %.3f"%square_area)
print("RETANGULO: %.3f"%rectangle_area)