
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless= False,slow_mo =5000)

    page = browser.new_page()

    page.goto("https://bootswatch.com/default/")
    
    # btn = page.locator("//button[contains(@class, 'btn-outline-primary')]")
    # btn.click()

    # btn = page.get_by_role("button",name="Block button").first

    # btn.click(modifiers=["Shift"])

    # valid_input = page.get_by_label("Valid input").first
    
    # valid_input.input_value()

    # valid_input.click()
    
    # checkbox = page.locator("#flexCheckDefault")

    # checkbox.set_checked(False)

    # options = page.get_by_label("Example multiple select")

    # options.select_option(["2","4"])

    # dropdown = page.locator("#btnGroupDrop1").first

    # dropdown.click()

    with page.expect_file_chooser() as fc_info:


       file_input = page.get_by_label("Default file input example")

       file_input.click()

       file_chooser = fc_info.value

       file_chooser.set_files("file.txt")

    # btn = page.get_by_role("button", name="Default button")
    # checkbox = page.get_by_role("checkbox", name ="Default checkbox")
    # email_input = page.get_by_label("Email address").nth(0)
    # password = page.get_by_placeholder("Password").nth(0)
    # text = page.get_by_text("fine print")
    # title = page.get_by_title("Source Title").nth(1)#

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
