numbers = []
pred = None
povishenie = True

for i in range(10):
    numer = int(input(f"введите число {i+1}:"))
    numbers.append(numer)  
    if pred is not None and numer <= pred:
        povishenie = False    
    pred = numer  

summa = sum(numbers)

print(f"Сумма: {summa}")
print(f"В порядке возрастания: {"Да" if povishenie = True else "нет"}")
