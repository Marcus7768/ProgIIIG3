
# ver p4sobre la estructura del sudoku
# como colocar restricciones y tecnicas de consistencia



for id in Idcols:
    constraintVars= [f"{id}{i}" for i in Dom]
    print(constraintVars)

def defColsConstraints(Icols,Dom):
    Constraints=[]


# tarea la funcion que devuelve los 9 recuadros que hacen falta
#     