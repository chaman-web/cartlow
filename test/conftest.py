import pytest

@pytest.fixture()
def set_up_tear_down(page) -> None:
    # page.set_viewport_size({"width": 1280, "height": 760})
    page.goto("https://www.cartlow.com/uae/en")
    yield page