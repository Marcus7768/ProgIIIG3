pieza(bicicleta, [rueda_delantera, cuadro, rueda_trasera]).

pieza(rueda_delantera, [llanta, radios, eje]).

pieza(cuadro, [manillar, sillon, traccion]).

pieza(traccion, [eje, plato, pedales, cadena]).

pieza(rueda_trasera, [llanta, radios, eje, pinyones]).

componentes(Pieza, Componentes) :-
    pieza(Pieza, Componentes).



generacion(0, [], []).

generacion(0, [t(_, R, _)|T], [R|L2]) :-  generacion(0, T, L2).

generacion(0, [nil|T], L2) :- generacion(0, T, L2).

generacion(_, [], []). 

generacion(N, [t(I, _, D)|T], L2) :-
    N > 0,
    N1 is N - 1,
    generacion(N1, [I, D], L), 
    generacion(N, T, L2T),
    append(L, L2T, L2).

generacion(N, [nil|T], L2) :-
    generacion(N, T, L2).