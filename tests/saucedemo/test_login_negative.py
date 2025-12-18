from pages.saucedemo.login_page import SauceLoginPage

def test_user_cannot_login_with_invalid_password(page):
    """Verify error message appears when user enters wrong password."""

    login = SauceLoginPage(page)

    login.open_login_page()
    login.login("standard_user", "wrong_password")

    error_text = login.get_error_message()

    assert "Username and password do not match" in error_text
    
    def test_user_cannot_login_with_invalid_username(page):
        """Verify error shows for invalid username."""


    login = SauceLoginPage(page)

    login.open_login_page()
    login.login("wrong_user", "secret_sauce")

    error_text = login.get_error_message()

    assert "Username and password do not match" in error_text

def test_login_fails_with_empty_username(page):
    """Username required error appears."""

    login = SauceLoginPage(page)

    login.open_login_page()
    login.login("", "secret_sauce")

    error_text = login.get_error_message()

    assert "Username is required" in error_text

def test_login_fails_with_empty_username(page):
    """Username required error appears."""

    login = SauceLoginPage(page)

    login.open_login_page()
    login.login("", "secret_sauce")

    error_text = login.get_error_message()

    assert "Username is required" in error_text

def test_login_fails_with_empty_password(page):
    """Password required error appears."""

    login = SauceLoginPage(page)

    login.open_login_page()
    login.login("standard_user", "")

    error_text = login.get_error_message()

    assert "Password is required" in error_text

def test_login_fails_with_empty_credentials(page):
    """Both fields empty should show username required."""

    login = SauceLoginPage(page)

    login.open_login_page()
    login.login("", "")

    error_text = login.get_error_message()

    assert "Username is required" in error_text

def test_locked_out_user_cannot_login(page):
    """Locked out user sees appropriate error."""

    login = SauceLoginPage(page)

    login.open_login_page()
    login.login("locked_out_user", "secret_sauce")

    error_text = login.get_error_message()

    assert "Sorry, this user has been locked out." in error_text

