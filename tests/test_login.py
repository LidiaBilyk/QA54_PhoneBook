from pages.login_page import LoginPage

VALID_EMAIL = "test1@gg.com"
INVALID_EMAIL = "test1gg.com"
VALID_PASSWORD = "Aa_1234!"

def test_valid_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(VALID_EMAIL)
    login_page.fill_password_field(VALID_PASSWORD)
    login_page.click_login_button()
    assert login_page.is_sign_out_displayed()

def test_with_wrong_email(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(INVALID_EMAIL)
    login_page.fill_password_field(VALID_PASSWORD)
    login_page.click_login_button()

