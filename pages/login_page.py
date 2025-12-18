from pages.base_page import BasePage
import utils.config as config

class LoginPage(BasePage):

    username_input = "#username"
    password_input = "#password"
    login_button = "button.radius"
    message = "#flash"

    def open_login_page(self):
        self.open(config.BASE_URL)

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_message(self):
        return self.page.text_content(self.message)
