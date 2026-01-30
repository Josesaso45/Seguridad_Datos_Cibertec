# Medidas de Seguridad contra SQL Injection
## SaludPlus Online - Recomendaciones

---

## 🔐 Introducción

La vulnerabilidad de **SQL Injection** es una de las más críticas según OWASP (A1/A03 dependiendo del año). Para SaludPlus Online, que maneja **datos médicos sensibles** y **transacciones farmacéuticas**, es crítico implementar defensas robustas.

---

## 🛡️ Medidas de Seguridad Principales

### 1. **Consultas Preparadas (Prepared Statements)**

**⭐ La defensa MÁS EFECTIVA contra SQL Injection**

#### ❌ Código Vulnerable (NO USAR):
```php
<?php
$user_id = $_GET['id'];
$query = "SELECT * FROM users WHERE id = '$user_id'";
$result = mysqli_query($conn, $query);
?>
```

#### ✅ Código Seguro (USAR):
```php
<?php
$user_id = $_GET['id'];
$stmt = $conn->prepare("SELECT * FROM users WHERE id = ?");
$stmt->bind_param("i", $user_id);
$stmt->execute();
$result = $stmt->get_result();
?>
```

**Ventajas:**
- Los parámetros se tratan como **datos**, no como **código SQL**
- El motor de BD separa la lógica de la query de los datos
- Protección automática contra inyección

---

### 2. **Validación y Sanitización de Entradas**

#### Validación Estricta por Tipo de Dato:

```php
// Para IDs numéricos
$user_id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($user_id === false || $user_id < 1) {
    die("ID inválido");
}

// Para emails
$email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
if (!$email) {
    die("Email inválido");
}

// Para DNI (8 dígitos)
$dni = $_POST['dni'];
if (!preg_match('/^[0-9]{8}$/', $dni)) {
    die("DNI inválido");
}
```

#### Whitelist de Valores Permitidos:

```php
// Para seleccionar especialidades médicas
$especialidades_validas = ['medicina_general', 'pediatria', 'cardiologia', 'dermatologia'];
$especialidad = $_POST['especialidad'];

if (!in_array($especialidad, $especialidades_validas)) {
    die("Especialidad no válida");
}
```

---

### 3. **Principio de Mínimo Privilegio en la BD**

#### ❌ Usuario con privilegios excesivos:
```sql
-- NO USAR: Usuario 'root' con acceso total
GRANT ALL PRIVILEGES ON *.* TO 'webapp'@'localhost';
```

#### ✅ Usuario con permisos limitados:
```sql
-- USAR: Usuario con permisos específicos
CREATE USER 'saludplus_app'@'localhost' IDENTIFIED BY 'password_seguro_123';

-- Solo permisos necesarios
GRANT SELECT, INSERT, UPDATE ON saludplus_db.citas TO 'saludplus_app'@'localhost';
GRANT SELECT ON saludplus_db.productos TO 'saludplus_app'@'localhost';

-- NO otorgar permisos de DROP, ALTER, CREATE
FLUSH PRIVILEGES;
```

**Beneficios:**
- Si hay inyección SQL, el atacante no podrá borrar tablas (DROP)
- No podrá modificar la estructura de la BD (ALTER)
- Reduce el impacto del ataque

---

### 4. **Escapado de Caracteres Especiales**

**⚠️ Método secundario, NO debe ser la única defensa**

```php
// Escapar entrada (solo como capa adicional)
$nombre = mysqli_real_escape_string($conn, $_POST['nombre']);

// PERO SIEMPRE usar Prepared Statements como defensa principal
$stmt = $conn->prepare("INSERT INTO pacientes (nombre) VALUES (?)");
$stmt->bind_param("s", $nombre);
$stmt->execute();
```

---

### 5. **ORM (Object-Relational Mapping)**

Usar frameworks que automatizan la protección:

#### Laravel (PHP):
```php
// Protección automática contra SQL Injection
$citas = DB::table('citas')
    ->where('paciente_id', $id)
    ->get();
```

#### Django (Python):
```python
# QuerySet con protección integrada
citas = Cita.objects.filter(paciente_id=id)
```

#### Sequelize (Node.js):
```javascript
// Prepared statements automáticos
const citas = await Cita.findAll({
    where: { paciente_id: id }
});
```

---

## 🔍 Medidas de Detección y Monitoreo

### 6. **Web Application Firewall (WAF)**

Implementar un WAF que detecte patrones de SQL Injection:

**Patrones a bloquear:**
- `' OR '1'='1`
- `UNION SELECT`
- `DROP TABLE`
- `; DELETE FROM`
- `SUBSTRING(`, `ASCII(`, `CONCAT(`

**Soluciones recomendadas:**
- **ModSecurity** (open source)
- **Cloudflare WAF**
- **AWS WAF**
- **Azure WAF**

---

### 7. **Logging y Auditoría**

```php
// Registrar intentos sospechosos
function log_sql_attempt($input, $ip) {
    $suspicious_patterns = ["'", "UNION", "SELECT", "DROP", "--", "/*"];
    
    foreach ($suspicious_patterns as $pattern) {
        if (stripos($input, $pattern) !== false) {
            // Registrar en archivo de log
            error_log("[SQL INJECTION ATTEMPT] IP: $ip | Input: $input");
            
            // Notificar al equipo de seguridad
            mail('security@saludplus.com', 'SQL Injection Attempt', 
                 "IP: $ip intentó: $input");
            
            // Bloquear IP temporalmente
            return false;
        }
    }
    return true;
}
```

