from pages.base_page import BasePage

class CheckoutInfoPage(BasePage):

    first_name = "input[data-test='firstName']"
    last_name = "input[data-test='lastName']"
    postal_code = "input[data-test='postalCode']"
    continue_button = "input[data-test='continue']"

    def enter_user_info(self, first, last, zip_code):
        self.page.fill(self.first_name, first)
        self.page.fill(self.last_name, last)
        self.page.fill(self.postal_code, zip_code)
        self.page.click(self.continue_button)
