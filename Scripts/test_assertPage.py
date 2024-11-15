
from playwright.sync_api import Page,expect

def test_linked(page: Page):
    page.goto("http://uitestingplayground.com/")
    
    button = page.get_by_role("button",name="Button with Dynamic ID")
    
    expect(button).to_be_visible()

    breakpoint()

    button.click()

