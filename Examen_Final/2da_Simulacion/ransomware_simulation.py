"""
=============================================================================
SIMULACIÓN EDUCATIVA DE RANSOMWARE — CASO COLONIAL PIPELINE / DARKSIDE (2021)
=============================================================================

Este script simula el flujo de un ataque de ransomware tipo DarkSide con fines
puramente educativos. NO contiene código malicioso real.

    - El "cifrado" se realiza con Base64 (completamente reversible).
    - Solo opera sobre un directorio local de prueba creado dinámicamente.
    - Ilustra la pérdida de los pilares de la Tríada CIA.

TRÍADA CIA — Impacto del Ransomware:
    
    CONFIDENCIALIDAD: El grupo DarkSide exfiltra datos antes de cifrar (Doble
    Extorsión). La información sensible queda expuesta al atacante y puede ser
    publicada, violando la confidencialidad de los datos corporativos.
    
    INTEGRIDAD: Aunque Base64 es reversible, un cifrado real (AES-256) altera
    los datos de forma irreversible sin la clave. Los archivos cifrados ya no
    representan la información original, comprometiendo su integridad.
    
    DISPONIBILIDAD: Es el pilar más afectado. Los archivos cifrados son
    inaccesibles para la organización, paralizando operaciones críticas.
    En el caso de Colonial Pipeline, esto provocó el cierre del oleoducto
    más grande de EE.UU. durante 6 días.

Autor: José Montero Vilcas
Curso: Seguridad de Aplicaciones — CIBERTEC 2026
"""

import os
import base64
import datetime
import textwrap
import shutil
import time


