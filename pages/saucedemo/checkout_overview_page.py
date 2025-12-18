from pages.base_page import BasePage

class CheckoutOverviewPage(BasePage):

    finish_button = "button[data-test='finish']"
    success_message = ".complete-header"

    def finish_order(self):
        self.page.click(self.finish_button)

    def get_success_message(self):
        return self.page.text_content(self.success_message)
