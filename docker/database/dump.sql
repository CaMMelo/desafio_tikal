create table if not exists crud_cliente (
    id serial primary key,
    nome varchar(80) not null,
    rg varchar(14) not null unique,
    cpf varchar(11) not null unique,
    data_nascimento date not null,
    sexo varchar(1) not null
);


create table if not exists crud_telefone (
    id serial primary key,
    ddd varchar(2) not null,
    numero varchar(8) not null unique,
    tipo varchar(2) not null unique,
    cliente_id integer not null,
    foreign key (cliente_id) references crud_cliente(id)
);


create table if not exists crud_email (
    id serial primary key,
    email varchar(88) not null,
    cliente_id integer not null,
    foreign key (cliente_id) references crud_cliente(id)
);
