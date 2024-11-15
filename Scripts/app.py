from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)

    context = browser.new_context(

        viewport={

            "width":300,
            "height": 400,
        }
    )
    # Create a new page
    page = context.new_page()
    
    # Visit the playwright website
    page.goto("https://playwright.dev/python")

    # Locate a link element with "Docs" text
    docs_button = page.get_by_role('link', name="Docs")
    

    docs_button.click()

    page.set_viewport_size(
          
            viewport={

            "width":100,
            "height": 200,
        }

    )

    # Get the url
    print("Docs:", page.url)

    browser.close()