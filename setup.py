from playwright.sync_api import sync_playwright
import time

def inputFormIntersection(email):
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://dedicatedteacher.cambridge.org/vote/")

        # Aceptar cookies
        page.wait_for_selector("#ub-gdpr-button-accept", timeout=10000)
        page.click("#ub-gdpr-button-accept")
        page.wait_for_selector("#ub-gdpr", state="hidden", timeout=5000)
        print("✅ Cookies aceptadas")

        page.wait_for_selector("iframe.hs-form-iframe", timeout=10000)

        iframe = page.frame(name="hs-form-iframe-0")
        frame = page.frame_locator("iframe.hs-form-iframe")

        # El valor que quieres seleccionar
        valor_deseado = "Corina Corpas, Colegio Real Royal School, Colombia"  # ← cambia esto por el value del radio que quieres

        inputs = iframe.query_selector_all("input")

        for inp in inputs:
            nombre = inp.get_attribute("name")
            tipo   = inp.get_attribute("type")
            id     = inp.get_attribute("id")
            value  = inp.get_attribute("value")

            corina = "choose_your_global_winner_of_the_2026_cambridge_dedicated_teacher_awards2-c19294fc-3923-4d33-a7af-d9326459f0f6"

            # Opción 1: el id empieza con el prefijo que buscas
            if id and id.startswith(corina):
                print(f"name: {nombre} | type: {tipo} | id: {id} | value: {value}")

                # Seleccionar el radio que tenga el value deseado
                if value == valor_deseado:
                    frame.locator(f"input[type='radio'][value='{value}']").check()
                    print(f"✅ Radio seleccionado: {value}")
                    frame.locator("#email-c19294fc-3923-4d33-a7af-d9326459f0f6").fill(email)
                    print("✅ Email insertado")
                    break

        time.sleep(3)
        browser.close()