%------------- hechos para conexiones direccionales del grafo y el costo ----------


conectado(ciudad(vancouve), ciudad(edmonton), costo(16)).
conectado(ciudad(vancouver), ciudad(calgary), costo(13)).

conectado(ciudad(edmonton), ciudad(saskatoon), costo(12)).

conectado(ciudad(calgary), ciudad(edmonton), costo(4)).
conectado(ciudad(calgary), ciudad(regina), costo(14)).

conectado(ciudad(regina), ciudad(saskatoon), costo(7)).
conectado(ciudad(regina), ciudad(winnipeg), costo(4)).

conectado(ciudad(saskatoon), ciudad(calgary), costo(9)).
conectado(ciudad(saskatoon), ciudad(winnipeg), costo(4)).


%----------- consulta de determinciudad(X)r si un nodo tiene o no tiene aristas ---------------

tieneArista(X):-
    conectado(City, _, _),
    City=..[ciudad,X].


%---------- consulta de determinar el costo de ir de X a F pasando por Y ---------------

costoDeIrA(X, Z, Y, Costo):-
    conectado(X, Y, C1) , conectado(Y, Z, C2) , Costo is C1 + C2.

%----------------- consulta de saber si hay un camino entre dos nodos -------------------

caminoDe(X, Y):- conectado(X, Y,_).
caminoDe(X, Y):- conectado(X, Z,_) , caminoDe(Z, Y). 

%----------------------------------------------------------------------------------------------------------------------

