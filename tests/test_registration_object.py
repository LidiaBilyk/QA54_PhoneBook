import uuid

from models.user import User
from pages.registration_page import RegistrationPage


def test_registration_success(driver):
    registration_page = RegistrationPage(driver)

    random_suffix = uuid.uuid4().hex[:8]

    user = User(
    f"User_{random_suffix}@gm.com",
        "Aa_12345!")

    registration_page.open_registration_page()
    registration_page.fill_email_field(user.username)
    registration_page.fill_password_field(user.password)
    registration_page.click_registration_button()
    assert registration_page.is_sign_out_displayed()


def test_registration_invalid_email(driver):
    registration_page = RegistrationPage(driver)

    random_suffix = uuid.uuid4().hex[:8]

    user = User(
        f"User_{random_suffix}gm.com",
        "Aa_12345!")

    registration_page.open_registration_page()
    registration_page.fill_email_field(user.username)
    registration_page.fill_password_field(user.password)
    registration_page.click_registration_button()
    assert "Wrong email or password" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_invalid_password(driver):
    registration_page = RegistrationPage(driver)

    random_suffix = uuid.uuid4().hex[:8]

    user = User(
        f"User_{random_suffix}@gm.com",
        "Aa12345")

    registration_page.open_registration_page()
    registration_page.fill_email_field(user.username)
    registration_page.fill_password_field(user.password)
    registration_page.click_registration_button()
    assert "Wrong email or password" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_existing_user(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "user_test@gm.com",
        "Aa_12345!")

    registration_page.open_registration_page()
    registration_page.fill_email_field(user.username)
    registration_page.fill_password_field(user.password)
    registration_page.click_registration_button()
    assert "User already exist" in registration_page.get_alert_text()
    registration_page.accept_alert()

