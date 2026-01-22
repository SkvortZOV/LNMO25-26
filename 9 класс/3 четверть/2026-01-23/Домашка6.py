stroka = input("")
b = stroka.lower().replace('.', '').replace(',', '').split()
a_count = {}
for a in b:
    if a in a_count:
        a_count[a] += 1  
    else:
        a_count[a] = 1
for a, count in a_count.items():
    print(f"{a}: {count}")
