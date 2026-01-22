spisoc = input("").split()
def a(familia):
    return familia.capitalize()  
b = [a(familia.lower()) for familia in spisoc]  
for familia in b:
    print(familia)
