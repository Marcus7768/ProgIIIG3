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


# tablero="ProgIIIG1-Act08-KK5GGRJS-Board.txt"
# tablero="ProgIIIG1-Act08-KK5DDPQF-Board.txt"
tablero="ProgIIIG1-Act08-KK5VMPMA-Board.txt"


with open(tablero,"r") as archivo:
    for clave in VarDoms:
        linea = archivo.readline().strip() #0-4 & - & 
        if linea=="-":
            VarDoms[clave] = "Negro"
        elif linea.isalnum():
            VarDoms[clave] = linea



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


Constraints = defColsConstraints(VarDoms, Idcols) + defRowsConstraints(VarDoms, Idcols)
# print(Constraints)



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

def es_valido(var, valor, asignacion, Constraints):
    # Crear una copia temporal de la asignación
    temp_asignacion = asignacion.copy()
    temp_asignacion[var] = valor

    for constraint in Constraints:
        vars_bloque, suma = constraint
        valores = []
        for v in vars_bloque:
            if v in temp_asignacion:
                valores.append(temp_asignacion[v])
            else:
                valores.append(None)
        
        asignados = [v for v in valores if v is not None]

        # Verificar duplicados
        if len(asignados) != len(set(asignados)):
            return False

        # Verificar suma si todas están asignadas
        if None not in valores:
            if sum(asignados) != suma:
                return False

        # Verificar que no sobrepasemos la suma parcial
        if sum(asignados) > suma:
            return False

    return True

def backtracking(VarDoms, Constraints):
    def bt(asignacion):
        if len(asignacion) == len([v for v in VarDoms if isinstance(VarDoms[v], set)]):
            return asignacion  # ¡Todas las variables asignadas!

        # Seleccionamos la siguiente variable no asignada
        for var in VarDoms:
            if isinstance(VarDoms[var], set) and var not in asignacion:
                for valor in VarDoms[var]:
                    if es_valido(var, valor, asignacion, Constraints):
                        asignacion[var] = valor
                        result = bt(asignacion)
                        if result:
                            return result
                        del asignacion[var]  # backtrack
                return None  # No hay valor válido para esta variable
        return None  # No hay más variables

    return bt({})

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

anyChange = True
iteration = 1
while anyChange:
    print(f"Iteracion#{iteration}")
    iteration += 1
    anyChange = False
    mostrar_tablero(VarDoms)
    print("\n")
    # for constraint in Constraints:
    #     if ConsistenceKakuro([constraint], VarDoms):
    #         anyChange = True

print("Ahora aplicamos la busqueda\n")
solution = backtracking(VarDoms, Constraints)
if solution:
    for var in VarDoms:
        if isinstance(VarDoms[var], set) and var in solution:
            VarDoms[var] = {solution[var]}
    print("¡Solución encontrada!")
else:
    print("No se encontró solución.")

mostrar_tablero(VarDoms)