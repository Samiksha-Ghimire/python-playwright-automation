from pages.saucedemo.login_page import SauceLoginPage
import utils.config as config

def test_user_can_login_with_valid_credentials(page):
    """Verify that a standard user is able to log into SauceDemo."""

    login = SauceLoginPage(page)

    login.open_login_page()
    login.login("standard_user", "secret_sauce")

    # Verify we land on the inventory page by checking URL
    assert page.url.endswith("/inventory.html")
