from selenium.common.exceptions import *
import math
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        self.browser.implicitly_wait(0)
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            self.browser.implicitly_wait(10)
            return True
        self.browser.implicitly_wait(10)
        return False

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Ссылка на логин отсутсвует"

    def go_to_view_basket(self):
        assert self.is_element_present(*BasePageLocators.VIEW_BASKET_BUTTON), f"Кнопка 'Посмотреть корзину' не найдена"
        self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON).click()

    def get_element_text(self, how, what):
        self.should_be_element(how, what)
        text = self.browser.find_element(how, what).text
        return text

    def should_be_element(self, how, what):
        assert self.is_element_present(how, what), f"{what} данный локатор не найден на странице"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def field_enter(self, how, what, text):
        self.should_be_element(how, what)
        self.browser.find_element(how, what).send_keys(text)

    def click(self, how, what):
        self.should_be_element(how, what)
        self.browser.find_element(how, what).click()