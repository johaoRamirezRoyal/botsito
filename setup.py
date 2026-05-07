from playwright.sync_api import sync_playwright
import time

def inputFormIntersection(email):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
        )

        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36")

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

        valor_deseado = "Corina Corpas, Colegio Real Royal School, Colombia"

        inputs = iframe.query_selector_all("input")

        radio_seleccionado = False

        for inp in inputs:
            nombre = inp.get_attribute("name")
            tipo   = inp.get_attribute("type")
            id     = inp.get_attribute("id")
            value  = inp.get_attribute("value")

            corina = "choose_your_global_winner_of_the_2026_cambridge_dedicated_teacher_awards2-c19294fc-3923-4d33-a7af-d9326459f0f6"

            if id and id.startswith(corina):
                print(f"name: {nombre} | type: {tipo} | id: {id} | value: {value}")

                if value == valor_deseado:
                    frame.locator(f"input[type='radio'][value='{value}']").check()
                    print(f"✅ Radio seleccionado: {value}")
                    radio_seleccionado = True
                    break

        if radio_seleccionado:
            # Insertar email
            frame.locator("#email-c19294fc-3923-4d33-a7af-d9326459f0f6").fill(email)
            print(f"✅ Email insertado: {email}")

            # Hacer submit
            frame.locator("input[type='submit'].hs-button.primary.large").click()
            print("✅ Formulario enviado")
        else:
            print("⚠️ No se encontró el radio deseado, formulario no enviado")

        time.sleep(15000)
        browser.close()

# Llamar la función
inputFormIntersection("correo@ejemplo.com")
