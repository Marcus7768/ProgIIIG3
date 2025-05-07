% Caso base: generación 0, árbol vacío
generacion(0, [], []).

% Caso base: generación 0, nodo nil
generacion(0, [nil|T], L2) :-
    generacion(0, T, L2).

% Caso base: generación 0, tomar la raíz del nodo
generacion(0, [t(_, R, _)|T], [R|L2]) :-
    generacion(0, T, L2).

% Caso base general para árboles vacíos en generaciones > 0
generacion(_, [], []).

% Caso recursivo: generación N > 0, nodo nil
generacion(N, [nil|T], L2) :-
    generacion(N, T, L2).

% Caso recursivo: generación N > 0, procesar subárboles
generacion(N, [t(Left, _, Right)|T], L2) :-
    N > 0,
    N1 is N - 1,
    generacion(N1, [Left, Right], SubL),
    generacion(N, T, RestL),
    append(SubL, RestL, L2).