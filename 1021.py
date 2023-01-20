number = float(input())
print("NOTAS:")
for x in [100,50,20,10,5,2]:
    print(f"{int(number/x)} nota(s) de R$ {x}.00")
    number = float(f"{number % x:.2f}")

print("MOEDAS:")
for x in [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]:
    print(f"{int(number / x)} moeda(s) de R$ {x:.2f}")
    number = float(f"{number % x:.2f}")