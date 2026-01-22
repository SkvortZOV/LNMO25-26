stroka = input("")
def polindrom(a):
  return a == a[::-1]
if polindrom(stroka):
  print("это полтндром")
else:
  print("это не полиндром")
