from pages.base_page import BasePage
import utils.config as config

class SauceLoginPage(BasePage):

    username_input = "#user-name"
    password_input = "#password"
    login_button = "#login-button"
    error_message = "h3[data-test='error']"

    def open_login_page(self):
        self.open(config.SAUCE_URL)

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        return self.page.text_content(self.error_message)
