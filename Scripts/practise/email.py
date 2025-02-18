from playwright.sync_api import sync_playwright
from time import perf_counter

with sync_playwright() as playwright:

    browser = playwright.firefox.launch(headless= False,slow_mo =500)

    page = browser.new_page()

    page.goto("https://accounts.google.com")

    email_input = page.get_by_label("Email or phone")
    set_email = "shuvankar95@gmail.com"
    email_input.fill(set_email)
    
    next_btn = page.get_by_role("button", name= "Next")
    next_btn.click()

    password = page.get_by_label("Enter your password")
    set_pass = "Dashbapu"

    password.fill(set_pass)
    next_btn.click()