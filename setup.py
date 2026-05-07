from playwright.sync_api import sync_playwright

def inputFormIntersection(email):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled"
            ]
        )

        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            )
        )

        page = context.new_page()

        page.goto(
            "https://dedicatedteacher.cambridge.org/vote/",
            wait_until="networkidle"
        )

        # Cookies
        page.locator(
            "#ub-gdpr-button-accept"
        ).click()

        frame = page.frame_locator(
            "iframe.hs-form-iframe"
        )

        valor_deseado = (
            "Corina Corpas, Colegio Real Royal School, Colombia"
        )

        # Radio
        radio = frame.locator(
            f"input[type='radio'][value='{valor_deseado}']"
        )

        radio.check(force=True)

        print("✅ Radio seleccionado")

        # Email
        email_input = frame.locator(
            "#email-c19294fc-3923-4d33-a7af-d9326459f0f6"
        )

        email_input.click()

        email_input.press_sequentially(email)

        print("✅ Email insertado")

        page.wait_for_timeout(2000)

        # Submit
        submit = frame.locator(
            "input[type='submit']"
        )

        submit.wait_for(state="visible")

        submit.click(force=True)

        print("✅ Submit enviado")

        page.wait_for_timeout(8000)

        browser.close()