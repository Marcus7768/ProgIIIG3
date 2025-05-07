# conceptos basicos

# objetos

print("hola mundo")

nombre =  "no podes"

def suma(op1,op2):
    return op1 + op2

def mult(op1,op2):
    return op1 * op2


def res(op1,op2):
    return op1 - op2

def div(op1,op2):
    return op1 / op2

print(mult(3,5))

def cal(oper,op1,op2):
    if(oper=="suma"):
        return suma(op1,op2)
    elif(oper=="resta"):
        return res(op1,op2)
    elif(oper=="div"):
        return div(op1,op2)
    elif(oper=="mult"):
        return mult(op1,op2)
    
def cal2(oper,op1,op2):
    return eval(f"{oper}({op1},{op2})")

print(cal2("mult",3,5))

for i in range(2,10,2):
    print(i)

for c in nombre:
    print(c)

# tarea investigar listas diccionarios conjuntos tuplas (array dict set tuples)

# listas y arrays

import array

A = array.array('i',[])

print(A)

L = []

L2 = list()

for i in range(10):
    L.append(i)
print(L)

L2 = [i for i in range(10)]

print(L2)

L3 = [i for i in range(10) if not (i%2==0)]

print(L3)

L4 = [i for i in range(1,10,2)]

print(L4)

# tupla

T = ()

T = tuple()

T=(1,"uno","one")

# diccionarios

D ={}

D = dict()

L5 = [(1,("uno","one")),(2,("dos","two")),(3,("tres","three"))]

D2 = dict(L5)

print(D2)

# conjuntos set

C = set()

C= set(range(10))

print(C)

# programacion por restricciones

palabras = "SEND MORE MONEY"

letras = set(palabras)
letras.discard(' ')
print(len(letras))

import itertools as it

# combs = list(it.combinations(L,len(letras)))

perm = list(it.permutations(L,len(letras)))

# print(combs)
print(len(perm))

dicci = {k:None for k in letras}

# perm=(4,9,8,7,6,5,4,3,2)
# pos = 0

# for k in dicci.keys():
#     dicci[k] = perm[pos]
#     pos+=1

send = (dicci['S']*1000) + (dicci['E'*100]) + (dicci['N']*10) + (dicci['D'])
more = (dicci['M']*1000) + (dicci['O'*100]) + (dicci['R']*10) + (dicci['E'])
money = (dicci['M']*10000) + (dicci['O']*1000) + (dicci['N'*100]) + (dicci['E']*10) + (dicci['Y'])

def validate(dicci):
    send = (dicci['S']*1000) + (dicci['E'*100]) + (dicci['N']*10) + (dicci['D'])
    more = (dicci['M']*1000) + (dicci['O'*100]) + (dicci['R']*10) + (dicci['E'])
    money = (dicci['M']*10000) + (dicci['O']*1000) + (dicci['N'*100]) + (dicci['E']*10) + (dicci['Y'])
    return (send+more) == money


# for perm in perm:
#     pos = 0
#     for k in dicci.keys():
#         dicci[k] = perm[pos]
#         pos+=1
#     if validate(dicci):
#         print(dicci)

L.discard(1)
perm = list(it.permutations(L,len(letras)-1))

# for perm in perm:
#     pos = 0
#     for k in dicci.keys():
#         if not(k=='M'):
#             dicci[k] = perm[pos]
#             pos+=1
#     if validate(dicci):
#         print(dicci)

dicci['M']=1
dicci['S']=9
dicci['O']=0

nope = ['M','S','O']

for perm in perm:
    pos = 0
    for k in dicci.keys():
        if not(k in nope):
            dicci[k] = perm[pos]
            pos+=1
    if validate(dicci):
        print(dicci)    