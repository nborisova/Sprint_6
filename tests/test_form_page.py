from pages.form_page import FormPage
import pytest
import allure
from utils.constants import BASE_URL, YANDEX_URL


data = [
        {
            'name': 'Алексей',
            'surname': 'Иванов',
            'address': 'ул. Ленина, 10',
            'metro': 'Черкизовская',
            'phone': '89995553322',
            'delivery_date': '31.07.2025',
            'rental_period': 'сутки',
            'scooter_color': 'black',
        },
        {
            'name': 'Мария',
            'surname': 'Петрова',
            'address': 'пр-т Мира, 23',
            'metro': 'Сокольники',
            'phone': '89991112233',
            'delivery_date': '01.08.2025',
            'rental_period': 'двое суток',
            'scooter_color': 'grey',
        }
    ]

class TestFormPage:

    @allure.title('Проверка верхней кнопки оформления заказа')
    @allure.description('Пользователь нажимает на кнопку и переходит к форме заказа')
    def test_check_top_order_button(self, driver):
        form_page = FormPage(driver)
        form_page.open_page(BASE_URL)
        order_button_top = form_page.order_button_top
        form_title = form_page.form_title
        form_page.check_top_order_button(order_button_top, form_title, 'Для кого самокат')

    @allure.title('Проверка нижней кнопки оформления заказа')
    @allure.description('Пользователь нажимает на кнопку и переходит к форме заказа')
    def test_check_middle_order_button(self, driver):
        form_page = FormPage(driver)
        form_page.open_page(BASE_URL)
        logo_scooter = form_page.logo_scooter
        form_page.close_cookie_banner()
        order_button_middle = form_page.order_button_middle
        form_title = form_page.form_title
        form_page.check_middle_order_button(logo_scooter, order_button_middle, form_title, 'Для кого самокат')

    @allure.title('Проверка успешного оформления заказа самоката')
    @allure.description('Пользователь заполняет форму и оформляет заказ')
    @pytest.mark.parametrize('data', data)
    def test_check_order_form(self, driver, data):
        form_page = FormPage(driver)
        form_page.open_page(BASE_URL)
        order_button_top = form_page.order_button_top
        form_page.click_element(order_button_top)
        form_page.close_cookie_banner()
        form_page.fill_order_form(data)
        order_placed_title = driver.find_element(*form_page.order_placed_title).text

        assert 'Заказ оформлен' in order_placed_title

    @allure.title('Проверка кнопок логотипа')
    @allure.description('Пользователь нажимает на логотип в хедере и переходит на соответствующий url')
    @pytest.mark.parametrize('locator, expected_url', [
        ['logo_scooter', BASE_URL],
        ['logo_yandex', YANDEX_URL]
    ])
    def test_check_logo(self, driver, locator, expected_url):
        form_page = FormPage(driver)
        form_page.open_page(BASE_URL)
        form_page.close_cookie_banner()
        locator_name = getattr(form_page, locator)
        form_page.check_logo(locator_name, expected_url)        
