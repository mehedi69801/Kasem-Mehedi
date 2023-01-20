day = int(input())
year = day//365
day = day%365
month = day//30
day = day%30
print(f"{year} ano(s)")
print(f"{month} mes(es)")
print(f"{day} dia(s)")