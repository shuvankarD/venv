from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:

    browser = playwright.firefox.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    page = context.new_page()

    # Visit google accounts
    page.goto("https://accounts.google.com")

    # Enter email address
    email_input = page.get_by_label("Email or phone")
    email_input.fill("shuvankar@gmail.com")

    page.get_by_role("button", name="Next").click()

    # Enter password
    password_input = page.get_by_label("Enter password")
    password_input.fill("Neni")

    page.get_by_role("button", name="Next").click()

    # Pause if your account has two-factor authentication
    # then complete the same before resuming
    page.pause()

    # Save authentication state
    context.storage_state(
        path="playwright/.auth/storage_state.json",
	# make sure 👆 you've created the playwright/.auth directory
    )

    browser.close()