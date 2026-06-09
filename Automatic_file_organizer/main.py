from pathlib import Path
import shutil

def organizar_archivos():

    carpeta_principal = Path.home() / "Desktop" / "Separador_de_archivos"

    lista = carpeta_principal.iterdir()

    extensiones = [".zip", ".txt", ".sb3", ".pdf", ".docx", ".xlsx", ".json"]

    for archivo in lista:

        if archivo.is_file():

            if archivo.suffix in extensiones:

                nombre_carpeta = archivo.suffix.replace(".", "")

                ruta_carpeta = carpeta_principal / nombre_carpeta

                ruta_carpeta.mkdir(exist_ok=True)

                shutil.move(str(archivo), str(ruta_carpeta))

organizar_archivos()