import pytest
from playwright.sync_api import Page, expect,TimeoutError

def test_link(page: Page):

     page.goto("http://uitestingplayground.com/visibility")

     hide_btn = page.get_by_role("button",name="Hide")
     removed_button = page.get_by_role("button", name="Removed")
     zero_width_button = page.get_by_role("button", name="Zero Width")
     overlapped_button = page.get_by_role("button", name="Overlapped")
     opacity_0_button = page.get_by_role("button", name="Opacity 0")
     hidden_button = page.get_by_role("button", name="Visibility Hidden")
     display_none_button = page.get_by_role("button", name="Display None")
     offscreen_button = page.get_by_role("button", name="Offscreen")

     breakpoint()

     hide_btn.click()

     expect(removed_button).to_be_hidden()

     expect(zero_width_button).to_have_css("width","0px")

     with pytest.raises(TimeoutError):
          overlapped_button.click(timeout=2000)

     expect(opacity_0_button).to_have_css("opacity","0px")     

     expect(hidden_button).to_be_hidden()

     expect(display_none_button).to_be_hidden()

     expect(offscreen_button).not_to_be_in_viewport()