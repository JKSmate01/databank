def border():
    print()
    for i in range(80):
        print("-",sep="",end="")
    print("\n")
for i in range(1,7):
    print(f"{i}. feladat")
    border()

#megadva
def border(n,s):
    print()
    for i in range(n):
        print(s,sep="",end="")
    print("\n")
border(80,"*")
print("1. feladat")
print("a) feladat")
border(10,"-")
print("b) feladat")
border(80,"*")
print("2. feladat")
#hatókör
def proc():
    global a
    a = 4
    print(b)
    #c = 3
    print(c)
b = 0
c = 4
proc()
print(a)
#Paraméter átadás
def proc(x):
    x+=1
    print(x)
proc(3)
a = 10
proc(a)
print(a)
#Tökéletes szám
def pm(num):
    end = int(num/2)
    s = 1
    for i in range(2,end+1):
        if num % i == 0:
            s += 1
    if s == num:
        print("Tökéletes szam")
    else:
        print("Nem tökéletes szám")
for i in range(2,1001):
    print(i,end=" ")
    pm(i)
ob = int(input("Kérem a vizsgálandó számot: "))
pm(ob)
#függ minta
def red(t,w,l):
    if l<=25 or w<=15:
        t = 0.8 * t
    return t
tax = int(input("Kérem a kedvezmény nélküli adót: "))
length = int(input("Kérem a telek hosszát: "))
width = int(input("Kérem a telek szélességét: "))
print(f"A kedvezményes adó: {red(tax,width,length)}")
