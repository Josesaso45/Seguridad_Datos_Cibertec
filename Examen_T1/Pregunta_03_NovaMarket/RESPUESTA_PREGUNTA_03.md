# RESPUESTA PREGUNTA 03 - OWASP A3: EXPOSICIÓN DE DATOS SENSIBLES
## Alumno: José Montero Vilcas | Curso: Seguridad de Aplicaciones

---

## 🎯 RESUMEN DEL CASO

**Empresa:** NovaMarket (Retail)  
**Sitio Web:** `RetailNova.com` (Simulado)  
**Vulnerabilidad:** OWASP A3: Exposición de Datos Sensibles / Fallos Criptográficos  
**Problema detectado:** El sitio opera bajo el protocolo **HTTP**, lo que implica una capa de transporte insegura sin cifrado.

---

## 1️⃣ EVIDENCIA DE LA VULNERABILIDAD

### Análisis del Sitio Web
El portal de **NovaMarket** (RetailNova) permite a los usuarios navegar por productos e iniciar sesión para realizar compras. Sin embargo, al observar la barra de direcciones del navegador:

- **Protocolo:** `http://` (en lugar de `https://`)
- **Estado:** "No es seguro" o "Inseguro" en el navegador.

### Evidencia de Información Sensible en Riesgo
Al utilizar el protocolo HTTP, toda la información que viaja entre el cliente y el servidor lo hace en **texto plano**. Esto incluye:

1. **Credenciales de Acceso:** El usuario y la contraseña enviados en el formulario de `login.html`.
2. **Datos Personales:** Nombres, direcciones y correos electrónicos de los clientes.
3. **Información de Pago:** Si el usuario ingresa una tarjeta de crédito, los números y el CVV pueden ser interceptados mediante ataques de **Sniffing** (como Man-in-the-Middle).

---

## 2️⃣ MEJORAS DE SEGURIDAD (3 Recomendaciones)

### 🛡️ Mejora 1: Implementación de Certificado SSL/TLS (HTTPS)
La medida más crítica es migrar el sitio de HTTP a **HTTPS**.
- **Acción:** Adquirir e instalar un certificado SSL/TLS (puede ser gratuito mediante *Let's Encrypt*).
- **Resultado:** Se cifra el canal de comunicación, asegurando que los datos viajen de forma privada e íntegra.

### 🛡️ Mejora 2: Configuración de HSTS (HTTP Strict Transport Security)
Una vez implementado HTTPS, se debe forzar a que el navegador solo use conexiones seguras.
- **Acción:** Añadir la cabecera de respuesta `Strict-Transport-Security`.
- **Resultado:** Evita ataques de degradación de protocolo (SSL Stripping) al prohibir que el navegador cargue el sitio vía HTTP.

### 🛡️ Mejora 3: Uso de Atributos de Cookies Seguras
Asegurar que las cookies de sesión no sean robadas.
- **Acción:** Configurar las cookies con los atributos `Secure` y `HttpOnly`.
- **Resultado:** 
    - `Secure`: Garantiza que la cookie solo se envíe sobre HTTPS.
    - `HttpOnly`: Evita que scripts maliciosos (XSS) accedan a la cookie de sesión.

---

## 📊 COMPARATIVA DE SEGURIDAD

| Característica | Estado Actual (HTTP) | Estado Deseado (HTTPS) |
|----------------|----------------------|------------------------|
| **Cifrado** | Ninguno (Texto plano) | Cifrado (AES-256) |
| **Integridad** | Vulnerable a cambios | Protegida |
| **Confianza** | "Sitio no seguro" | Candado verde / Seguro |
| **Protección Sniffing** | Nula | Alta |

---

## 📸 CAPTURAS NECESARIAS PARA 6 PUNTOS (Sugeridas)

1. ✅ **Captura de la página NovaMarket (RetailNova)** mostrando el mensaje de "No es seguro" en la URL.
2. ✅ **Captura del formulario de Login** evidenciando que los datos se envían por una ruta insegura.
3. ✅ **Simulación de Sniffing (opcional):** Captura de Wireshark o F12 (Network) mostrando la contraseña en texto plano al hacer clic en Ingresar.

---

## 🎯 RÚBRICA - AUTOEVALUACIÓN

### ✅ EXCELENTE (6 puntos):
- [x] Logra encontrar/crear la página web (**RetailNova**).
- [x] Evidencia de la información sensible (Explicación del riesgo en HTTP).
- [x] Brinda 3 mejoras de seguridad (SSL, HSTS, Cookies Seguras).

---

**Fecha:** 29 de enero de 2026  
**Curso:** 2414 - Seguridad de Aplicaciones  
**Profesor:** Wilman Vasquez  
**Sección:** T5HO - Grupo 01
