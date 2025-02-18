from playwright.sync_api import sync_playwright
from time import perf_counter

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless= False,slow_mo =500)

    page = browser.new_page()


    page.goto("https://www.scrapethissite.com/pages/ajax-javascript/",
              wait_until='networkidle', )

    link = page.get_by_role("link", name= '2015')
    link.click(timeout=1000)
    
    
    print("Item loading...")
    start = perf_counter()

    table_data = page.locator("td.film-title").first
    table_data.wait_for()
    
    time_taken = perf_counter() - start
    print(f"Item loaded in {time_taken}s ...")

    browser.close()

