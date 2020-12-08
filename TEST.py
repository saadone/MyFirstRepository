
x = 20
x = 3
nom = "saad"
trouve = True


print(x)

nom = input("qel est votre nom")
print("Hello " + nom)

Annee = input('entrez année de naissance  ')
age = 2020 - int(Annee)


print("votre age " + str(age))


 ########################## STRING 
msg = "The Leyth El ghouzal"
print(msg.find("th"))
print("Leyth" in msg)
 

########################## ARETHMETIC
print(10/3)    # return float
print(10//3)   # return int Value

print(10*3)    # 30
print(10**3)   # 1000


########################## CONDITION
x = 15
if x > 30:
    print("it's a hot day")
    print("take a water")
elif x > 20:
    print("it's a hot day")
else:
    print("it COLD")
print("Done ")

########################## WHILE

i=0
while i <= 10:   # Sparator mill reading num 1_000
    print(i * '*')   # repeat * depend value of i
    i += 1

########################## LIST   TAB

name = ["saad","el ghouzal",'leyth',"mery"]
name[0]="$@@d"
name.append("TEST")
name.remove("el ghouzal")
print(name[0:2])  # print 0 1 and 2 index of tab
print("mery" in name)
for elemt in name:
    print(elemt)



for n in range(5, 10, 2):
    print(n)

########################## TUPLE
num = (5, 9, 4, 8)

