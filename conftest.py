import pytest
from selene import browser


@pytest.fixture(scope='session', params=[(1280, 720), (412, 915), (430, 932)],
                ids=['desktop', 'Samsung Galaxy S20 Ultra', 'iPhone 14 Pro Max'])
def open_github(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    browser.config.base_url = "https://github.com"

    if width > 1012:
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()


@pytest.fixture(scope='session', params=[(1280, 720), (1920, 1080), (2048, 1080)],
                ids=['HD 720p', 'Full HD 1080p', '2K'])
def open_github_desktop(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    browser.config.base_url = "https://github.com"


@pytest.fixture(scope='session', params=[(360, 740), (412, 915), (414, 896)],
                ids=['Samsung Galaxy S8+', 'Pixel 7', 'iPhone XR'])
def open_github_mobile(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    browser.config.base_url = "https://github.com"
