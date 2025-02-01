
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless= False,slow_mo = 500)

    page = browser.new_page()

    page.goto("https://bootswatch.com/default/")

    # btn = page.get_by_role("button", name="Default button")
    # checkbox = page.get_by_role("checkbox", name ="Default checkbox")
    # email_input = page.get_by_label("Email address").nth(0)
    # password = page.get_by_placeholder("Password").nth(0)
    # text = page.get_by_text("fine print")
    # title = page.get_by_title("Source Title").nth(1)


    btn = page.locator("button.btn btn-success").nth(0)

    btn.click()


    # btn.highlight()
    # checkbox.highlight()

    # btn.click()
    # checkbox.click()

    # email_input.highlight()
    # email_input.click()

    # password.highlight()
    # password.click()

    # text.highlight()
    # title.click()


    browser.close()
