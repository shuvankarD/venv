import pytest
from playwright.sync_api import Page, expect, TimeoutError

def test_prac(page: Page):
     page.goto("http://uitestingplayground.com/sampleapp")
     
     input = page.get_by_placeholder("Name")

     div = input.locator("..")

     div.hover()

     page.mouse.wheel(0,200)

     data ="python"

     input.fill(data)

     expect(input).to_have_value(data)