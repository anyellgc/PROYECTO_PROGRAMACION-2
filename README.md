
APLICACIÓN WEB DE SISTEMA DE GESTION DE TAREAS Y PROYECTOS ESCOLARES.


1.Descripción del Proyecto: Sistema de Gestión de Tareas y Proyectos Escolares

Este proyecto consiste en el desarrollo de un sistema web integral diseñado para optimizar la gestión de tareas y proyectos en un entorno escolar como lo es para el colegio (I.E .EL CHARCO) del cual me gradue de once y el cual esta ubicacdo en el campo, pensando en darle solución en este caso a una problematica en la cual ellos no cuentan actualmente con una aplicación que pueda gestionar los proyectos y las tareas para mejorar sus conocimientos y que sean participes de algo innovador y diferente. El sistema busca mejorar la comunicación y la colaboración entre estudiantes, profesores y administradores, facilitando la organización de actividades académicas y extracurriculares.

2.Definicion modulos del sistema:

Módulos Principales:

1.Autenticación y Gestión de Usuarios:
Este módulo proporciona un acceso seguro al sistema, permitiendo a los usuarios registrarse, iniciar sesión y gestionar sus perfiles.
Se implementará un sistema de roles y permisos para controlar el acceso a diferentes funcionalidades según el tipo de usuario (estudiante, profesor y administrador).

2.Procesamiento de Datos:
Este módulo se encarga de la lógica de negocio del sistema, gestionando la creación, modificación y eliminación de tareas, proyectos, eventos y calificaciones.
Se implementarán funcionalidades para asignar tareas, calcular calificaciones, generar informes y gestionar la información académica de los estudiantes.

3.Interfaz de Usuario:
Este módulo proporciona una interfaz intuitiva y fácil de usar para que los usuarios interactúen con el sistema.
Se diseñarán vistas para mostrar tareas, proyectos, calendarios, calificaciones y mensajes, facilitando la navegación y el acceso a la información.

Modulos Secundarios:
4.Módulo de Calendario y Eventos:

Proporciona un calendario interactivo que muestra fechas importantes (exámenes, entregas, eventos escolares).
Permite a los usuarios crear y gestionar eventos personales o grupales.
Envía recordatorios automáticos de eventos próximos.

5.Módulo de Calificaciones:

Permite a los profesores registrar y gestionar las calificaciones de los estudiantes.
Proporciona a los estudiantes acceso a las calificaciones y al progreso académico.

6.Módulo de Gestión de Recursos:

Permite a los profesores compartir materiales de estudio, documentos y otros recursos con los estudiantes.
Organiza los recursos por materia, grado o proyecto.

7.Módulo de Informes y Estadísticas:

Genera informes sobre el progreso de los estudiantes, el rendimiento de los profesores y otras métricas relevantes.
Proporciona estadísticas sobre la asistencia y participacion en las tareas dando un porcentaje a los proyectos de los estudiantes como ayuda en sus notas.


Objetivos del Proyecto:

1.Mejorar la organización y la productividad de estudiantes y profesores.
2.Facilitar la comunicación y la colaboración en el entorno escolar.
3.Proporcionar una herramienta centralizada para la gestión de tareas, proyectos y eventos.
4.Mejorar el seguimiento del progreso académico de los estudiantes.
5.Crear algo bonito, intuitivo, y llamativo para el colegio que sea util.

Tecnologías:

1.El proyecto se desarrollará utilizando el lenguaje de programación Python en el IDE Visual Code Studio.
2.Se utilizará Django como framework donde se va a integrar a HTML, CSS y JavaScript mediante un sistema de plantillas que contiene Django que los permite mezclar para tener una logica de presentación y mejorar la funcionalidad y el diseño del sistema web.
3. La base de datos sera creada desde cero, para este sistema se implementara la base de datos usando MySQL desde un servicio en la nube como Google Cloud SQL y sera hecha desde MySQL Workbench como un entorno local antes de desplegar la base de datos a la nube.


Flujo del Sistema:

1.Autenticación:
 -El usuario ingresa sus credenciales.
 -Verificación  de las credenciales del usuario (estudiante, docente).

2.Gestión de Tareas y Proyectos:
 -Los profesores crean tareas/proyectos a través de la interfaz.
 -Los estudiantes ver las tareas/proyectos en la interfaz.
 -Los estudiantes marcan tareas como completadas y suben entregas.
 -Los profesores pueden subir guias de ayuda.

3.Gestión de Calificaciones:
 -Los profesores agregan calificaciones a través de la interfaz.
 -Los profesores podran hacer la retroalimentacion sobre las tareas.
 -Los estudiantes pueden recibir comentarios en sus entregas.
 -Actualizar las calificaciones en la base de datos.
 -Los estudiantes pueden ver las calificaciones.
 
4.Calendario y Eventos:
 -El sistema muestra un calendario con eventos.
 -El sistema puede notificar una alerta de un evento proximo.

5.Informes y Estadísticas:
 -Los informes se pueden mostrar en la interfaz.
 -Los eventos se pueden mostrar en la interfaz.
 
6.Roles y Permisos:
 -Permiso del administrador para dar acceso a recursos el administrador va a tener el rol de docente.
 -Registro de los estudiantes y acceso del docente para ingresar al curso.
