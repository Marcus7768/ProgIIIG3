# 1)
%--------------- hechos para la definición de personas en los Simpson y sus relaciones familiares ---------

% Listas de hombres y mujeres
hombres([bart, homero, abrajam, herbert, clancy]).
mujeres([marge, lisa, selma, patty, maggie, ling, mona, jacqueline]).

% Relaciones familiares con listas
padres([
    (abrajam, [homero, herbert]),
    (clancy, [selma, patty, marge]),
    (homero, [bart, lisa, maggie])
]).

madres([
    (marge, [lisa, bart, maggie]),
    (selma, [ling]),
    (jacqueline, [patty, selma, marge]),
    (mona, [homero, herbert])
]).

% -------------- reglas de las relaciones familiares de mayor orden -------------

% Buscar en la lista de hombres o mujeres
es_hombre(X) :- hombres(H), member(X, H).
es_mujer(X) :- mujeres(M), member(X, M).

% Buscar padres e hijos en la lista de padres
es_padre(P, Hijo) :- padres(Lista), member((P, Hijos), Lista), member(Hijo, Hijos).
es_madre(M, Hijo) :- madres(Lista), member((M, Hijos), Lista), member(Hijo, Hijos).

abueloPaterno(X, Y):- 
    es_hombre(X), es_padre(X, Z), es_padre(Z, Y).

abuelaPaterna(X, Y):- 
    es_mujer(X), es_madre(X, Z), es_padre(Z, Y).

abueloMaterno(X, Y):- 
    es_hombre(X), es_padre(X, Z), es_madre(Z, Y).

abuelaMaterna(X, Y):- 
    es_mujer(X), es_madre(X, Z), es_madre(Z, Y).

hermana(X, Y):- 
    es_mujer(X), es_padre(P, X), es_padre(P, Y), es_madre(M, X), es_madre(M, Y), X \= Y.

hermano(X, Y):- 
    es_hombre(X), es_padre(P, X), es_padre(P, Y), es_madre(M, X), es_madre(M, Y), X \= Y.

tio(X, Y):- 
    hermano(X, P), es_padre(P, Y) ; hermano(X, M), es_madre(M, Y).

tia(X, Y):- 
    hermana(X, P), es_padre(P, Y) ; hermana(X, M), es_madre(M, Y).

primos(X, Y):- 
    es_padre(P1, X), es_padre(P2, Y), hermano(P1, P2), X \= Y ; 
    es_madre(M1, X), es_madre(M2, Y), hermana(M1, M2), X \= Y.

prima(X, Y):- 
    es_mujer(X), primos(X, Y).

primo(X, Y):- 
    es_hombre(X), primos(X, Y).