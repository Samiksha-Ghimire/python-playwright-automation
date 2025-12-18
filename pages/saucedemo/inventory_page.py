from pages.base_page import BasePage

class InventoryPage(BasePage):

    add_to_cart_button = "button[data-test='add-to-cart-sauce-labs-backpack']"
    cart_icon = ".shopping_cart_link"

    def add_item_to_cart(self):
        self.page.click(self.add_to_cart_button)

    def open_cart(self):
        self.page.click(self.cart_icon)
