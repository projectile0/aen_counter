create table athletes
(
    id       integer not null
        constraint sportsmans_pk
            primary key autoincrement,
    name     TEXT    not null,
    weight   integer,
    birthday TEXT    not null,
    league   integer not null
        constraint athletes_leagues_id_fk
            references leagues
);