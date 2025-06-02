Dom=set(range(1,10))
# print(Dom)

Idcols = "ABCDEFGHI"

import itertools as it

Varkeys = list(it.product(Dom,Idcols))
# print(Varkeys)

# convertir lista de tuplas a strings

strVarkeys= [f"{key[1]}{key[0]}" for key in Varkeys]

# print(strVarkeys)

VarDoms={key:Dom.copy() for key in strVarkeys}

# print(VarDoms)



# tableros disponibles, se debe comentar todos menos el que se desea utilizar


tablero="KK5GGRJS-MD.txt"


with open(tablero,"r") as archivo:
    for clave in VarDoms:
        linea = archivo.readline().strip() #0-4 & - & 
        if linea=="-":
            VarDoms[clave] = "Negro"
        elif linea.isalnum():
            VarDoms[clave] = linea




            # linea = {int(linea)}
            # VarDoms[clave] = linea

# print(VarDoms)
# VarDoms["A2"].discard(5)

# def defColsConstraints(IdCols,Dom):
#     Constraints=[]
#     for id in IdCols:
#         ConstraintVars=[f"{id}{i}" for i in Dom]
#         Constraints.append(ConstraintVars)
#     return Constraints


# def defColsConstraints(Vardoms,IdCols):
#     Constraints = []
    
#     for i in range(1,10):
#         for key in VarDoms:
#             print(VarDoms[key])

#     return Constraints

# def defColsConstraints(VarDoms,IdCols,Dom):
#     Constraints=[]

#     for id in IdCols:
#         ConstraintVars = []
#         for i in Dom:
#             cadena = f"{id}{i}"
#             linea = str(VarDoms.get(cadena))
#             if linea == "Negro" and linea.isalnum(): 
#                 for j in Dom:
#                     if j != i:
                                 
#             else:
#                 ConstraintVars.append(cadena)
#         Constraints.append(ConstraintVars)

#     return Constraints

# def defColsConstraints(VarDoms, IdCols):
#     constraints = []
#     for col in IdCols:
#         bloque = []
#         for row in range(1, 10):
#             clave = f"{col}{row}"
#             valor = VarDoms[clave]
#             if isinstance(valor, set):  # blanca
#                 bloque.append(clave)
#             else:  # negra o sumador
#                 if bloque:
#                     constraints.append(bloque)
#                     bloque = []
#         if bloque:  # Si termina la columna con blancas
#             constraints.append(bloque)
#     return constraints

# -----------------------------------------------------------------------------------------

def defColsConstraints(VarDoms, IdCols):
    constraints = []
    for col in IdCols:
        bloque = []
        suma = None
        for row in range(1, 10):
            clave = f"{col}{row}"
            valor = VarDoms[clave]
            if isinstance(valor, set):  # blanca
                bloque.append(clave)
            else:  # negra o sumador
                if bloque:
                    # Revisar celda anterior para buscar la suma
                    fila_suma = row - len(bloque) - 1
                    if fila_suma >= 1:
                        clave_suma = f"{col}{fila_suma}"
                        valor_suma = VarDoms.get(clave_suma, "")
                        if isinstance(valor_suma, str) and "y" in valor_suma:
                            try:
                                _, suma_str = valor_suma.split("y")
                                suma = int(suma_str)
                                if suma > 0:
                                    constraints.append([bloque.copy(), suma])
                            except:
                                pass  # formato inválido, se ignora
                    bloque = []
        if bloque:
            fila_suma = 9 - len(bloque)
            if fila_suma >= 1:
                clave_suma = f"{col}{fila_suma}"
                valor_suma = VarDoms.get(clave_suma, "")
                if isinstance(valor_suma, str) and "y" in valor_suma:
                    try:
                        _, suma_str = valor_suma.split("y")
                        suma = int(suma_str)
                        if suma > 0:
                            constraints.append([bloque.copy(), suma])
                    except:
                        pass
            bloque = []
    return constraints

# -----------------------------------------------------------------------------------------


# def defRowsConstraints(VarDoms, IdCols):
#     constraints = []
#     for row in range(1, 10):  # Filas de 1 a 9
#         bloque = []
#         for col in IdCols:    # Columnas de A a I
#             clave = f"{col}{row}"
#             valor = VarDoms[clave]
#             if isinstance(valor, set):  # Es celda blanca
#                 bloque.append(clave)
#             else:  # Celda negra o con sumador
#                 if bloque:
#                     constraints.append(bloque)
#                     bloque = []
#         if bloque:  # Si termina la fila con blancas
#             constraints.append(bloque)
#     return constraints

