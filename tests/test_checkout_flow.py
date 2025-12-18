from pages.saucedemo.login_page import SauceLoginPage
from pages.saucedemo.inventory_page import InventoryPage
from pages.saucedemo.cart_page import CartPage
from pages.saucedemo.checkout_info_page import CheckoutInfoPage
from pages.saucedemo.checkout_overview_page import CheckoutOverviewPage

def test_user_can_complete_checkout_flow(page):
    """Full end-to-end test: login → add item → checkout → finish order."""

    # Login
    login = SauceLoginPage(page)
    login.open_login_page()
    login.login("standard_user", "secret_sauce")

    # Inventory page
    inventory = InventoryPage(page)
    inventory.add_item_to_cart()
    inventory.open_cart()

    # Cart page
    cart = CartPage(page)
    cart.proceed_to_checkout()

    # Checkout info page
    info = CheckoutInfoPage(page)
    info.enter_user_info("Samiksha", "Ghimire", "85281")

    # Checkout overview page
    overview = CheckoutOverviewPage(page)
    overview.finish_order()

    # Assert successful order
    success_message = overview.get_success_message()
    assert "thank you for your order" in success_message.lower()





