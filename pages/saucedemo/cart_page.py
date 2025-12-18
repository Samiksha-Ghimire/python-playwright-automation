from pages.base_page import BasePage

class CartPage(BasePage):

    checkout_button = "button[data-test='checkout']"

    def proceed_to_checkout(self):
        self.page.click(self.checkout_button)
