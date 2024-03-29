from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert button, 'button add to basket is not presented'
