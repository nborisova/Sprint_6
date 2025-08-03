from selenium import webdriver
from pages.form_page import FormPage
import pytest
import allure


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
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка верхней кнопки оформления заказа')
    @allure.description('Пользователь нажимает на кнопку и переходит к форме заказа')
    def test_check_top_order_button(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        form_page = FormPage(self.driver)
        order_button_top = form_page.order_button_top
        form_title = form_page.form_title
        form_page.check_top_order_button(order_button_top, form_title, 'Для кого самокат')

    @allure.title('Проверка нижней кнопки оформления заказа')
    @allure.description('Пользователь нажимает на кнопку и переходит к форме заказа')
    def test_check_middle_order_button(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        form_page = FormPage(self.driver)
        logo_scooter = form_page.logo_scooter
        form_page.close_cookie_banner()
        order_button_middle = form_page.order_button_middle
        form_title = form_page.form_title
        form_page.check_middle_order_button(logo_scooter, order_button_middle, form_title, 'Для кого самокат')

    @allure.title('Проверка успешного оформления заказа самоката')
    @allure.description('Пользователь заполняет форму и оформляет заказ')
    @pytest.mark.parametrize('data', data)
    def test_check_order_form(self, data):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')  

        form_page = FormPage(self.driver)
        order_button_top = form_page.order_button_top
        form_page.click_element(order_button_top)
        form_page.close_cookie_banner()
        form_page.fill_order_form(data)
        order_placed_title = self.driver.find_element(*form_page.order_placed_title).text

        assert 'Заказ оформлен' in order_placed_title

    @allure.title('Проверка кнопок логотипа')
    @allure.description('Пользователь нажимает на логотип в хедере и переходит на соответствующий url')
    @pytest.mark.parametrize('locator, expected_url', [
        ['logo_scooter', 'https://qa-scooter.praktikum-services.ru/'],
        ['logo_yandex', 'https://dzen.ru']
    ])
    def test_check_logo(self, locator, expected_url):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')  

        form_page = FormPage(self.driver)
        form_page.close_cookie_banner()
        locator_name = getattr(form_page, locator)
        form_page.check_logo(locator_name, expected_url)        

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()