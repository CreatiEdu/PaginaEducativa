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

use testback;
INSERT INTO roles (rol) VALUES ('administrador');
INSERT INTO roles (rol) VALUES ('Usuario');

CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL CHECK (precio >= 0),
    stock INT NOT NULL DEFAULT 0 CHECK (stock >= 0),
    url_imagen VARCHAR(255),
    UNIQUE (nombre)
);

CREATE TABLE pago (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    fecha_pago DATE,
    descripcion TEXT,
    monto_pagado DECIMAL(10,2) NOT NULL CHECK (monto_pagado >= 0),
    concepto VARCHAR(75),
    estado_pago VARCHAR(255),
    referencia_de_transacion VARCHAR(75)
    );
    
CREATE TABLE alumnos(
    id_alumno INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    nombre VARCHAR (75) NOT NULL,
    apellido VARCHAR (75) NOT NULL,
    dni INT NOT NULL,
    curso VARCHAR(50) NOT NULL UNIQUE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);


create TABLE estado(
id_estado INT PRIMARY KEY AUTO_INCREMENT,
estado VARCHAR (10) NOT NULL
);

CREATE TABLE cuotas (
    id_cuota INT AUTO_INCREMENT PRIMARY KEY,
    id_alumno INT  NOT NULL, 
    concepto VARCHAR(100),
    curso_grado INT  NOT NULL, 
    estado INT NOT NULL DEFAULT 1,
    monto_base DECIMAL(10,2)  NOT NULL,
	monto_con_recargo DECIMAL(10,2),
    fecha_vencimiento1 DATE,
	fecha_vencimiento2 DATE,
    monto_recargo FLOAT,
    fecha_pago DATE,
    FOREIGN KEY (id_alumno) REFERENCES alumnos(id_alumno),
    FOREIGN KEY (estado) REFERENCES estado(id_estado)
);

CREATE TABLE pedido(
    id_pedido INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_producto INT NOT NULL,
	id_usuario INT NOT NULL, 
    nombre_producto VARCHAR (75) NOT NULL,
    fecha_pedido DATE,
    total DECIMAL(10,2),
	FOREIGN KEY (id_producto) REFERENCES productos(id_producto),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);