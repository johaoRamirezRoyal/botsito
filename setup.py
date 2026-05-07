from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto("https://dedicatedteacher.cambridge.org/vote/")

     # Esperar a que el banner de cookies aparezca
    page.wait_for_selector("#ub-gdpr-button-accept", timeout=10000)

    # Hacer clic en el botón por su ID
    page.click("#ub-gdpr-button-accept")

    # Esperar a que el banner desaparezca
    page.wait_for_selector("#ub-gdpr", state="hidden", timeout=5000)

    print("✅ Cookies aceptadas")
    
    page.wait_for_selector("iframe.hs-form-iframe", timeout=10000)

    # Acceder al frame como objeto (no frame_locator)
    iframe = page.frame(name="hs-form-iframe-0")  # usa el id del iframe

    # Imprimir todos los inputs disponibles dentro del iframe
    inputs = iframe.query_selector_all("input")
    for inp in inputs:
        corina = "choose_your_global_winner_of_the_2026_cambridge_dedicated_teacher_awards2-c19294fc-3923-4d33-a7af-d9326459f0f6"
        nombre = inp.get_attribute("name")
        id = inp.get_attribute("id")
        tipo = inp.get_attribute("type")
        value = inp.get_attribute("value")
        placeholder = inp.get_attribute("placeholder")
        
        if(corina == id):
            print(f"name: {nombre} | type: {tipo} | placeholder: {placeholder} | id: {id} | value: {value}")
        

    time.sleep(5)
    browser.close()


    # html = page.content()

    # soup = BeautifulSoup(html, "html.parser")
    
    # with open("pagina.html", "w", encoding="utf-8") as f:
    #     f.write(soup.prettify())

    # browser.close()