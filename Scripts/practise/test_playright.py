from playwright.sync_api import Page, BrowserContext
import pytest

DOCS_URL = "https://playwright.dev/python/docs/intro"

@pytest.fixture(scope="function")

def context(browser) -> BrowserContext:
    context = browser.new_context(record_video_dir='films/')
    yield context
    context.close()

@pytest.fixture(autouse= True, scope= "function")
def page(context) -> Page:
    page = context.new_page()
    page.goto("https://playwright.dev/python/")
    yield page
    #video_path = page.video.path()
    #print(f"Video recorded: {video_path}")  # Prints video location
    page.close()

def test_docs_link_page(page: Page): 
    link = page.get_by_role("link", name="Docs")
    link.click()
    assert link.is_visible()


def test_get_started(page: Page):
    link = page.get_by_role("link", name="GET STARTED")
    link.click()
    page.screenshot(path="snaps.jpg")
    assert page.url == DOCS_URL