---

### 8. **Rate Limiting**

Limitar intentos de consulta desde la misma IP:

```php
// Implementar límite de 50 consultas por minuto
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$ip = $_SERVER['REMOTE_ADDR'];
$key = "rate_limit:$ip";

$requests = $redis->incr($key);
if ($requests === 1) {
    $redis->expire($key, 60); // Expira en 60 segundos
}

if ($requests > 50) {
    http_response_code(429); // Too Many Requests
    die("Demasiadas solicitudes. Intente más tarde.");
}
```

---

## 🧪 Medidas de Prueba y Validación

### 9. **Testing de Seguridad Automatizado**

#### Herramientas recomendadas:

1. **SQLMap** - Testing manual de SQL Injection:
```bash
sqlmap -u "http://saludplus.com/citas.php?id=1" --batch --risk=3
```

2. **OWASP ZAP** - Escaneo automatizado:
   - Ejecutar Active Scan
   - Revisar alertas de nivel High/Medium

3. **Burp Suite** - Interceptar y modificar peticiones:
   - Usar Intruder para fuzzing
   - Revisar respuestas anormales

---

### 10. **Code Review y Análisis Estático**

#### Herramientas:

- **SonarQube**: Detecta código vulnerable
- **PHPStan**: Análisis estático para PHP
- **Bandit**: Para aplicaciones Python
- **ESLint Security**: Para Node.js

```bash
# Ejemplo con SonarQube
sonar-scanner \
  -Dsonar.projectKey=saludplus \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000
```

---

## 📊 Tabla Resumen de Medidas

| # | Medida | Prioridad | Dificultad | Efectividad |
|---|--------|-----------|------------|-------------|
| 1 | Prepared Statements | 🔴 CRÍTICA | Baja | ⭐⭐⭐⭐⭐ |
| 2 | Validación de Entradas | 🔴 CRÍTICA | Media | ⭐⭐⭐⭐ |
| 3 | Mínimo Privilegio BD | 🟠 Alta | Baja | ⭐⭐⭐⭐ |
| 4 | Escapado de Caracteres | 🟡 Media | Baja | ⭐⭐⭐ |
| 5 | ORM Framework | 🟠 Alta | Media | ⭐⭐⭐⭐⭐ |
| 6 | WAF | 🟠 Alta | Media-Alta | ⭐⭐⭐⭐ |
| 7 | Logging/Auditoría | 🟡 Media | Media | ⭐⭐⭐ |
| 8 | Rate Limiting | 🟡 Media | Media | ⭐⭐⭐ |
| 9 | Testing Automatizado | 🟠 Alta | Media | ⭐⭐⭐⭐ |
| 10 | Code Review | 🟡 Media | Alta | ⭐⭐⭐⭐ |

---

## 🎯 Plan de Implementación para SaludPlus Online

### Fase 1 - Inmediata (0-2 semanas):
- ✅ Implementar Prepared Statements en TODOS los módulos
- ✅ Validación estricta de entradas
- ✅ Crear usuario de BD con permisos mínimos

### Fase 2 - Corto Plazo (1 mes):
- ✅ Implementar WAF (ModSecurity o Cloudflare)
- ✅ Sistema de logging y alertas
- ✅ Rate limiting en endpoints críticos

### Fase 3 - Mediano Plazo (2-3 meses):
- ✅ Migrar a framework con ORM
- ✅ Testing automatizado en CI/CD
- ✅ Auditoría de seguridad completa

---

## 📚 Referencias y Recursos

### Documentación Oficial:
- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [CWE-89: SQL Injection](https://cwe.mitre.org/data/definitions/89.html)
- [PHP Manual: Prepared Statements](https://www.php.net/manual/es/mysqli.quickstart.prepared-statements.php)

### Herramientas:
- [SQLMap](https://sqlmap.org/)
- [OWASP ZAP](https://www.zaproxy.org/)
- [ModSecurity](https://modsecurity.org/)
- [SonarQube](https://www.sonarqube.org/)

---

## ✅ Checklist de Seguridad

Antes de pasar a producción, verificar:

- [ ] Todos los queries usan Prepared Statements
- [ ] Validación de entrada implementada en todos los formularios
- [ ] Usuario de BD con permisos limitados
- [ ] WAF configurado y activo
- [ ] Sistema de logging funcionando
- [ ] Rate limiting implementado
- [ ] Testing de seguridad realizado (SQLMap + OWASP ZAP)
- [ ] Code review completado
- [ ] Documentación de seguridad actualizada
- [ ] Equipo capacitado en buenas prácticas

---

## 🎓 Conclusión

Para **SaludPlus Online**, la protección contra SQL Injection es **CRÍTICA** debido a:

1. **Datos sensibles:** Información médica protegida por ley (HIPAA, Ley de Protección de Datos Personales en Perú)
2. **Transacciones económicas:** Pagos de productos farmacéuticos
3. **Reputación:** Una brecha de seguridad destruiría la confianza de los pacientes

**La combinación de Prepared Statements + Validación + Mínimo Privilegio** proporciona una defensa sólida con **~99% de efectividad** contra ataques de SQL Injection.

---

**Autor:** José Montero Vilcas  
**Curso:** 2414 - Seguridad de Aplicaciones  
**Fecha:** 29 de enero de 2026
