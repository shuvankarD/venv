from playwright.sync_api import Route, Page, expect

def on_route(route: Route):
   response = route.fetch()
   body = response.text().replace("Playwright enables","Dashbabu")

   route.fulfill(
       response= response,
       body = body,
   )

def test_docs_link(page:Page):

    page.route("https://playwright.dev/python",on_route)

    page.goto("https://playwright.dev/python")

    page.screenshot(path="networkk.jpg",full_page=True)

    page.pause()

    