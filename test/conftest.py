import pytest

@pytest.fixture()
def set_up_tear_down(page) -> None:
    # page.set_viewport_size({"width": 1366, "height": 1000})
    page.goto("https://www.cartlow.com/uae/en")
    yield page