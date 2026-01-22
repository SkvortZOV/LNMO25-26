email = input("")
def domen(email):
    part = email.split("@")
    return part[1]
print(domen(email))
        
