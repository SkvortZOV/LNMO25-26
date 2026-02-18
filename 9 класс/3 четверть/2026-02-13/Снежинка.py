import turtle as t
t.shape("turtle")
t.speed(30)
commanda = "FLFRRFLF"
commanda2 = "FLFRRFLF"
n = 3
def parc(l):
    for i in l:
        if( i == "F"):
            t.forward(30)
        if( i == "L"):
             t.left(60)
        if( i == "R"):
             t.left(60)
for i in range(0, n-1):
    commanda3 =""
    for j in commanda2:
        if( j == "F"):
             commanda3 = commanda3 + commanda
        else:
            commanda3 = commanda3 + j
    commanda2 = commanda3
parc(commanda3)
t.right(120)
parc(commanda3)
t.right(120)
parc(commanda3)
t.done()
        
