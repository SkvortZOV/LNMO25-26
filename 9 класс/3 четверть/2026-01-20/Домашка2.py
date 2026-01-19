def sortirovka(arr):
    for i in range(1, len(arr)):
        b = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > b:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = b
    return arr
input_str = input("Введите числа:")
my_list = list(map(int, input_str.split()))
otsortirovanniy = sortirovka(my_list)
print("Отсортированный массив:", otsortirovanniy)
