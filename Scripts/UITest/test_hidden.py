import pytest
from playwright.sync_api import TimeoutError, Page,expect

def test_linked(page: Page):
    page.goto("http://uitestingplayground.com/")
    
    load_delay = page.get_by_role("link", name="Load Delay")

    load_delay.click()

    btn = page.locator("//button[@class='btn btn-primary']")

    btn.wait_for(timeout=20_000)

    expect(btn).to_be_visible()

    btn.click()

