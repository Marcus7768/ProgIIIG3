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

# tablero="SD1AALFN-MF.txt"
# tablero="t-MF.txt"
# tablero="SD2OVFEP-F.txt"
# tablero="SD2PTZJZ-F.txt"
# tablero="SD9VMFYG-I.txt"
tablero="SD9MMWDX-I.txt"


with open(tablero,"r") as archivo:
    for clave in VarDoms:
        linea = archivo.readline().strip()
        if linea.isdigit() and len(linea) == 1:
            linea = {int(linea)}
            VarDoms[clave] = linea

# print(VarDoms)
# VarDoms["A2"].discard(5)



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
    anyChange=False
    for constraint in Constraints:

        for var in constraint:
            if len(VarDoms[var])==1:
                for othervar in constraint:
                    if othervar!=var:
                        oldDom = VarDoms[othervar].copy()
                        VarDoms[othervar].difference_update(VarDoms[var])
                        if(oldDom!=VarDoms[othervar]):
                            anyChange=True
    return anyChange

def DomsEqual(VarDoms, constraint):
    anyChange = False
    dom_to_vars = {}

    # Agrupar variables que tienen el mismo dominio (con más de un valor)
    for var in constraint:
        dom = VarDoms[var]
        if len(dom) > 1:
            dom_key = tuple(sorted(dom))  # usar como clave del diccionario
            if dom_key in dom_to_vars:
                dom_to_vars[dom_key].add(var)
            else:
                dom_to_vars[dom_key] = {var}

    # Para cada grupo de variables con dominio igual
    for dom, vars_with_same_dom in dom_to_vars.items():
        if len(dom) == len(vars_with_same_dom):  # aplicar sólo si #valores == #variables
            for var in constraint:
                if var not in vars_with_same_dom:
                    old_dom = VarDoms[var].copy()
                    VarDoms[var].difference_update(dom)
                    if VarDoms[var] != old_dom:
                        anyChange = True

    return anyChange

def NumAlone(VarDoms, Constraints):
    anyChange = False

    for constraint in Constraints:
        # 1. Contador: número -> lista de variables donde aparece
        num_locations = {}

        for var in constraint:
            for n in VarDoms[var]:
                if n not in num_locations:
                    num_locations[n] = [var]
                else:
                    num_locations[n].append(var)

        # 2. Si un número aparece en solo una variable, es un "hidden single"
        for n, vars_with_n in num_locations.items():
            if len(vars_with_n) == 1:
                var = vars_with_n[0]
                if len(VarDoms[var]) > 1:
                    VarDoms[var] = {n}
                    anyChange = True

    return anyChange


def mostrar_tablero(VarDoms):
    for i in range(1, 10):
        fila = ""
        for c in Idcols:
            val = VarDoms[f"{c}{i}"]
            fila += str(next(iter(val))) if len(val) == 1 else "."
            fila += " "
            if c in "CF": fila += "| "
        print(fila)
        if i in [3, 6]: print("-" * 21)
# print(ConsistenceDifference(Constraints,VarDoms))

def is_consistent(var, value, assignment, Constraints):
    """
    Verifica si asignar `value` a `var` es consistente con las restricciones y la asignación actual.
    """
    for constraint in Constraints:
        if var in constraint:
            for other in constraint:
                if other != var and other in assignment and assignment[other] == value:
                    return False
    return True

def conflict_var(var, assignment, Constraints):
    """
    Devuelve una variable con la que `var` entra en conflicto en las restricciones.
    """
    for constraint in Constraints:
        if var in constraint:
            for other in constraint:
                if other != var and other in assignment and assignment[other] == assignment[var]:
                    return other
    return None

def backjump_search(VarDoms, Constraints, assignment=None, var_order=None, level=0):
    if assignment is None:
        assignment = {}
    if var_order is None:
        var_order = list(VarDoms.keys())  # Orden fijo, se puede mejorar con heurísticas

    if len(assignment) == len(VarDoms):
        return assignment  # Solución encontrada

    current_var = var_order[level]
    for value in VarDoms[current_var]:
        if is_consistent(current_var, value, assignment, Constraints):
            assignment[current_var] = value
            result = backjump_search(VarDoms, Constraints, assignment, var_order, level + 1)
            if result:
                return result  # Solución válida encontrada
            else:
                conflict = conflict_var(current_var, assignment, Constraints)
                if conflict is not None and var_order.index(conflict) < level - 1:
                    return None  # Backjump: salto más allá del nivel anterior
        # Si no es consistente o falló el camino, intenta siguiente valor

    if current_var in assignment:
        del assignment[current_var]  # Backtrack
    return None


anyChange = True
iteration = 1
while anyChange:
    print(f"Iteracion#{iteration}")
    iteration += 1
    anyChange = False
    mostrar_tablero(VarDoms)
    print("\n")
    for constraint in Constraints:
        if ConsistenceDifference([constraint], VarDoms):
            anyChange = True
        if DomsEqual(VarDoms, constraint):
            anyChange = True
        if NumAlone(VarDoms, [constraint]):
            anyChange = True

print("Ahora aplicamos la busqueda\n")
solution = backjump_search(VarDoms, Constraints)
if solution:
    for var in VarDoms:
        VarDoms[var] = {solution[var]}
    print("¡Solución encontrada!")
else:
    print("No se encontró solución.")

mostrar_tablero(VarDoms)