import allure

from constants.constants import Constants


@allure.epic('SimbirSoft SDET practicum')
@allure.suite('UI tests')
@allure.title('Тест заполнения форм')
def test_form_filling(forms_page):
    page = forms_page
    page.fill_field_name(Constants.NAME)
    page.fill_field_password(Constants.PASSWORD)
    page.check_drink_milk()
    page.check_drink_coffee()
    page.check_color_yellow()
    page.choice_like_automation()
    page.fill_field_email(Constants.EMAIL)
    page.fill_field_message()
    page.click_button_submit()
    page.assert_successfull_message_creation()