class RansomwareSimulator:
    """
    Simula el comportamiento de un ransomware tipo DarkSide.
    
    IMPORTANTE: Este simulador usa Base64 en lugar de cifrado real para
    garantizar que la demo sea segura y completamente reversible. En un
    ataque real, DarkSide usaba Salsa20 + RSA-1024 para cifrar archivos.
    """

    ENCRYPTED_EXTENSION = ".darkside_encrypted"
    RANSOM_NOTE_FILENAME = "README_TO_RECOVER_FILES.txt"

    def __init__(self, target_directory):
        """
        Inicializa el simulador con el directorio objetivo.
        
        En un escenario real, el ransomware escanearía unidades de red
        completas y recursos compartidos SMB para maximizar el daño.
        """
        self.target_directory = target_directory
        self.compromised_files = []
        self.total_size_bytes = 0
        self.start_time = None

    def simulate_encryption(self):
        """
        Recorre el directorio objetivo y 'cifra' cada archivo usando Base64.
        
        IMPACTO EN LA TRÍADA CIA:
        - DISPONIBILIDAD: Los archivos originales dejan de existir; solo
          queda la versión codificada con extensión .darkside_encrypted.
        - CONFIDENCIALIDAD: En un ataque real, los datos se exfiltran al
          servidor C2 del atacante ANTES del cifrado (Doble Extorsión).
        - INTEGRIDAD: El contenido original es reemplazado por datos
          codificados, perdiendo la representación fiel de la información.
        """
        self.start_time = time.time()

        print("\n" + "=" * 70)
        print("  ☠️  DARKSIDE RANSOMWARE SIMULATOR — FASE DE CIFRADO")
        print("=" * 70)
        print(f"  [*] Directorio objetivo: {self.target_directory}")
        print(f"  [*] Timestamp: {datetime.datetime.now().isoformat()}")
        print(f"  [*] Extensión de cifrado: {self.ENCRYPTED_EXTENSION}")
        print("-" * 70)

        # Simular fase de exfiltración previa (Doble Extorsión)
        print("\n  [FASE 1] EXFILTRACIÓN DE DATOS (Doble Extorsión)")
        print("  " + "-" * 50)
        total_exfil = 0
        for root, dirs, files in os.walk(self.target_directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                size = os.path.getsize(filepath)
                total_exfil += size
                relative = os.path.relpath(filepath, self.target_directory)
                print(f"  [EXFIL] Copiando al C2: {relative} ({size} bytes)")
                time.sleep(0.1)

        print(f"\n  [*] Total exfiltrado: {total_exfil:,} bytes")
        print("  [*] Datos enviados al servidor C2 del atacante")
        print("  [!] CONFIDENCIALIDAD COMPROMETIDA — datos en poder del atacante\n")

        # Fase de cifrado
        print("  [FASE 2] CIFRADO DE ARCHIVOS")
        print("  " + "-" * 50)

        for root, dirs, files in os.walk(self.target_directory):
            for filename in files:
                if filename == self.RANSOM_NOTE_FILENAME:
                    continue
                if filename.endswith(self.ENCRYPTED_EXTENSION):
                    continue

                filepath = os.path.join(root, filename)
                self._encrypt_file(filepath)

        elapsed = time.time() - self.start_time

        print("\n" + "-" * 70)
        print(f"  [✓] Cifrado completado en {elapsed:.2f} segundos")
        print(f"  [✓] Archivos comprometidos: {len(self.compromised_files)}")
        print(f"  [✓] Datos cifrados: {self.total_size_bytes:,} bytes")
        print(f"  [!] DISPONIBILIDAD COMPROMETIDA — archivos inaccesibles")
        print(f"  [!] INTEGRIDAD COMPROMETIDA — contenido original alterado")
        print("=" * 70)

    def _encrypt_file(self, filepath):
        """
        'Cifra' un archivo individual usando codificación Base64.
        
        En un ataque real de DarkSide:
        - Se generaría una clave Salsa20 única por archivo.
        - La clave se cifraría con RSA-1024 del atacante.
        - El archivo original se sobrescribiría con los datos cifrados.
        - Se usaría I/O asíncrono para maximizar velocidad de cifrado.
        """
        try:
            with open(filepath, 'rb') as f:
                original_data = f.read()

            file_size = len(original_data)
            encoded_data = base64.b64encode(original_data)

            encrypted_path = filepath + self.ENCRYPTED_EXTENSION
            with open(encrypted_path, 'wb') as f:
                f.write(encoded_data)

            os.remove(filepath)

            relative_path = os.path.relpath(filepath, self.target_directory)
            self.compromised_files.append(relative_path)
            self.total_size_bytes += file_size

            print(f"  [LOCKED] 🔒 {relative_path}")
            print(f"           Tamaño: {file_size:,} bytes | "
                  f"Nuevo: {os.path.basename(encrypted_path)}")
            time.sleep(0.15)

        except Exception as e:
            print(f"  [ERROR] No se pudo cifrar {filepath}: {e}")

    def generate_ransom_note(self):
        """
        Genera la nota de rescate simulada en el directorio objetivo.
        
        Las notas de ransomware reales de DarkSide eran sorprendentemente
        profesionales. El grupo operaba como RaaS (Ransomware-as-a-Service)
        y mantenía un portal .onion con chat de "soporte" al cliente.
        
        La técnica de Doble Extorsión amenaza con publicar los datos
        exfiltrados si no se paga el rescate, presionando a la víctima
        incluso si tiene backups funcionales.
        """
        note_path = os.path.join(self.target_directory, self.RANSOM_NOTE_FILENAME)

        note_content = textwrap.dedent(f"""\
        ============================================================
              ☠️  DARKSIDE RANSOMWARE — NOTA DE RESCATE  ☠️
        ============================================================

        ¡Atención!

        Tu red corporativa ha sido COMPROMETIDA por el grupo DarkSide.

        ¿Qué ha sucedido?
        ------------------
        • Todos tus archivos han sido CIFRADOS con algoritmos de
          grado militar (Salsa20 + RSA-1024).
        • Hemos EXFILTRADO más de 100 GB de datos confidenciales
          de tu infraestructura, incluyendo:
            - Registros financieros y facturación
            - Documentos estratégicos corporativos
            - Datos personales de empleados y clientes
            - Contratos y acuerdos legales

        DOBLE EXTORSIÓN:
        ----------------
        Si NO pagas el rescate:
        1. Tus archivos permanecerán cifrados PERMANENTEMENTE.
        2. Publicaremos TODOS los datos exfiltrados en nuestro
           blog de filtraciones en la Dark Web.

        Instrucciones de Pago:
        ----------------------
        • Monto: 75 BTC (≈ $4,400,000 USD)
        • Wallet Bitcoin: bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh
        • Plazo: 5 días antes de publicar los datos.
        • Portal de negociación: http://darkside[REDACTED].onion

        Archivos comprometidos: {len(self.compromised_files)}
        Datos cifrados: {self.total_size_bytes:,} bytes
        Timestamp: {datetime.datetime.now().isoformat()}

        ---

        ⚠️ AVISO: ESTO ES UNA SIMULACIÓN EDUCATIVA.
        Ningún archivo ha sido realmente cifrado con criptografía.
        Se usó Base64 (reversible) con fines demostrativos.
        Curso: Seguridad de Aplicaciones — CIBERTEC 2026
        Alumno: José Montero Vilcas

        ============================================================
        """)

        with open(note_path, 'w', encoding='utf-8') as f:
            f.write(note_content)

        print(f"\n  [RANSOM] 📄 Nota de rescate generada: {self.RANSOM_NOTE_FILENAME}")
        print(f"  [RANSOM] Rescate exigido: 75 BTC (~$4.4M USD)")
        print(f"  [RANSOM] Amenaza: publicación de 100GB de datos exfiltrados")


def create_mock_files(target_dir):
    """
    Crea archivos de ejemplo que simulan datos corporativos reales.
    
    En el caso de Colonial Pipeline (mayo 2021), DarkSide comprometió
    los sistemas IT de la empresa, lo que llevó al cierre preventivo
    del oleoducto que transporta el 45% del combustible de la costa
    este de Estados Unidos. La empresa pagó 4.4 millones de dólares
    en Bitcoin como rescate.
    """
    print("\n" + "=" * 70)
    print("  📁 PREPARACIÓN DEL ENTORNO DE SIMULACIÓN")
    print("=" * 70)

    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.makedirs(target_dir)

    files_to_create = {
        "facturacion_Q1_2026.csv": (
            "ID,Cliente,Monto,Fecha,Estado\n"
            "F-001,Petrogas S.A.,45000.00,2026-01-15,Pagada\n"
            "F-002,Refinería del Norte,128500.50,2026-01-22,Pendiente\n"
            "F-003,Distribuidora Central,67200.00,2026-02-01,Pagada\n"
            "F-004,Terminal Marítima LLC,215000.00,2026-02-10,Pendiente\n"
            "F-005,Logística Colonial,89750.25,2026-02-15,Pagada\n"
            "F-006,Estaciones Nacionales,34100.00,2026-03-01,Pendiente\n"
        ),
        "plan_estrategico_2026.docx.txt": (
            "PLAN ESTRATÉGICO CORPORATIVO 2026\n"
            "=================================\n"
            "CONFIDENCIAL — Solo para directivos\n\n"
            "1. Expansión de oleoducto Tramo Norte: inversión $120M\n"
            "2. Migración a SCADA v4.2 con segmentación de red OT/IT\n"
            "3. Adquisición de Terminal Portuaria del Pacífico\n"
            "4. Reducción de costos operativos: meta 15% en Q3\n"
            "5. Programa de ciberseguridad: presupuesto $8.5M\n"
        ),
        "empleados_nomina.csv": (
            "ID,Nombre,Cargo,Salario,SSN_Simulado\n"
            "E-001,María González,Directora IT,95000,XXX-XX-1234\n"
            "E-002,Carlos Ramírez,Ingeniero SCADA,72000,XXX-XX-5678\n"
            "E-003,Ana Torres,Analista SOC,65000,XXX-XX-9012\n"
            "E-004,Luis Mendoza,Operador Planta,48000,XXX-XX-3456\n"
        ),
        "contratos/contrato_proveedor_A.txt": (
            "CONTRATO DE SERVICIO N° CS-2026-0147\n"
            "Proveedor: CyberDefense Corp.\n"
            "Servicio: Monitoreo SOC 24/7\n"
            "Vigencia: 01/01/2026 — 31/12/2026\n"
            "Monto anual: $450,000 USD\n"
            "Cláusula de confidencialidad: Nivel 3\n"
        ),
        "contratos/acuerdo_NDA_colonial.txt": (
            "ACUERDO DE NO DIVULGACIÓN (NDA)\n"
            "Partes: Colonial Pipeline Co. y Gobierno Federal\n"
            "Clasificación: CONFIDENCIAL\n"
            "Infraestructura crítica: Categoría 1\n"
            "Penalización por incumplimiento: $5,000,000\n"
        ),
        "backups/config_scada_backup.cfg": (
            "[SCADA_CONFIG]\n"
            "version=4.1.3\n"
            "protocol=modbus_tcp\n"
            "plc_addresses=192.168.100.10-50\n"
            "hmi_server=10.0.1.5\n"
            "historian_db=10.0.2.10:5432\n"
            "auth_mode=legacy_password\n"
            "# NOTA: Migrar a certificados en Q2 2026\n"
        ),
    }

    for relative_path, content in files_to_create.items():
        full_path = os.path.join(target_dir, relative_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [+] Creado: {relative_path} ({len(content)} bytes)")

    print(f"\n  [✓] {len(files_to_create)} archivos de ejemplo creados en: {target_dir}")
    print("=" * 70)


def main():
    """
    Bloque principal que orquesta la simulación completa.
    
    Flujo del ataque simulado:
    1. Crear archivos de ejemplo (datos corporativos mock)
    2. Ejecutar la simulación de cifrado (con exfiltración previa)
    3. Generar la nota de rescate
    4. Mostrar resumen del impacto en la Tríada CIA
    """
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║     SIMULACIÓN EDUCATIVA DE RANSOMWARE — DARKSIDE          ║
    ║     Caso: Colonial Pipeline (Mayo 2021)                    ║
    ║                                                            ║
    ║  ⚠️  Este script es 100% educativo y seguro.               ║
    ║  ⚠️  Usa Base64 (reversible), NO criptografía real.        ║
    ║                                                            ║
    ║  Curso: Seguridad de Aplicaciones — CIBERTEC 2026          ║
    ║  Alumno: José Montero Vilcas                               ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

    target_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "colonial_pipeline_mock_data")

    # PASO 1: Crear archivos de ejemplo
    create_mock_files(target_dir)

    # PASO 2: Iniciar simulación de ransomware
    simulator = RansomwareSimulator(target_dir)
    simulator.simulate_encryption()

    # PASO 3: Generar nota de rescate
    simulator.generate_ransom_note()

    # PASO 4: Resumen final con análisis de impacto CIA
    print("\n" + "=" * 70)
    print("  📊 RESUMEN DEL ATAQUE — IMPACTO EN LA TRÍADA CIA")
    print("=" * 70)
    print(f"""
  ┌─────────────────────────────────────────────────────────────┐
  │ CONFIDENCIALIDAD  ❌ COMPROMETIDA                          │
  │   → 100GB de datos exfiltrados al servidor C2              │
  │   → Amenaza de publicación en la Dark Web                  │
  │   → Datos de empleados, contratos y config. SCADA expuestos│
  ├─────────────────────────────────────────────────────────────┤
  │ INTEGRIDAD  ❌ COMPROMETIDA                                │
  │   → {len(simulator.compromised_files)} archivos alterados (contenido original reemplazado)  │
  │   → Sin la clave de descifrado, los datos son irrecuperables│
  │   → Hashes originales ya no coinciden                       │
  ├─────────────────────────────────────────────────────────────┤
  │ DISPONIBILIDAD  ❌ COMPROMETIDA (Pilar más afectado)       │
  │   → {simulator.total_size_bytes:,} bytes de datos inaccesibles               │
  │   → Operaciones paralizadas (Colonial Pipeline: 6 días)    │
  │   → Rescate exigido: 75 BTC (~$4.4M USD)                  │
  └─────────────────────────────────────────────────────────────┘

  LECCIONES DEL CASO COLONIAL PIPELINE:
  • La segmentación de redes IT/OT es crítica
  • Los backups offline son la mejor defensa contra ransomware
  • El pago del rescate NO garantiza la recuperación de datos
  • La respuesta a incidentes debe incluir plan de comunicación
  • La ciberseguridad en infraestructura crítica es seguridad nacional
    """)
    print("=" * 70)
    print("  FIN DE LA SIMULACIÓN EDUCATIVA")
    print("=" * 70)

    # Mostrar contenido del directorio después del ataque
    print("\n  📂 Estado del directorio después del ataque:")
    print("  " + "-" * 50)
    for root, dirs, files in os.walk(target_dir):
        level = root.replace(target_dir, '').count(os.sep)
        indent = '  ' + '  ' * level
        print(f"{indent}📁 {os.path.basename(root)}/")
        sub_indent = '  ' + '  ' * (level + 1)
        for file in files:
            icon = "🔒" if file.endswith(simulator.ENCRYPTED_EXTENSION) else "📄"
            print(f"{sub_indent}{icon} {file}")


if __name__ == "__main__":
    main()