# -----------------------------------------------------------------------------------------

def defRowsConstraints(VarDoms, IdCols):
    constraints = []
    for row in range(1, 10):
        bloque = []
        suma = None
        for col_index, col in enumerate(IdCols):
            clave = f"{col}{row}"
            valor = VarDoms[clave]
            if isinstance(valor, set):  # celda blanca
                bloque.append(clave)
            else:  # celda negra o sumador
                if bloque:
                    # Revisar celda anterior (a la izquierda) para la suma
                    col_suma_idx = col_index - len(bloque) - 1
                    if col_suma_idx >= 0:
                        col_suma = IdCols[col_suma_idx]
                        clave_suma = f"{col_suma}{row}"
                        valor_suma = VarDoms.get(clave_suma, "")
                        if isinstance(valor_suma, str) and "y" in valor_suma:
                            try:
                                suma_str, _ = valor_suma.split("y")
                                suma = int(suma_str)
                                if suma > 0:
                                    constraints.append([bloque.copy(), suma])
                            except:
                                pass  # formato inválido
                    bloque = []
        if bloque:
            col_suma_idx = 8 - len(bloque)
            if col_suma_idx >= 0:
                col_suma = IdCols[col_suma_idx]
                clave_suma = f"{col_suma}{row}"
                valor_suma = VarDoms.get(clave_suma, "")
                if isinstance(valor_suma, str) and "y" in valor_suma:
                    try:
                        suma_str, _ = valor_suma.split("y")
                        suma = int(suma_str)
                        if suma > 0:
                            constraints.append([bloque.copy(), suma])
                    except:
                        pass
            bloque = []
    return constraints


# -----------------------------------------------------------------------------------------




Constraints = defColsConstraints(VarDoms, Idcols) + defRowsConstraints(VarDoms, Idcols)
print(Constraints)

# [[[b6, b7, b8], 19]   ...  []   []   []  []]

# def ConsistenceDifference(Constraints,VarDoms):
#     anyChange=False
#     for constraint in Constraints:

#         for var in constraint:
#             if len(VarDoms[var])==1:
#                 for othervar in constraint:
#                     if othervar!=var:
#                         oldDom = VarDoms[othervar].copy()
#                         VarDoms[othervar].difference_update(VarDoms[var])
#                         if(oldDom!=VarDoms[othervar]):
#                             anyChange=True
#     return anyChange



# def Consistence(Constraints,Vardoms):
#     anyChange = False

#     for constraits in Constraints:
#         for Var in constraits:



#     return anyChange



def ConsistenceKakuro(Constraints, VarDoms):
    anyChange = False
    for constraint in Constraints:
        vars_bloque, suma = constraint
        asignadas = {v: next(iter(VarDoms[v])) for v in vars_bloque if len(VarDoms[v]) == 1}
        no_asignadas = [v for v in vars_bloque if len(VarDoms[v]) > 1]

        # 1. Eliminar valores asignados en el mismo bloque (como Sudoku)
        for v_asig, val in asignadas.items():
            for v in no_asignadas:
                oldDom = VarDoms[v].copy()
                VarDoms[v].discard(val)
                if VarDoms[v] != oldDom:
                    anyChange = True

        # 2. Generar combinaciones válidas para las no asignadas
        doms = [VarDoms[v] for v in no_asignadas]
        posibles_combinaciones = []
        for comb in it.product(*doms):
            if len(set(comb)) == len(comb):  # sin repeticiones
                total = sum(comb) + sum(asignadas.values())
                if total == suma:
                    posibles_combinaciones.append(comb)

        # 3. Recortar dominios según combinaciones válidas
        for i, v in enumerate(no_asignadas):
            posibles_valores = set(comb[i] for comb in posibles_combinaciones)
            oldDom = VarDoms[v].copy()
            VarDoms[v].intersection_update(posibles_valores)
            if VarDoms[v] != oldDom:
                anyChange = True

    return anyChange


anyChange = True
iteration = 1
while anyChange:
    print(f"Iteracion#{iteration}")
    iteration += 1
    anyChange = False
    print(VarDoms)
    print("\n")
    for constraint in Constraints:
        if ConsistenceKakuro([constraint], VarDoms):
            anyChange = True