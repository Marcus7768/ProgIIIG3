% 1)----------- Base de datos de relaciones familiares-----------------------
progenitor(clara, jose).
progenitor(tomas, jose).
progenitor(tomas, isabel).
progenitor(jose, ana).
progenitor(jose, patricia).
progenitor(patricia, jaime).

%2)---------------------- Definición de género-----------------------
hombre(tomas).
hombre(jose).
hombre(jaime).
mujer(clara).
mujer(isabel).
mujer(ana).
mujer(patricia).

% 3)-----------------------Regla para diferenciar personas-----------------------
dif(X,Y) :- X \= Y.

% -----------------------Reglas para las relaciones familiares-----------------------
es_madre(X) :- progenitor(X,_), mujer(X).

es_padre(X) :- progenitor(X,_), hombre(X).

es_hijo(X) :- progenitor(_,X), hombre(X).

hermana_de(X, Y) :- progenitor(Z, X), progenitor(Z, Y), mujer(X), dif(X,Y).

abuelo_de(X, Y) :- progenitor(X, Z), progenitor(Z, Y), hombre(X).

abuela_de(X, Y) :- progenitor(X, Z), progenitor(Z, Y), mujer(X).

hermanos(X, Y) :- progenitor(Z, X), progenitor(Z, Y), dif(X, Y).

tia(X, Y) :- progenitor(Z, Y), hermanos(X, Z), mujer(X), dif(X, Z).