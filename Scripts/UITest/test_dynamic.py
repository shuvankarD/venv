from playwright.sync_api import Page,expect

def test_linked(page: Page):
    page.goto("http://uitestingplayground.com/dynamictable")

    label = page.locator("p.bg-warning").inner_text()

    percentage = label.split()[-1]
    
    headers = page.get_by_role("columnheader")
    cpu_column = None

    for index in range(headers.count()):
        header = headers.nth(index)

        if header.inner_text() =="CPU":
         cpu_column = index 
         break   

    assert cpu_column != None

    rowgroup = page.get_by_role("rowgroup").last

    chrome_row = rowgroup.get_by_role("row").filter(
       has_text= "Chrome"
    )    
    
    chrome_value = chrome_row.get_by_role("cell").nth(cpu_column)
     

    expect(chrome_value).to_have_text(percentage)