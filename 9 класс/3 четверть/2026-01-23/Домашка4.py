stroka = input("")
def a(stroka):
    glas = "аеёиоуыэюяaeiou"
    soglas = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"
    
    glas_count = 0
    soglas_count = 0
    
    for char in stroka:
        if char in glas:
            glas_count += 1
        elif char in soglas:
            soglas_count += 1
    
    return glas_count, soglas_count

glas, soglas = a(stroka)
print(f"Гласные: {glas}, Согласные: {soglas}")
