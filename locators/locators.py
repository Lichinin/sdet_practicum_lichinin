from selenium.webdriver.common.by import By


class Selectors:

    FIELD_NAME = (By.ID, 'name-input')
    FIELD_PASSWORD = (By.CSS_SELECTOR, 'input[type="password"]')
    CHECKBOX_MILK = (By.CSS_SELECTOR, 'input[value="Milk"]')
    CHECKBOX_COFFEE = (By.CSS_SELECTOR, 'input[value="Coffee"]')
    RADIO_COLOR_YELLOW = (By.ID, 'color3')
    OPTIONS_AUTOMATIONS = (By.XPATH, '//select[@id="automation"]/option')
    FIELD_EMAIL = (By.ID, 'email')
    AUTOMATION_TOOLS = (
        By.XPATH,
        '//label[text()="Automation tools"]/following-sibling::ul[1]/li'
    )
    FIELD_MESSAGE = (By.ID, 'message')
    BUTTON_SUBMIT = (By.ID, 'submit-btn')
