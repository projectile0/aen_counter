create table leagues
(
    id     integer not null
        constraint leagues_pk
            primary key autoincrement,
    league TEXT    not null
);

