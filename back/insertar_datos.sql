use testback;

-- 1. Usuarios

INSERT INTO usuarios (nombre, apellido, dni, rol, usuario, contraseña) VALUES
('Eric', 'Astrada', 46451230, 2, 'Negas', 'hash_pass_eric'),
('Marta', 'Gomez', 25300123, 1, 'Mgomez', 'hash_pass_marta'),
('Carlos', 'Lopez', 32987654, 2, 'Clopez', 'hash_pass_carlos')
ON DUPLICATE KEY UPDATE usuario=usuario;

 
-- 2. Productos
 
INSERT INTO productos (nombre, descripcion, precio, stock, url_imagen) VALUES
('Libro de Python', 'Guía completa para desarrollo backend.', 35.50, 50, 'url/imagen/python.jpg'),
('Taza Institucional', 'Taza con logo del curso de Programación.', 12.00, 200, 'url/imagen/taza.jpg'),
('Licencia Software', 'Licencia anual para software de diseño.', 99.99, 10, 'url/imagen/licencia.jpg')
ON DUPLICATE KEY UPDATE nombre=nombre;

 
-- 3. Estado de cuotas
 
INSERT INTO estado (estado) VALUES 
('Pendiente'),
('Pagada'),
('Vencida')
ON DUPLICATE KEY UPDATE estado=estado;

 
-- 4. Alumnos
 
INSERT INTO alumnos (id_usuario, nombre, apellido, dni, curso) VALUES
(1, 'Eric', 'Astrada', 46451230, 'Programación Web Avanzada'),
(3, 'Carla', 'Fernandez', 40112233, 'Diseño Gráfico 2024')
ON DUPLICATE KEY UPDATE curso=curso;


-- 5. Cuotas
INSERT INTO cuotas (id_alumno, concepto, curso_grado, estado, monto_base, monto_con_recargo, fecha_vencimiento1, fecha_vencimiento2, monto_recargo, fecha_pago) VALUES
-- Cuotas de Eric
(1, 'Matrícula 2024', 1, 2, 7500.00, 7500.00, '2024-03-01', NULL, 0.00, '2024-02-28'),
(1, 'Cuota Septiembre', 1, 3, 5000.00, 5200.00, '2024-09-10', '2024-09-20', 200.00, NULL),
(1, 'Cuota Octubre', 1, 1, 5000.00, NULL, '2024-10-10', '2024-10-20', NULL, NULL),
-- Cuotas de Carla
(2, 'Matrícula 2024', 2, 2, 8000.00, 8000.00, '2024-03-05', NULL, 0.00, '2024-03-01'),
(2, 'Cuota Septiembre', 2, 1, 5500.00, NULL, '2024-09-15', '2024-09-25', NULL, NULL)
ON DUPLICATE KEY UPDATE concepto=concepto;


-- 6. Pedidos

INSERT INTO pedido (id_producto, id_usuario, nombre_producto, fecha_pedido, total) VALUES
(1, 1, 'Libro de Python', '2024-10-12', 35.50),
(2, 3, 'Taza Institucional', '2024-10-13', 24.00),
(3, 2, 'Licencia Software', '2024-10-14', 99.99)
ON DUPLICATE KEY UPDATE nombre_producto=nombre_producto;

-- 7. Pago
INSERT INTO pago (fecha_pago, descripcion, monto_pagado, concepto, estado_pago, referencia_de_transacion) VALUES
('2024-02-28', 'Pago Matrícula Alumno ID 1', 7500.00, 'Matrícula', 'Completado', 'REF7500A1'),
('2024-10-12', 'Pago Pedido ID 1', 35.50, 'Pedido', 'Completado', 'REF3550P1'),
('2024-10-14', 'Pago Licencia Marta', 99.99, 'Pedido', 'Completado', 'REF9999P3')
ON DUPLICATE KEY UPDATE referencia_de_transacion=referencia_de_transacion;