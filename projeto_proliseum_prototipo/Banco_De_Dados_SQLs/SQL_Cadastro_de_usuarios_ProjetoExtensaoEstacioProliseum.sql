CREATE TABLE tbl_usuario (
    id_de_usuario SERIAL PRIMARY KEY NOT NULL,
    nome_completo VARCHAR(255) NOT NULL,
    nome_de_usuario VARCHAR(100) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    biografia TEXT,
    genero VARCHAR(50),
    data_de_nascimento DATE NOT NULL,
    foto_de_perfil_de_usuario VARCHAR(255),
    foto_de_capa_de_usuario VARCHAR(255)
);

CREATE TABLE tbl_email (
    id_email SERIAL PRIMARY KEY NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    id_de_usuario INT REFERENCES tbl_usuario(id_de_usuario) NOT NULL
);

CREATE TABLE tbl_rede_social (
    id_rede_social SERIAL PRIMARY KEY NOT NULL,
    rede_social VARCHAR(255) UNIQUE NOT NULL,
    id_de_usuario INT REFERENCES tbl_usuario(id_de_usuario) NOT NULL
);

CREATE TABLE tbl_jogo (
    id_jogo SERIAL PRIMARY KEY NOT NULL,
    nome_do_jogo VARCHAR(255) NOT NULL,
    foto_do_jogo VARCHAR(255) NOT NULL
);

CREATE TABLE tbl_rank (
    id_rank SERIAL PRIMARY KEY NOT NULL,
    nome_do_rank VARCHAR(255) NOT NULL,
    foto_do_rank VARCHAR(255) NOT NULL
);

CREATE TABLE tbl_funcao (
    id_funcao SERIAL PRIMARY KEY NOT NULL,
    nome_da_funcao VARCHAR(255) NOT NULL,
    foto_da_funcao VARCHAR(255) NOT NULL
);

CREATE TABLE tbl_jogador (
    id_de_jogador SERIAL PRIMARY KEY NOT NULL,
    nickname VARCHAR(100) NOT NULL,
    biografia_de_jogador TEXT,
    foto_de_perfil_do_jogador VARCHAR(255),
    foto_de_capa_do_jogador VARCHAR(255),
    id_de_usuario INT REFERENCES tbl_usuario(id_de_usuario) UNIQUE NOT NULL
);

CREATE TABLE tbl_time (
    id_time SERIAL PRIMARY KEY NOT NULL,
    nome_do_time VARCHAR(255) NOT NULL,
    biografia_do_time TEXT,
    foto_de_perfil_do_time VARCHAR(255),
    foto_de_capa_do_time VARCHAR(255),
    id_jogo INT REFERENCES tbl_jogo(id_jogo) NOT NULL
);

CREATE TABLE tbl_jogador_time (
    id_de_jogador INT REFERENCES tbl_jogador(id_de_jogador) UNIQUE NOT NULL,
    id_time INT REFERENCES tbl_time(id_time) NOT NULL,
    PRIMARY KEY (id_de_jogador, id_time)
);

CREATE TABLE tbl_disponibilidade_de_jogador (
    id_postagem_do_jogador SERIAL PRIMARY KEY NOT NULL,
    descricao TEXT NOT NULL,
    horario_disponivel TIMESTAMP NOT NULL,
    pros TEXT,
    id_de_jogador INT REFERENCES tbl_jogador(id_de_jogador) UNIQUE NOT NULL,
    id_jogo INT REFERENCES tbl_jogo(id_jogo) NOT NULL,
    id_rank INT REFERENCES tbl_rank(id_rank) NOT NULL,
    id_funcao INT REFERENCES tbl_funcao(id_funcao) NOT NULL
);

CREATE TABLE tbl_peneira (
    id_da_peneira SERIAL PRIMARY KEY NOT NULL,
    descricao TEXT NOT NULL,
    horario_desejado TIMESTAMP NOT NULL,
    pros TEXT,
    id_time INT REFERENCES tbl_time(id_time) UNIQUE NOT NULL,
    id_jogo INT REFERENCES tbl_jogo(id_jogo) NOT NULL,
    id_rank INT REFERENCES tbl_rank(id_rank) NOT NULL,
    id_funcao INT REFERENCES tbl_funcao(id_funcao) NOT NULL
);

CREATE TABLE tbl_inscricao_peneira (
    id_de_jogador INT REFERENCES tbl_jogador(id_de_jogador) NOT NULL,
    id_da_peneira INT REFERENCES tbl_peneira(id_da_peneira) NOT NULL,
    PRIMARY KEY (id_de_jogador, id_da_peneira)
);

COMMIT;
