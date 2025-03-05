import allure


@allure.epic('SimbirSoft SDET practicum')
@allure.suite('UI tests')
@allure.title('Тест заполнения форм')
def test_form_filling(open_test_page):
    page = open_test_page
    page.fill_field_name()
    page.fill_field_password()
    page.check_drink()
    page.check_color()
    page.choice_like_automation()
    page.fill_field_email()
    page.fill_field_message()
    page.click_button_submit()
    page.assert_successfull_message_creation()