import os
import time

def rename_downloaded_file(new_name, download_dir):
    # Esperar a que el archivo se descargue completamente
    time.sleep(10)  
    files = os.listdir(download_dir)
    files = [f for f in files if f.endswith('.crdownload') or f.endswith('.xlsx')]
    
    if files:
        latest_file = max([os.path.join(download_dir, f) for f in files], key=os.path.getctime)

        if latest_file.endswith('.crdownload'):
            time.sleep(10)  # Espera adicional si el archivo aún se está descargando

        if latest_file.endswith('.xlsx') and os.path.basename(latest_file).startswith("data"):
            os.rename(latest_file, os.path.join(download_dir, new_name))
            return True
    return False