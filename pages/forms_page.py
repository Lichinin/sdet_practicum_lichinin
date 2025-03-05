import random
import time

import allure

# from constants.constants import Constans
from locators.locators import Selectors
from pages.base_page import BasePage


class FormsPage(BasePage):

    def fill_field_name(self):
        field = self.get_element(Selectors.FIELD_NAME)
        field.click()
        field.clear()
        field.send_keys('name')

    def fill_field_password(self):
        field = self.get_element(Selectors.FIELD_PASSWORD)
        field.click()
        field.clear()
        field.send_keys('password')

    def check_drink_milk(self):
        self.get_element(Selectors.CHECKBOX_MILK).click()

    def check_drink_coffee(self):
        self.get_element(Selectors.CHECKBOX_COFFEE).click()

    def check_color_yellow(self):
        element = self.get_element(Selectors.RADIO_COLOR_YELLOW)
        self.browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        time.sleep(0.5)
        element.click()

    def choice_like_automation(self):
        options = self.get_elements(Selectors.OPTIONS_AUTOMATIONS)
        valid_options = [option for option in options if option.get_attribute("value") != "default"]
        random_option = random.choice(valid_options)
        random_option.click()

    def fill_field_email(self):
        field = self.get_element(Selectors.FIELD_EMAIL)
        self.browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            field
        )
        time.sleep(0.5)
        field.click()
        field.clear()
        field.send_keys('email@mail.ru')

    def fill_field_message(self):
        tools = self.get_elements(Selectors.AUTOMATION_TOOLS)
        number_of_tools = len(tools)
        tools_name = [tool.text for tool in tools]
        longer_tool = max(tools_name, key=len)
        message_field = self.get_element(Selectors.FIELD_MESSAGE)
        self.browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            message_field
        )
        time.sleep(0.5)
        message_field.click()
        message_field.clear()
        message_field.send_keys(number_of_tools)
        message_field.send_keys('\n')
        message_field.send_keys(longer_tool)

    def click_button_submit(self):
        button = self.get_element(Selectors.BUTTON_SUBMIT)
        self.browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )
        button.click()

    def assert_successfull_message_creation(self):
        alert = self.browser.switch_to.alert
        message = alert.text
        self.assert_equals('Message received!', message)
