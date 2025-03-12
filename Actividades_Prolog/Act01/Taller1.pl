# 1)
%--------------- hechos para la definición de personas en los Simpson y sus relaciones familiares ---------

hombre(bart).
hombre(homero).
hombre(abrajam).
hombre(herbert).
hombre(clancy).

mujer(marge).
mujer(lisa).
mujer(selma).
mujer(patty).
mujer(maggie).
mujer(ling).
mujer(mona).
mujer(jacqueline).

padre(abrajam, homero).
padre(abrajam, herbert).
padre(clancy, selma).
padre(clancy, patty).
padre(clancy, marge).
padre(homero, bart).
padre(homero, lisa).
padre(homero, maggie).

madre(marge, lisa).
madre(marge, bart).
madre(marge, maggie).
madre(selma, ling).
madre(jacqueline, patty).
madre(jacqueline, selma).
madre(jacqueline, marge).
madre(mona, homero).
madre(mona, herbert).

hijo(homero, mona).
hijo(homero, abrajam).
hijo(herbert, mona).
hijo(herbert, abrajam).
hijo(bart, homero).
hijo(bart, marge).
hijo(lisa, homero).
hijo(lisa, marge).
hijo(maggie, homero).
hijo(maggie, marge).
hijo(ling, selma).
hijo(marge, jacqueline).
hijo(marge, clancy).
hijo(patty, jacqueline).
hijo(patty, clancy).
hijo(selma, clancy).
hijo(selma, jacqueline).

% -------------- reglas de las relaciones familiares de mayor orden -------------


abueloPaterno(X, Y):- 
    hombre(X), padre(X, Z) , padre(Z, Y).
abuelaPaterna(X, Y):- 
    mujer(X), madre(X, Z) , padre(Z, Y).

abueloMaterno(X, Y):- 
    hombre(X), padre(X, Z) , madre(Z, Y).
abuelaMaterna(X, Y):- 
    mujer(X), madre(X, Z) , madre(Z, Y).


hermana(X, Y):-
    mujer(X), padre(P, X) , padre(P, Y) , madre(M, X) , madre(M, Y) , X \= Y.
hermano(X, Y):-
    hombre(X) , padre(P, X) , padre(P, Y) , madre(M, X) , madre(M, Y) , X \= Y.                                                                  

tio(X, Y):-
    hermano(X, P) , padre(P, Y) ; hermano(X, M) , madre(M, Y).


tia(X, Y):-
    hermana(X, P) , padre(P, Y) ; hermana(X, M) , madre(M, Y).

    
primos(X, Y):-
    padre(P1, X), padre(P2, Y), hermano(P1, P2), X \= Y ; madre(M1, X), madre(M2, Y), hermana(M1, M2), X \= Y .


primos(X, Y):-
    padre(P, X), madre(M, Y), hermano(P, M), X \= Y ; madre(M, X), padre(P, Y), hermana(M, P), X \= Y.


    
prima(X, Y):-
    mujer(X), primos(X, Y).
primo(X, Y):-
    hombre(X), primos(X, Y).
    



# 2) ----------------------------------------------------------------------------------------------

% ----------- hechos del enunciado entregados ------------------------

hostil(coreaDelSur).
esEstadoUnidense(coronelWest).
vendioArmasA(coronelWest, coreaDelSur).

criminal(X, Y):-
    esEstadoUnidense(X), vendioArmasA(X, Y), hostil(Y).