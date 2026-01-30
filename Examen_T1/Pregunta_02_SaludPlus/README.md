# Pregunta 02 - SaludPlus Online
## OWASP A1: SQL Injection Blind

### Contexto del Ejercicio

**Empresa:** SaludPlus Online  
**Descripción:** Plataforma dedicada a la gestión de citas médicas y venta de productos farmacéuticos vía web.

**Objetivo de la auditoría:**  
Evaluar la seguridad de la plataforma utilizando DVWA (Damn Vulnerable Web Application) antes de pasar a producción.

---

## 📋 Estructura del Proyecto

```
Pregunta_02_SaludPlus/
├── index.html          # Página principal de SaludPlus Online
├── citas.html          # Formulario de agendamiento de citas
├── farmacia.html       # Catálogo de productos farmacéuticos
├── perfil.html         # Perfil del usuario
├── styles.css          # Estilos CSS del sitio
├── README.md           # Este archivo
├── SQL_INJECTION_BLIND.md    # Guía del ataque SQL Injection Blind
└── MEDIDAS_SEGURIDAD.md      # Medidas de seguridad recomendadas
```

---

## 🌐 Cómo Abrir la Página Web

1. **Opción 1 - Doble clic:**
   - Navega a la carpeta `Pregunta_02_SaludPlus`
   - Doble clic en `index.html`
   - Se abrirá en tu navegador predeterminado

2. **Opción 2 - Desde Visual Studio Code:**
   - Abre la carpeta en VS Code
   - Click derecho en `index.html`
   - Selecciona "Open with Live Server" (si tienes la extensión instalada)

3. **Opción 3 - Navegador directo:**
   - Abre tu navegador
   - Presiona `Ctrl + O`
   - Selecciona el archivo `index.html`

---

## 🎯 Objetivo de la Pregunta 02

Según la rúbrica (7 puntos):

### Excelente (7 puntos):
✅ **Evidenciar el nombre de la base de datos**  
✅ **Evidenciar el usuario conectado al servidor**  
✅ **Brindar medidas de seguridad**

### Bueno (4 puntos):
- Evidencia el nombre de la base de datos y/o usuario conectado

### Regular (2 puntos):
- Logra determinar cuál es el parámetro vulnerable

---

## 🔧 Configuración Requerida

### DVWA (Damn Vulnerable Web Application)

1. **Instalar DVWA:**
   - Puede ser mediante XAMPP, Docker, o una VM con DVWA preinstalado

2. **Configuración:**
   - Nivel de seguridad: **Medium**
   - Módulo: **SQL Injection (Blind)**

3. **Acceso:**
   - URL típica: `http://localhost/dvwa/vulnerabilities/sqli_blind/`
   - Usuario por defecto: `admin`
   - Contraseña: `password`

---

## 📝 Pasos para Realizar el Ejercicio

### Fase 1: Preparación (Ya completada ✅)
- [x] Crear página web de SaludPlus Online
- [x] Documentar estructura del proyecto

### Fase 2: Explotación SQL Injection Blind
Ver archivo: **`SQL_INJECTION_BLIND.md`**

### Fase 3: Documentar Medidas de Seguridad
Ver archivo: **`MEDIDAS_SEGURIDAD.md`**

---

## 📸 Capturas Requeridas

Para obtener 7 puntos, debes capturar pantalla completa de:

1. ✅ **Página web de SaludPlus Online funcionando**
2. ⏳ **DVWA configurado en nivel Medium**
3. ⏳ **Identificación del parámetro vulnerable**
4. ⏳ **Extracción del nombre de la base de datos**
5. ⏳ **Extracción del usuario conectado**
6. ⏳ **Documento con medidas de seguridad**

---

## 🔐 Vulnerabilidad: SQL Injection Blind

**Tipo:** OWASP A1 - Injection  
**Nivel:** Medium  
**Módulo DVWA:** SQL Injection (Blind)

**Descripción:**  
En SQL Injection Blind, el atacante no recibe mensajes de error directos de la base de datos, pero puede inferir información basándose en diferencias en las respuestas del servidor (tiempo de respuesta, contenido diferente, etc.).

---

## 📚 Archivos Complementarios

- **`SQL_INJECTION_BLIND.md`**: Guía paso a paso del ataque
- **`MEDIDAS_SEGURIDAD.md`**: Recomendaciones de seguridad para prevenir SQL Injection

---

## ⚠️ Disclaimer

Este proyecto es **únicamente con fines educativos** para la asignatura de Seguridad de Aplicaciones en CIBERTEC. 

**NO utilizar estas técnicas en sistemas de producción o sin autorización explícita.**

---

## 👨‍🎓 Información del Estudiante

**Alumno:** José Montero Vilcas  
**Curso:** 2414 - Seguridad de Aplicaciones  
**Profesor:** Wilman Vasquez  
**Fecha:** 29 de enero de 2026  
**Sección:** T5HO - Grupo 01
