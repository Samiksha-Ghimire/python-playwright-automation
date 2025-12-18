from pages.login_page import LoginPage
import utils.config as config

def test_user_can_login_with_valid_credentials(page):
    """Verify that a user can log in using valid credentials."""

    login = LoginPage(page)

    login.open_login_page()
    login.login(config.VALID_USERNAME, config.VALID_PASSWORD)

    message = login.get_message()

    assert "You logged into a secure area!" in message
