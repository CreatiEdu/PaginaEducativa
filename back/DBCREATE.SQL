CREATE DATABASE testback;
use testback;
create TABLE roles(
id_rol INT PRIMARY KEY AUTO_INCREMENT,
rol VARCHAR (20) NOT NULL
);
use testback;
CREATE TABLE usuarios(
    id_usuario INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR (75) NOT NULL,
    apellido VARCHAR (75) NOT NULL,
    dni INT NOT NULL,
    rol INT NOT NULL,
    usuario VARCHAR(100) NOT NULL UNIQUE,
    contraseña VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_usuario),
    FOREIGN KEY (rol) REFERENCES roles(id_rol)
);