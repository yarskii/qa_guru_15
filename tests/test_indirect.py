import pytest
from selene import browser, be, have


@pytest.mark.parametrize('open_github', [(1920, 1080)], ids=['HD'], indirect=True)
def test_desktop_version(open_github):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').should(be.visible).click()
    browser.element('.application-main').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize('open_github', [(768, 1024), (375, 667)],
                         ids=['iPad Mini', 'iPhone SE'], indirect=True)
def test_mobile_version(open_github):
    browser.open('/')
    button = browser.element('.flex-1.flex-order-2.text-right')
    button.should(be.visible).element('.js-prevent-focus-on-mobile-nav').click()
    browser.element('.application-main').should(have.text('Sign in to GitHub'))
