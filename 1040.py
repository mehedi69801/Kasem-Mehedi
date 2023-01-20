N1,N2,N3,N4= list(map(float,input().split()))

avg = (N1*2+N2*3+N3*4+N4*1)/(2+3+4+1)

print(f'Media: {avg:.1f}')
if avg>=7.0 :
    print("Aluno aprovado.")
elif avg<5.0:
    print("Aluno reprovado.")
elif avg >= 5.0 and avg <7.0:
    print("Aluno em exame.")
    N5 = float(input())
    print(f'Nota do exame: {N5:.1f}')
    avg2=(N5+avg)/2
    if avg2 >= 5.0:
     print("Aluno aprovado.")

    else:
     print("Aluno reprovado.")
    print(f"Media final: {avg2:.1f}")
"""
A,B,C,D = map(float,input().split())
A = (A*2+B*3+C*4+D*1)/10
print(f'Media: {A:.1f}')
if A>=7.0:
    print("Aluno aprovado.")
elif A<5.0:
    print("Aluno reprovado.")
elif A>=5.0 and A<7.0:
    print("Aluno em exame.")
    N = float(input())
    print(f'Nota do exame: {N:.1f}')
    N = (A+N)/2
    if N>=5.0:
        print("Aluno aprovado.")
        print(f'Media final: {N:.1f}')
    else:
        print("Aluno reprovado.")
        print(f'Media final: {N:.1f}')"""