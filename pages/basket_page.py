from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_is_empty(self):
        self.should_be_element(*BasketPageLocators.EMPTY_TEXT)
        self.is_not_element_present(*BasketPageLocators.BASKET_FORM)
