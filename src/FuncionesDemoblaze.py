import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

class FuncionesGlobales:

    def __init__(self, driver):
        self.driver = driver

    def navegar(self, url):
        self.driver.get(url)
        print("Navego a la pagina: ", url)
        self.driver.maximize_window()

    def click_xpath_validado(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("Se hizo click en el boton: ", xpath)
            time.sleep(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + xpath)

    def click_id_validado(self, aidi, tiempo):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, aidi)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, aidi)
            val.click()
            print("Se hizo click en el boton: ", aidi)
            time.sleep(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + aidi)

    def texto_id_validado(self, aidi, texto, tiempo):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, aidi)))
            val.clear()
            val.send_keys(texto)
            print(f"Escribiendo en {aidi}: {texto}")
            time.sleep(tiempo)  # Opcional, mejor usar esperas explicitas
        except TimeoutException as ex:
            print(f"No se encontró el elemento para escribir: {aidi}")

    def obtener_texto_alerta(self):
        try:
            # Espera a que la alerta aparezca
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alerta = self.driver.switch_to.alert
            texto = alerta.text
            alerta.accept()  # Cierra la alerta haciendo clic en OK
            return texto
        except:
            return None

    def obtener_texto_xpath(self, xpath):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return val.text
        except:
            return ""

    def logout(self):
        try:
            self.click_xpath_validado("//a[@id='logout2']", 1)
            print("Sesión cerrada correctamente.")
        except:
            pass
