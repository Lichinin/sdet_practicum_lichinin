import random

import allure

from constants.constants import Constants
from locators.locators import Selectors
from pages.base_page import BasePage


class FormsPage(BasePage):

    @allure.step('Заполнение поля "Name" значением "{name}"')
    def fill_field_name(self, name):
        field = self.get_element(Selectors.FIELD_NAME)
        self.click_and_clear(field)
        field.send_keys(name)

    @allure.step('Заполнение поля "Password" значением "{password}"')
    def fill_field_password(self, password):
        field = self.get_element(Selectors.FIELD_PASSWORD)
        self.click_and_clear(field)
        field.send_keys(password)

    @allure.step('Выбор напитка "Milk"')
    def check_drink_milk(self):
        self.get_element(Selectors.CHECKBOX_MILK).click()

    @allure.step('Выбор напитка "Coffee"')
    def check_drink_coffee(self):
        self.get_element(Selectors.CHECKBOX_COFFEE).click()

    @allure.step('Выбор цвета "Желтый"')
    def check_color_yellow(self):
        element = self.get_element(Selectors.RADIO_COLOR_YELLOW)
        self.scroll_to_element(element)
        element.click()

    @allure.step('Выбор случайного варианта "Do you like automation?"')
    def choice_like_automation(self):
        with allure.step('Поиск всех возможных непустых вариантов заполнения'):
            options = self.get_elements(Selectors.OPTIONS_AUTOMATIONS)
            valid_options = [option for option in options if option.get_attribute("value") != "default"]
        with allure.step('Выбор случайного значения из найденных вариантов'):
            random_option = random.choice(valid_options)
        random_option.click()

    @allure.step('Заполнение поля "Email" значением "{email}"')
    def fill_field_email(self, email):
        field = self.get_element(Selectors.FIELD_EMAIL)
        self.click_and_clear(field, scroll_first=True)
        field.send_keys(email)

    @allure.step('Заполнение поля "Message" с количеством инструментов и самым длинным названием')
    def fill_field_message(self):
        with allure.step('Подсчет количества инструментов'):
            tools = self.get_elements(Selectors.AUTOMATION_TOOLS)
            number_of_tools = len(tools)
        with allure.step('Поиск самого длинного названия инструмента'):
            tools_name = [tool.text for tool in tools]
            longer_tool = max(tools_name, key=len)
        message_field = self.get_element(Selectors.FIELD_MESSAGE)
        self.click_and_clear(message_field, scroll_first=True)
        with allure.step('Заполнение поля Message вычесленными значениями'):
            message_field.send_keys(f'{number_of_tools}\n{longer_tool}')

    @allure.step('Нажатие кнопки "Submit"')
    def click_button_submit(self):
        button = self.get_element(Selectors.BUTTON_SUBMIT)
        self.scroll_to_element(button)
        button.click()

    @allure.step("Проверка сообщения успешной отправки формы через alert")
    def assert_successfull_message_creation(self):
        alert = self.browser.switch_to.alert
        message = alert.text
        self.assert_equals(Constants.EXCEPTED_FORM_MESSAGE, message)
