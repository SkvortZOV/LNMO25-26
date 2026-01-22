stroka = input("")
def longest(stroka):
    slova = stroka.split()
    return max(slova , key = len)
print(f"самое длинное слово: {longest(stroka)}")
