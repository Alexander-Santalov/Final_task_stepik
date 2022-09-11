from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "Url incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.field_enter(*LoginPageLocators.EMAIL_FIELD, email)
        self.field_enter(*LoginPageLocators.PASS_FIELD, password)
        self.field_enter(*LoginPageLocators.REPEAT_PASS_FIELD, password)
        self.click(*LoginPageLocators.REGISTER_BUTTON)



