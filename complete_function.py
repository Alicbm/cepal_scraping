import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# download_dir = "/mnt/c/Users/Alic Barandica/Documents/proyectos/cepal_scraping/files/all_files"
download_dir = "/mnt/c/Users/Alic Barandica/Documents/proyectos/cepal_scraping/files/demografia"


def rename_downloaded_file(new_name):
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

def main_function():
    # Configuramos el driver de chrome
    service = Service(ChromeDriverManager().install())  # Instalar chrome si no existe
    option = webdriver.ChromeOptions()
    option.add_argument("--window-size=1400,1080")
    # option.add_argument("--window-size=1920,1080")

    option.add_experimental_option("prefs", {
        "download.default_directory": download_dir,  # Ruta personalizada para descargas
        "download.prompt_for_download": False,  # Evitar diálogos de confirmación
        "safebrowsing.enabled": True,  # Evitar bloqueos por contenido "inseguro"
    })

    driver = Chrome(service=service, options=option)
    driver.get("https://statistics.cepal.org/portal/cepalstat/dashboard.html?theme=1&lang=es")

    try:

        demograficos_sociales = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "box1394"))
        )

        ids_demograficos_sociales = ["box2395"]
        # ids_demograficos_sociales = ["box2395", "box2404"]

        for id_demografico_social in ids_demograficos_sociales:

            demografia = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, id_demografico_social))
            )

            demografia_items = demografia.find_elements(By.CSS_SELECTOR, "div.row-dash-indicator-2")

            ids_containers_elements = demografia.find_elements(By.CSS_SELECTOR, f"#{id_demografico_social} > div.boxniv_2")

            ids_containers = [item.get_attribute("id") for item in ids_containers_elements]

            for item_id, categoria in zip(ids_containers, demografia_items):

                if (categoria.get_attribute("textContent")).strip() != "Población": 
                    categoria.click()

                #container_poblacion
                poblacion_container = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, item_id))
                )
                
                elements_poblacion_container = poblacion_container.find_elements(By.CSS_SELECTOR, "div.row-dash-indicator-link-3")

                for section in elements_poblacion_container:
                    select_section = section.find_element(By.TAG_NAME, "span")
                    select_section.click()

                    name_category = section.find_element(By.TAG_NAME, "span")
                    
                    #filtros

                    #paises (boton de filtro, es enecsario que cargue primero para hacer los demas filtros)
                    paises = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "form#searchForm div.form-row div.form-group.col-md-2"))
                    ).click()

                    container_filter = driver.find_element(By.ID, "searchForm")
                    elements_filter = container_filter.find_element(By.TAG_NAME, "div")
                    elements = elements_filter.find_elements(By.CSS_SELECTOR, "div.form-group")

                    for element in elements[:-1]:
                        try:
                            res = element.find_element(By.CLASS_NAME, "multiselect-native-select")
                            res_p = res.find_element(By.CLASS_NAME, "btn-group")
                            pepe = res_p.find_element(By.CSS_SELECTOR, ".dropdown-item.multiselect-all")
                            if "active" in pepe.get_attribute("class"):
                                print("Ya está seleccionado")
                            else:
                                pepe.click()
                        except:
                            res = element.find_element(By.CLASS_NAME, "multiselect-native-select")
                            res_p = res.find_element(By.CLASS_NAME, "btn-group")
                            res_p.click()
                            pepe = res_p.find_element(By.CSS_SELECTOR, ".dropdown-item.multiselect-all")
                            if "active" in pepe.get_attribute("class"):
                                print("Ya está seleccionado")
                            else:
                                pepe.click()

                    boton_aplicar = elements[-1].find_element(By.TAG_NAME, "button").click()

                    #descargar excel
                    container_botones_descarga = driver.find_element(By.ID, "infoForm")
                    botones_descarga = container_botones_descarga.find_elements(By.TAG_NAME, "button")
                    
                    download_button = botones_descarga[-1].click()

                    # Renombrar el archivo descargado
                    while not rename_downloaded_file(f"{name_category.get_attribute('textContent')}.xlsx"):
                        print("Esperando a que el archivo se renombre...")
                        time.sleep(5)  # Espera antes de volver a intentar

    except Exception as e:
        print(f"Error al intentar hacer clic en el botón: {e}")
    finally:
        # Mantener el navegador abierto para inspección
        input("Presiona Enter para cerrar el navegador...")
        driver.quit()


if __name__ == "__main__":
    main_function()