product1 = input()
product1 = product1.split()
unit1 = product1[1]
price1 = product1[2]
total_price1 = float(unit1) * float(price1)

product2 = input()
product2 = product2.split()
unit2 = product2[1]
price2 = product2[2]
total_price2 = float(unit2) * float(price2)

final_result = total_price1 + total_price2
print("VALOR A PAGAR: R$ %.2f"%final_result)