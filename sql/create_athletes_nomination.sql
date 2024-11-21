create table athletes_nomination
(
    id         integer
        constraint athletes_nomination_pk
            primary key autoincrement
        constraint athletes_nomination_athletes_id_fk
            references athletes,
    sh_n_saber integer default 0,
    sh_n_sword integer default 0,
    triathlon  integer default 0
);