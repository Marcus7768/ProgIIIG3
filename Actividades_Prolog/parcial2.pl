

% homero-------------------------------------------
persona(homer, [bart, lisa], [
    evento(nacimiento, 1956),
    evento(graduacion, 1974),
    evento(boda, 1980),
    evento(trabajo_en_planta, 1980),
    evento(campeon_bolos, 1990),
    evento(gira_rock, 1993),
    evento(astronauta, 1994),
    evento(desempleado, 1995)
]).

% marge--------------------------------------
persona(marge, [bart, lisa], [
    evento(nacimiento, 1958),
    evento(graduacion, 1976),
    evento(boda, 1980),
    evento(pinto_a_burns, 1992),
    evento(arresto, 1993),
    evento(hospital_psiquiatrico, 1997),
    evento(telerrealidad, 2001)
]).

% bart----------------------------------------------------
persona(bart, [], [
    evento(nacimiento, 1980),
    evento(iq, 1990),
    evento(revolucion_escolar, 1991),
    evento(estrella_tv, 1993),
    evento(heroico, 1995),
    evento(campeonato_deportivo, 1999),
    evento(expulsion, 2000)
]).

% lisa-----------------------------------------------------
persona(lisa, [], [
    evento(nacimiento, 1982),
    evento(saxofon, 1988),
    evento(honores, 1993),
    evento(bleeding_gums, 1994),
    evento(vegetariana, 1995),
    evento(premio_ambiental, 1997),
    evento(presidenta, 2010)
]).

%------Linea descendencia------------------------------------------------------------

linea_de_descendencia(Nombre, T) :-
    persona(Nombre, Hijos, _),
    linea_de_descendencia_aux(Hijos, T).

linea_de_descendencia_aux([], []).

linea_de_descendencia_aux([Hijo|Resto], D) :-
    linea_de_descendencia(Hijo, DH),
    linea_de_descendencia_aux(Resto, DR),
    append([Hijo|DH], DR, D).


%------evento reciente------------------------------------------------------------

evento_mas_reciente(Nombre, R) :-
    persona(Nombre, _, Eventos),
    mas_reciente(Eventos, R).

mas_reciente([E], E).  % Caso base: solo queda un evento

mas_reciente([evento(T1, A1), evento(T2, A2) | Resto], R) :-
    ( A1 >= A2 ->
        mas_reciente([evento(T1, A1) | Resto], R)
    ;
        mas_reciente([evento(T2, A2) | Resto], R)
    ).


%------historia familiar------------------------------------------------------------

% historia_familiar(Nombre, EventosOrdenados)
historia_familiar(Nombre, EventosOrdenados) :-
    persona(Nombre, Hijos, EventosPropios),
    historia_descendientes(Hijos, EventosHijos),
    append(EventosPropios, EventosHijos, TodosEventos),
    sort_eventos_por_anio(TodosEventos, EventosOrdenados).

% historia_descendientes(ListaDeHijos, Eventos)
historia_descendientes([], []).

historia_descendientes([Hijo|Resto], EventosTotales) :-
    historia_familiar(Hijo, EventosHijo),
    historia_descendientes(Resto, EventosResto),
    append(EventosHijo, EventosResto, EventosTotales).

% Ordenamiento por año
sort_eventos_por_anio(Eventos, Ordenados) :-
    predsort(comparar_eventos, Eventos, Ordenados).

comparar_eventos(Delta, evento(_, A1), evento(_, A2)) :-
    compare(Delta, A1, A2).