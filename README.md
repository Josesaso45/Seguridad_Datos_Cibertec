# 🛡️ Seguridad de Aplicaciones - CIBERTEC

Este repositorio contiene los ejercicios, prácticas y evaluaciones del curso de **Seguridad de Aplicaciones** (Carrera de Computación e Informática). El objetivo principal es documentar el aprendizaje sobre vulnerabilidades web, herramientas de auditoría y mecanismos de defensa.

---

## 📁 Estructura del Proyecto

El repositorio está organizado por semanas y evaluaciones:

### 📑 [Examen T1](./Examen_T1/)
Contiene la resolución de la Primera Evaluación T1.
*   **[Pregunta 02 - SaludPlus Online](./Examen_T1/Pregunta_02_SaludPlus/)**: Caso de estudio sobre **SQL Injection Blind**.
    *   Simulación de una plataforma médica.
    *   Guía de explotación en DVWA (Nivel Medium).
    *   Medidas de mitigación (Prepared Statements, Validación, Mínimo Privilegio).
*   **[Pregunta 03 - NovaMarket](./Examen_T1/Pregunta_03_NovaMarket/)**: Caso sobre **Exposición de Datos Sensibles (HTTP vs HTTPS)**.
    *   Página de retail simulada.
    *   Análisis de riesgos por falta de cifrado.
    *   Implementación de SSL/TLS, HSTS y Cookies Seguras.

### 📅 [Semana 02](./Semana_02/)
Introducción a metodologías y herramientas OWASP.
*   **Análisis Estático y Dinámico:** Ejercicios básicos de búsqueda y scripts.
*   **Herramientas OWASP:** Exploración de herramientas para auditoría.
*   **Login OWASP:** Ejemplo de validación de credenciales básica.

### 📅 [Semana 03](./Semana_03/)
Profundización en inyecciones y autenticación.
*   **Inyección SQL:** Scripts `.sql` para entender la manipulación de consultas.
*   **Autenticación LDAP:** Ejemplos de login simulado y conexión LDAP con Node.js.

---

## 🚀 Conceptos Clave Aprendidos

### 1. OWASP Top 10
*   **A1: Inyección:** Especialmente SQL Injection (Normal y Blind). Aprendimos que el uso de *Prepared Statements* es la defensa número uno.
*   **A3: Exposición de Datos Sensibles:** La importancia de cifrar la comunicación mediante HTTPS para evitar ataques de *Sniffing*.

### 2. Herramientas de Auditoría
*   **DVWA (Damn Vulnerable Web Application):** Entorno de pruebas para practicar ataques en un ambiente controlado.
*   **Burp Suite / OWASP ZAP:** Herramientas para interceptar y analizar tráfico HTTP.
*   **SQLMap:** Automatización de pruebas de inyección SQL.

### 3. Mecanismos de Defensa
*   **Cifrado:** Implementación de certificados SSL/TLS.
*   **Sanitización:** Validación estricta de entradas del usuario.
*   **WAF (Web Application Firewall):** Capa de protección externa para filtrar tráfico malicioso.

---

## 🛠️ Cómo usar este repositorio para practicar

1.  **Para SQL Injection:**
    *   Levanta un contenedor Docker con DVWA: `docker run --rm -it -p 80:80 vulnerables/web-dvwa`.
    *   Sigue los pasos en [SQL_INJECTION_BLIND.md](./Examen_T1/Pregunta_02_SaludPlus/SQL_INJECTION_BLIND.md).
2.  **Para Análisis de Tráfico:**
    *   Abre el archivo `index.html` de NovaMarket.
    *   Observa la advertencia de "No es seguro" y analiza cómo viajan los datos en el formulario de login.
3.  **Para Node.js:**
    *   Revisa los archivos en `Semana_03` para entender cómo se manejan las sesiones y autenticaciones.

---

## 👨‍🎓 Información del Estudiante
*   **Alumno:** José Montero Vilcas
*   **Institución:** CIBERTEC
*   **Ciclo:** Quinto
*   **Profesor:** Wilman Vasquez

---

> *"La seguridad no es un producto, es un proceso."*
