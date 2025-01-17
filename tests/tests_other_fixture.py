from selene import browser, be, have


def test_desktop_version(open_github_desktop):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').should(be.visible).click()
    browser.element('.application-main').should(have.text('Sign in to GitHub'))


def test_mobile_version(open_github_mobile):
    browser.open('/')
    button = browser.element('.flex-1.flex-order-2.text-right')
    button.should(be.visible).element('.js-prevent-focus-on-mobile-nav').click()
    browser.element('.application-main').should(have.text('Sign in to GitHub'))
