SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

CREATE DATABASE IF NOT EXISTS `usuarios` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `usuarios`;

DROP TABLE IF EXISTS `asignaturas`;
CREATE TABLE IF NOT EXISTS `asignaturas` (
  `id_asignatura` int DEFAULT NULL,
  `nombre_asignatura` varchar(16) DEFAULT NULL,
  `descripción_asignatura` varchar(42) DEFAULT NULL,
  `id_docente` int DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

INSERT INTO `asignaturas` (`id_asignatura`, `nombre_asignatura`, `descripción_asignatura`, `id_docente`) VALUES
(1, 'Matematicas', 'area de algebra, calculo', 1),
(2, 'Sociales', 'altlas, politica, leyes', 4),
(3, 'Ingles', 'speaking, reading, listening', 18),
(4, 'Español', 'literatura', 2),
(5, 'Educación Fisica', 'practicar deportes y ejercicios', 9),
(6, 'Biologia', 'estudiar seres vivos', 7),
(7, 'Quimica', 'estudio de reacciones quimicas', 6),
(8, 'Tecnologia', 'word,excel,power point, one drive', 16),
(9, 'Filosofia', 'estudios de filosofos', 20),
(10, 'Fisica', 'estudio de ondas', 5),
(11, 'Geografia', 'estudio del planeta y sus alrededores', 8),
(12, 'Religión', 'pensamiento del ser humano y sus creencias', 17);

DROP TABLE IF EXISTS `calificaciones`;
CREATE TABLE IF NOT EXISTS `calificaciones` (
  `id_calificacion` int DEFAULT NULL,
  `id_asignatura` int DEFAULT NULL,
  `calificación` decimal(2,1) DEFAULT NULL,
  `retroalimentacion` varchar(21) DEFAULT NULL,
  `fecha_calificacion` varchar(10) DEFAULT NULL,
  `asignatura` varchar(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

INSERT INTO `calificaciones` (`id_calificacion`, `id_asignatura`, `calificación`, `retroalimentacion`, `fecha_calificacion`, `asignatura`) VALUES
(1, 4, 4.5, 'falta mejor redaccion', '6/04/2025', 'biologia'),
(2, 5, 3.4, 'mejorar ortografia', '7/04/2025', 'quimica'),
(3, 6, 4.6, 'bien', '8/04/2025', 'religion'),
(4, 7, 3.8, 'bien', '9/04/2025', 'fisica'),
(5, 8, 4.7, 'excelente', '10/04/2025', 'matematicas');

DROP TABLE IF EXISTS `docentes`;
CREATE TABLE IF NOT EXISTS `docentes` (
  `id_docente` int DEFAULT NULL,
  `nombre_docente` varchar(9) DEFAULT NULL,
  `apellido_docente` varchar(9) DEFAULT NULL,
  `identificacion` bigint DEFAULT NULL,
  `edad` int DEFAULT NULL,
  `correo_electronico` varchar(28) DEFAULT NULL,
  `telefono` bigint DEFAULT NULL,
  `asignatura_correspondiente` varchar(19) DEFAULT NULL,
  `estado` varchar(6) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

INSERT INTO `docentes` (`id_docente`, `nombre_docente`, `apellido_docente`, `identificacion`, `edad`, `correo_electronico`, `telefono`, `asignatura_correspondiente`, `estado`) VALUES
(1, 'Javier', 'Herrera', 2098767812, 34, 'javier.herrera@gmail.com', 3009876543, 'Matemáticas', 'Activo'),
(2, 'Martha', 'Castro', 3456789012, 28, 'martha.castro@gmail.com', 3012345678, 'Lengua y Literatura', 'Activo'),
(3, 'Ricardo', 'López', 1098765432, 40, 'ricardo.lopez@gmail.com', 3023456789, 'Historia', 'Activo'),
(4, 'Lucía', 'Sánchez', 2098767854, 33, 'lucia.sanchez@gmail.com', 3034567890, 'Ciencias Sociales', 'Activo'),
(5, 'Alberto', 'González', 9876543210, 45, 'alberto.gonzalez@gmail.com', 3045678901, 'Física', 'Activo'),
(6, 'Teresa', 'Mendoza', 10345567764, 29, 'teresa.mendoza@gmail.com', 3056789012, 'Química', 'Activo'),
(7, 'Ricardo', 'Jiménez', 4567890123, 38, 'ricardo.jimenez@gmail.com', 3067890123, 'Biología', 'Activo'),
(8, 'Carolina', 'Ruiz', 1234567890, 32, 'carolina.ruiz@gmail.com', 3078901234, 'Geografía', 'Activo'),
(9, 'Alejandro', 'Martínez', 2023456789, 50, 'alejandro.martinez@gmail.com', 3089012345, 'Educación Física', 'Activo'),
(10, 'Beatriz', 'Díaz', 3123456789, 27, 'beatriz.diaz@gmail.com', 3090123456, 'Filosofía', 'Activo'),
(11, 'Luis', 'Fernández', 9234567890, 41, 'luis.fernandez@gmail.com', 3101234567, 'Arte', 'Activo'),
(12, 'Sara', 'Rodríguez', 1045678901, 35, 'sara.rodriguez@gmail.com', 3112345678, 'Lengua y Literatura', 'Activo'),
(13, 'Francisco', 'García', 2145678901, 39, 'francisco.garcia@gmail.com', 3123456789, 'Matemáticas', 'Activo'),
(14, 'Carmen', 'Pérez', 3056789012, 42, 'carmen.perez@gmail.com', 3134567890, 'Psicología', 'Activo'),
(15, 'Eduardo', 'Torres', 4098765432, 33, 'eduardo.torres@gmail.com', 3145678901, 'Tecnología', 'Activo'),
(16, 'Elena', 'Fernández', 5198765432, 36, 'elena.fernandez@gmail.com', 3156789012, 'Historia', 'Activo'),
(17, 'Javier', 'Rodríguez', 6034567890, 30, 'javier.rodriguez@gmail.com', 3167890123, 'Ciencias Religiosas', 'Activo'),
(18, 'Marta', 'Gómez', 7098765432, 26, 'marta.gomez@gmail.com', 3178901234, 'Inglés', 'Activo'),
(19, 'Mario', 'Sánchez', 8098765432, 43, 'mario.sanchez@gmail.com', 3189012345, 'Matemáticas', 'Activo'),
(20, 'Laura', 'Hernández', 9034567890, 31, 'laura.hernandez@gmail.com', 3190123456, 'Filosofía', 'Activo');

DROP TABLE IF EXISTS `estudiantes`;
CREATE TABLE IF NOT EXISTS `estudiantes` (
  `id_estudiantes` int DEFAULT NULL,
  `nombre_estudiante` varchar(9) DEFAULT NULL,
  `apellido_estudiante` varchar(9) DEFAULT NULL,
  `tipo_de_identificacion` varchar(2) DEFAULT NULL,
  `numero_de_identificacion` int DEFAULT NULL,
  `edad` int DEFAULT NULL,
  `correo_electronico` varchar(26) DEFAULT NULL,
  `grado_actual` varchar(8) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

INSERT INTO `estudiantes` (`id_estudiantes`, `nombre_estudiante`, `apellido_estudiante`, `tipo_de_identificacion`, `numero_de_identificacion`, `edad`, `correo_electronico`, `grado_actual`) VALUES
(1, 'Juan', 'Pérez', 'CC', 1054345678, 16, 'juanperez@gmail.com', 'Décimo'),
(2, 'María', 'Gómez', 'TI', 1054345681, 15, 'mariagomez@gmail.com', 'Noveno'),
(3, 'Pedro', 'López', 'CC', 1054345684, 17, 'pedrolopez@gmail.com', 'Undécimo'),
(4, 'Laura', 'Díaz', 'TI', 1054345687, 14, 'lauradiaz@gmail.com', 'Octavo'),
(5, 'Carlos', 'Martínez', 'CC', 1054345690, 16, 'carlosmartinez@gmail.com', 'Décimo'),
(6, 'Ana', 'Rodríguez', 'TI', 1054345693, 13, 'anarodriguez@gmail.com', 'Séptimo'),
(7, 'Luis', 'González', 'CC', 1054345696, 18, 'luisgonzalez@gmail.com', 'Undécimo'),
(8, 'Carmen', 'Fernández', 'TI', 1054345699, 14, 'carmenfernandez@gmail.com', 'Noveno'),
(9, 'Sergio', 'Sánchez', 'CC', 1054345702, 15, 'sergiosanchez@gmail.com', 'Décimo'),
(10, 'Isabel', 'Torres', 'TI', 1054345705, 17, 'isabeltorres@gmail.com', 'Undécimo'),
(11, 'Diego', 'Ramírez', 'CC', 1054345708, 16, 'diegoramirez@gmail.com', 'Décimo'),
(12, 'Valentina', 'Ruiz', 'TI', 1034567890, 14, 'valentinaruiz@gmail.com', 'Octavo'),
(13, 'David', 'García', 'CC', 1034567893, 17, 'davidgarcia@gmail.com', 'Undécimo'),
(14, 'Sofia', 'López', 'TI', 1034567896, 16, 'sofialopez@gmail.com', 'Décimo'),
(15, 'Martín', 'Pérez', 'CC', 1034567899, 15, 'martinperez@gmail.com', 'Noveno'),
(16, 'Elena', 'Martínez', 'TI', 1034567902, 18, 'elenamartinez@gmail.com', 'Undécimo'),
(17, 'Andrés', 'Rodríguez', 'CC', 1034567905, 14, 'andresrodriguez@gmail.com', 'Octavo'),
(18, 'Lucia', 'González', 'TI', 1034567908, 13, 'luciagonzalez@gmail.com', 'Séptimo'),
(19, 'Marcos', 'Sánchez', 'CC', 1034567911, 16, 'marcossanchez@gmail.com', 'Décimo'),
(20, 'Teresa', 'Díaz', 'TI', 1034567914, 17, 'teresadiaz@gmail.com', 'Undécimo'),
(21, 'Javier', 'López', 'CC', 1034567917, 14, 'javierlopez@gmail.com', 'Noveno'),
(22, 'Paula', 'García', 'TI', 1034567920, 15, 'paulagarcia@gmail.com', 'Décimo'),
(23, 'Sergio', 'Ramírez', 'CC', 1034567923, 16, 'sergioramirez@gmail.com', 'Décimo'),
(24, 'Miguel', 'Rodríguez', 'TI', 1055667889, 18, 'miguelrodriguez@gmail.com', 'Undécimo'),
(25, 'Patricia', 'González', 'CC', 1055667893, 14, 'patriciagonzalez@gmail.com', 'Octavo'),
(26, 'Javier', 'Martínez', 'TI', 1055667897, 16, 'javiermartinez@gmail.com', 'Décimo'),
(27, 'Laura', 'Sánchez', 'CC', 1055667901, 15, 'laurasanchez@gmail.com', 'Noveno'),
(28, 'Juan', 'Ramírez', 'TI', 1055667905, 17, 'juanramirez@gmail.com', 'Undécimo'),
(29, 'Alicia', 'López', 'CC', 1055667909, 16, 'alicialopez@gmail.com', 'Décimo'),
(30, 'Clara', 'García', 'TI', 1055667913, 14, 'claragarcia@gmail.com', 'Octavo'),
(31, 'Pablo', 'Sánchez', 'CC', 1055667917, 13, 'pablolperez@gmail.com', 'Séptimo'),
(32, 'Roberto', 'Ramírez', 'TI', 1055667921, 18, 'robertoramirez@gmail.com', 'Undécimo'),
(33, 'Luis', 'Díaz', 'CC', 1055667925, 14, 'luisdiaz@gmail.com', 'Octavo'),
(34, 'Silvia', 'Pérez', 'TI', 1055667929, 15, 'silviaperez@gmail.com', 'Noveno'),
(35, 'Eva', 'González', 'CC', 1055667933, 16, 'evagonzalez@gmail.com', 'Décimo'),
(36, 'Felipe', 'Rodríguez', 'TI', 1055667937, 17, 'feliperodriguez@gmail.com', 'Undécimo'),
(37, 'Carmen', 'Sánchez', 'CC', 1055667941, 15, 'carmensanchez@gmail.com', 'Noveno'),
(38, 'Laura', 'Ramírez', 'TI', 1055667945, 18, 'lauraramirez@gmail.com', 'Undécimo'),
(39, 'Andrés', 'Pérez', 'CC', 1055667949, 14, 'andresperez@gmail.com', 'Octavo'),
(40, 'Rosa', 'González', 'TI', 1055667953, 16, 'rosagonzalez@gmail.com', 'Décimo'),
(41, 'Alberto', 'Sánchez', 'CC', 1055667957, 17, 'albertsanchez@gmail.com', 'Undécimo'),
(42, 'Juan', 'Rodríguez', 'TI', 1055667961, 16, 'juanrodriguez@gmail.com', 'Décimo'),
(43, 'Patricia', 'Ramírez', 'CC', 1077899020, 13, 'patriciaramirez@gmail.com', 'Séptimo'),
(44, 'Julia', 'González', 'TI', 1077899024, 17, 'juliagonzalez@gmail.com', 'Undécimo'),
(45, 'Luis', 'Sánchez', 'CC', 1077899028, 16, 'luissanchez@gmail.com', 'Décimo'),
(46, 'Alicia', 'Pérez', 'TI', 1077899032, 14, 'aliciaperez@gmail.com', 'Octavo'),
(47, 'Sergio', 'González', 'CC', 1077899036, 18, 'sergiogonzalez@gmail.com', 'Undécimo'),
(48, 'Rosa', 'Ramírez', 'TI', 1077899040, 16, 'rosaramirez@gmail.com', 'Décimo'),
(49, 'Marta', 'Rodríguez', 'CC', 1077899044, 17, 'martarodriguez@gmail.com', 'Undécimo'),
(50, 'Luis', 'Martínez', 'TI', 1077899048, 15, 'luismartinez@gmail.com', 'Noveno'),
(51, 'Juan', 'Ramírez', 'CC', 1077899052, 13, 'juanramirez@gmail.com', 'Séptimo'),
(52, 'Isabel', 'Sánchez', 'TI', 1077899056, 16, 'isabelsanchez@gmail.com', 'Décimo'),
(53, 'Pablo', 'Pérez', 'CC', 1077899060, 17, 'pabloperez@gmail.com', 'Undécimo'),
(54, 'Carlos', 'Ramírez', 'TI', 1077899064, 16, 'carlosramirez@gmail.com', 'Décimo'),
(55, 'Teresa', 'González', 'CC', 1077899068, 14, 'teresagonzalez@gmail.com', 'Octavo'),
(56, 'Marcos', 'Rodríguez', 'TI', 1077899072, 17, 'marcosrodriguez@gmail.com', 'Undécimo'),
(57, 'Javier', 'Pérez', 'CC', 1077899076, 16, 'javierperez@gmail.com', 'Décimo'),
(58, 'Cristina', 'Sánchez', 'TI', 1077899080, 18, 'cristinasanchez@gmail.com', 'Undécimo'),
(59, 'Felipe', 'Ramírez', 'CC', 1077899084, 14, 'feliperamirez@gmail.com', 'Octavo');

DROP TABLE IF EXISTS `eventos`;
CREATE TABLE IF NOT EXISTS `eventos` (
  `id_evento` int DEFAULT NULL,
  `titulo` varchar(16) DEFAULT NULL,
  `descripcion` varchar(19) DEFAULT NULL,
  `fecha_inicio` varchar(9) DEFAULT NULL,
  `fecha_fin` varchar(9) DEFAULT NULL,
  `id_proyecto` int DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

INSERT INTO `eventos` (`id_evento`, `titulo`, `descripcion`, `fecha_inicio`, `fecha_fin`, `id_proyecto`) VALUES
(1, 'festival', 'evento de disfraces', '3/04/2025', '8/04/2025', 1),
(2, 'isada de bandera', 'dia de la raza', '4/04/2025', '4/04/2025', 4);

DROP TABLE IF EXISTS `proyectos`;
CREATE TABLE IF NOT EXISTS `proyectos` (
  `id_proyecto` int DEFAULT NULL,
  `titulo` varchar(19) DEFAULT NULL,
  `descripcion` varchar(18) DEFAULT NULL,
  `fecha_inicio` varchar(10) DEFAULT NULL,
  `fecha_limite` varchar(10) DEFAULT NULL,
  `id_docente` int DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

INSERT INTO `proyectos` (`id_proyecto`, `titulo`, `descripcion`, `fecha_inicio`, `fecha_limite`, `id_docente`) VALUES
(1, 'proyecto de grado_1', 'asignatura español', '15/04/2025', '22/04/2025', 2);

DROP TABLE IF EXISTS `tareas`;
CREATE TABLE IF NOT EXISTS `tareas` (
  `id_tarea` int DEFAULT NULL,
  `titulo` varchar(18) DEFAULT NULL,
  `descripcion` varchar(22) DEFAULT NULL,
  `fecha_limite` varchar(10) DEFAULT NULL,
  `id_proyecto` int DEFAULT NULL,
  `id_asignatura` int DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

INSERT INTO `tareas` (`id_tarea`, `titulo`, `descripcion`, `fecha_limite`, `id_proyecto`, `id_asignatura`) VALUES
(1, 'Ensayo_de_biologia', 'Seres vivos', '12/04/2025', 2, 6),
(2, 'Ensayo_de_quimica', 'Reacciones moleculares', '15/04/2025', 3, 7);

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int DEFAULT NULL,
  `nombre` varchar(4) DEFAULT NULL,
  `apellido` varchar(5) DEFAULT NULL,
  `correo_electronico` varchar(20) DEFAULT NULL,
  `tipo_usuario` varchar(10) DEFAULT NULL,
  `identificación` int DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

INSERT INTO `usuarios` (`id_usuario`, `nombre`, `apellido`, `correo_electronico`, `tipo_usuario`, `identificación`) VALUES
(1, 'Juan', 'Perez', 'juan.perez@gmail.com', 'estudiante', 1054345678);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
