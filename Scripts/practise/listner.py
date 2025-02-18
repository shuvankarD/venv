from playwright.sync_api import sync_playwright
from time import perf_counter


with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless= False,slow_mo =500)

    page = browser.new_page()
    page.goto("https://unsplash.com/photos/a-person-swimming-in-the-ocean-with-a-camera-NhWxAIs61MM")
    
    btn = page.get_by_role("button", name = "Download")

    with page.expect_download() as download_info:
        btn.click()

    download = download_info.value
    download.save_as("moon.jpg")    

    browser.close()
