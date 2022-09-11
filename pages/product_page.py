from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_book_to_basket(self):
        self.should_be_element(*ProductPageLocators.BASKET_BUTTON)
        login_link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        login_link.click()
        self.solve_quiz_and_get_code()

    def assert_book_is_added(self):
        actual_price = self.get_element_text(*ProductPageLocators.PRICE_BOOK)
        actual_name = self.get_element_text(*ProductPageLocators.NAME_BOOK)
        expected_price = self.get_element_text(*ProductPageLocators.PRICE_IN_BASKET)
        expected_name = self.get_element_text(*ProductPageLocators.NAME_IN_BASKET)
        message_added = self.get_element_text(*ProductPageLocators.SUCCESS_MESSAGE)
        assert "has been added to your basket." in message_added, f"Книга не добавилась в корзину"
        assert actual_price == expected_price, f"Ожидаемый результат {actual_price}, " \
                                               f"Фактический результат {expected_price}"
        assert actual_name == expected_name, f"Ожидаемый результат {actual_name}, " \
                                             f"Фактический результат {expected_name}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            f"Сообщения об успехе есть на странице"

    def staleness_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            f"Сообщения об успехе продолжает отображаться"