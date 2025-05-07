Dom=set(range(1,10))
print(Dom)

Idcols = "ABCDEFGHI"

import itertools as it

# convinatoria con for Emmanuel

Varkeys2 = []

for i in Idcols:
    Varkeys2 = i

# --------------------------------------

Varkeys = list(it.product(Dom,Idcols))
# print(Varkeys)

# convertir lista de tuplas a strings

strVarkeys= [f"{key[1]}{key[0]}" for key in Varkeys]

# print(strVarkeys)

VarDoms={key:Dom.copy() for key in strVarkeys}

# print(VarDoms)

# asignar valores desde un archivo plano ordenado por filas para no copiar el tablero uno a uno

with open("plano.txt","r") as archivo:
    for clave in VarDoms:
        linea = archivo.readline().strip()
        if linea.isdigit() and len(linea) == 1:
            linea = {int(linea)}
            VarDoms[clave] = linea

# print(VarDoms)
# VarDoms["A2"].discard(5)

# tarea pensar de como modelar el conjunto de restricciones sin modulos para solucionar por consistencia

def defColsConstraints(IdCols,Dom):
    Constraints=[]
    for id in IdCols:
        ConstraintVars=[f"{id}{i}" for i in Dom]
        Constraints.append(ConstraintVars)
    return Constraints

# print(defColsConstraints(Idcols,Dom))


def defRowsConstraints(IdCols,Dom):
    Constraints=[]
    for i in Dom:
        ConstraintVars=[f"{id}{i}" for id in IdCols]
        Constraints.append(ConstraintVars)
    return Constraints

# print(defRowsConstraints(Idcols,Dom))

def def3x3Constraints(IdCols, Dom):
    Constraints = []
    
    row_blocks = [IdCols[i:i+3] for i in range(0, 9, 3)]  # [['A','B','C'], ['D','E','F'], ['G','H','I']]
    col_blocks = [list(range(i, i+3)) for i in range(1, 10, 3)]  # [[1,2,3], [4,5,6], [7,8,9]]

    for rows in row_blocks:
        for cols in col_blocks:
            block = [f"{r}{c}" for r in rows for c in cols]
            Constraints.append(block)

    return Constraints

# print(def3x3Constraints(Idcols,Dom))

Constraints=defColsConstraints(Idcols,Dom) + defRowsConstraints(Idcols,Dom) + def3x3Constraints(Idcols,Dom)

# print(Constraints)

def ConsistenceDifference(Constraints,VarDoms):

    for constraint in Constraints:

        for var in constraint:
            if len(VarDoms[var])==1:
                for othervar in constraint:
                    if othervar!=var:
                        VarDoms[othervar].difference_update(VarDoms[var])
    return VarDoms

print(ConsistenceDifference(Constraints,VarDoms))

