import pytest
from playwright.sync_api import Page, BrowserContext

DOCS_URL = "https://playwright.dev/python/docs/intro"

@pytest.fixture(autouse=True)
def test_trace(context: BrowserContext):
    context.tracing.start(
        name = "playwright",
        screenshots= True,
        snapshots= True,
        sources = True,
    )
    yield 
    context.tracing.stop(path="tracefile.zip")

def test_started_page(page: Page):
    
    page.goto("https://playwright.dev/python")
    
    link = page.get_by_role("link", name="GET STARTED")

    link.click()

    assert page.url == DOCS_URL