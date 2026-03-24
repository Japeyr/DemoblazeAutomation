import pytest
from selenium import webdriver
from FuncionesDemoblaze import FuncionesGlobales


# Fixture para manejar el driver automáticamente
@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # <--- OBLIGATORIO para GitHub Actions
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    f = FuncionesGlobales(driver)
    f.navegar("https://www.demoblaze.com/index.html")
    yield driver, f
    driver.quit()


# Test parametrizado (4 tests en 1 solo bloque de código)
@pytest.mark.parametrize("user, password, desc", [
    ("jorge6", "1111", "Login Exitoso"),
    ("", "", "Campos Vacíos"),
    ("jorge6", "error123", "Password Incorrecto"),
    ("no_existo", "123", "Usuario no existente")
])
def test_logins(setup, user, password, desc):
    driver, f = setup

    f.click_xpath_validado("//a[@id='login2']", 1)
    f.texto_id_validado("loginusername", user, 0.5)
    f.texto_id_validado("loginpassword", password, 0.5)  # Creando este metodo en Globales
    f.click_xpath_validado("//button[@onclick='logIn()']", 1)

    # Aquí podrías agregar un ASSERT para validar alertas o mensajes
    if desc == "Login Exitoso":
        texto_bienvenida = f.obtener_texto_xpath("//a[@id='nameofuser']")
        # En el test:
        assert f"Welcome {user}" in texto_bienvenida
        f.logout()

    elif desc == "Campos Vacíos":
        mensaje = f.obtener_texto_alerta()
        assert mensaje == "Please fill out Username and Password."

    elif desc == "Password Incorrecto":
        mensaje = f.obtener_texto_alerta()
        assert mensaje == "Wrong password."

    elif desc == "Usuario no existente":
        mensaje = f.obtener_texto_alerta()
        assert mensaje == "User does not exist."

    print(f"Ejecutando caso: {desc}")
