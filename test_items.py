from selenium.webdriver.common.by import By
def test_guest_should_see_login_link(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    x = len(browser.find_elements(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert x > 0, 'Not found'