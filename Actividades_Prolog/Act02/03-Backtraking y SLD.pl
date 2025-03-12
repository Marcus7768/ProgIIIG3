%------------- hechos para conexiones direccionales del grafo y el costo ----------

conectado(vancouver, edmonton, 16).
conectado(vancouver, calgary, 13).

conectado(edmonton, saskatoon, 12).

conectado(calgary, edmonton, 4).
conectado(calgary, regina, 14).

conectado(regina, saskatoon, 7).
conectado(regina, winnipeg, 4).

conectado(saskatoon, calgary, 9).
conectado(saskatoon, winnipeg, 4).


%----------- consulta de determinar si un nodo tiene o no tiene aristas ---------------

tieneArista(X):-
    conectado(X, _, _).


%---------- consulta de determinar el costo de ir de X a F pasando por Y ---------------

costoDeIrA(X, Z, Y, Costo):-
    conectado(X, Y, C1) , conectado(Y, Z, C2) , Costo is C1 + C2.

%----------------- consulta de saber si hay un camino entre dos nodos -------------------

caminoDe(X, Y):- conectado(X, Y,_).
caminoDe(X, Y):- conectado(X, Z,_) , caminoDe(Z, Y). 