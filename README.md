# PROYECTO - PROGRAMACIÓN II

Este repositorio contiene todo lo relacionado con el desarrollo del proyecto para la asignatura de Programación II.

## Aplicación Web de Sistema de Gestión de Tareas y Proyectos Escolares

### Breve Descripción del Problema que Resuelve

El colegio **I.E. El Charco**, ubicado en zona rural y del cual **somos egresados**, actualmente no cuenta con una aplicación que facilite la gestión de tareas y proyectos académicos. Esto limita la organización, la participación y la innovación educativa.

Nuestro proyecto busca solucionar esta necesidad mediante una plataforma web que permita:

- Gestionar tareas, proyectos y eventos escolares de forma eficiente.
- Mejorar la comunicación y colaboración entre estudiantes y docentes.
- Facilitar el acceso a recursos académicos y el seguimiento del rendimiento escolar.

---

## Integrantes del Equipo

- Johán Nicolás Bautista Raba
- Anyell Mariana Gómez Castillo

---

## Lista Inicial de Módulos del Sistema

### 1. Autenticación y Gestión de Usuarios

- Registro e inicio de sesión de usuarios (estudiantes, docentes y administradores).
- Gestión segura de perfiles y control de accesos mediante roles y permisos.

### 2. Procesamiento de Datos

- Gestión de tareas, proyectos, eventos y calificaciones.
- Asignación de tareas, cálculo de notas y generación de informes académicos.

### 3. Interfaz de Usuario

- Diseño de una interfaz intuitiva que permita visualizar tareas, proyectos, calendarios, calificaciones y mensajes.

### 4. Calendario y Eventos

- Calendario interactivo para visualizar fechas importantes.
- Creación de eventos personales o grupales.
- Recordatorios automáticos de eventos próximos.

### 5. Módulo de Calificaciones

- Registro y gestión de calificaciones por parte de los docentes.
- Visualización de calificaciones y progreso académico por los estudiantes.

### 6. Gestión de Recursos

- Compartición de documentos, guías y materiales de estudio organizados por materia, grado o proyecto.

### 7. Informes y Estadísticas

- Generación de informes sobre el rendimiento académico.
- Estadísticas de participación en proyectos y tareas.
- Cálculo de porcentajes de participación como apoyo en la evaluación.

### 8. Chatbot Asistente Escolar

#### ¿Qué papel cumple el chatbot en el sistema?

El chatbot se integra como un **asistente virtual básico** dentro de la plataforma, cumpliendo las siguientes funciones:

- **Guía a estudiantes y profesores**:
  - Responde preguntas típicas como:
    - "¿Dónde veo mis tareas?"
    - "¿Dónde están mis calificaciones?"
    - "¿Qué eventos hay?"
  - Facilita la navegación para usuarios que no estén familiarizados con el sistema.

- **Mejora la experiencia del usuario**:
  - Aporta interactividad y moderniza la plataforma.

- **Ahorra tiempo a los docentes**:
  - Responde automáticamente a preguntas frecuentes para que los docentes puedan enfocarse en sus actividades de enseñanza.

- **Prepara el sistema para futuras mejoras**:
  - Inicialmente ofrece respuestas fijas, pero a futuro podrá conectarse a la base de datos para consultas dinámicas (por ejemplo, buscar tareas pendientes o eventos próximos).

| Función | ¿Qué hace el chatbot? |
|:--------|:----------------------|
| Atención Básica | Responde preguntas frecuentes |
| Guía de Navegación | Indica dónde ver tareas, notas y proyectos |
| Innovación | Hace la plataforma escolar más atractiva |
| Base para Mejoras | Puede evolucionar a consultas dinámicas |

---

## Tecnologías a Utilizar

### Backend y Base de Datos

- **Python** con **Django** para el desarrollo del backend.
- **MySQL** como sistema de gestión de base de datos:
  - Diseño inicial en entorno local con **MySQL Workbench**.
  - Implementación en la nube utilizando **Google Cloud SQL**.

### Frontend

- **HTML**, **CSS** y **JavaScript** utilizando el sistema de plantillas de Django para una integración fluida entre lógica y presentación.

### Entornos de Desarrollo

- **Visual Studio Code** como IDE principal de trabajo.

### Chatbot

- Chatbot web básico desarrollado en **JavaScript** e integrado mediante las plantillas de Django.

---

## Flujo del Sistema

### Inicio y Autenticación

- El usuario accede al sistema mediante su nombre de usuario y contraseña.
- Se verifica el tipo de usuario (estudiante, docente o administrador).

### Gestión de Tareas y Proyectos

- Los docentes crean tareas y proyectos desde la plataforma.
- Los estudiantes visualizan y gestionan sus tareas y proyectos asignados.
- Los estudiantes pueden marcar tareas como completadas y cargar entregas.
- Los docentes tienen la posibilidad de subir guías de apoyo.

### Gestión de Calificaciones

- Los docentes registran y actualizan las calificaciones de los estudiantes.
- Se permite la retroalimentación personalizada sobre las entregas.
- Los estudiantes consultan sus calificaciones en tiempo real.

### Calendario y Eventos

- El sistema presenta un calendario interactivo.
- Se generan alertas de eventos y recordatorios automáticos.

### Informes y Estadísticas

- Se muestran informes de rendimiento académico.
- Se calculan estadísticas de participación en actividades escolares.

### Chatbot Escolar

- El chatbot guía a los usuarios para encontrar la información de manera rápida.
- Se planea su evolución hacia un chatbot conectado a la base de datos.

### Roles y Permisos

- El administrador, que también cumple el rol de docente, gestiona el acceso de los usuarios y la asignación de recursos.

---

## Cronograma de Actividades

- [ ] Organización de módulos en Notion.
- [ ] Configuración del entorno de desarrollo (Django + MySQL).
- [ ] Creación de la base de datos local y despliegue en Google Cloud SQL.
- [ ] Desarrollo de módulos principales (autenticación, tareas, proyectos).
- [ ] Implementación del calendario y gestión de eventos.
- [ ] Desarrollo del módulo de informes y estadísticas.
- [ ] Creación e integración del chatbot asistente.
- [ ] Pruebas de usuario y ajustes finales.

---
