from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.constants import YANDEX_URL


class FormPage(BasePage):

    logo_yandex = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    logo_scooter = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']

    order_button_top = [By.CLASS_NAME, 'Button_Button__ra12g']
    order_button_middle = [By.CSS_SELECTOR, '.Button_Button__ra12g.Button_Middle__1CSJM']
    next_button = [By.XPATH, './/button[text()="Далее"]']
    complete_order_button = [By.XPATH, './/div[contains(@class, "Order_Buttons__1xGrp")]/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']
    order_confirmation_button = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]']

    form_title = [By.XPATH, './/div[text()="Для кого самокат"]']
    name_field = [By.XPATH, './/input[@placeholder="* Имя"]']
    surname_field = [By.XPATH, './/input[@placeholder="* Фамилия"]']
    address_field = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
    metro_field = [By.XPATH, './/input[@placeholder="* Станция метро"]']
    phone_field = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']
    delivery_date_field = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
    rental_period_field = [By.CLASS_NAME, 'Dropdown-placeholder']

    order_placed_title = [By.XPATH, './/div[text()="Заказ оформлен"]']

    #проверка работы верхней кнопки заказа
    def check_top_order_button(self, button, form_title, expected_result):
        self.click_element(button)
        actual_result = self.driver.find_element(*form_title).text

        assert actual_result == expected_result, f'Ожидалось значение: "{expected_result}", получено "{actual_result}"'

    #проверка работы нижней кнопки заказа
    def check_middle_order_button(self, logo_scooter, button, form_title, expected_result):
        self.click_element(logo_scooter)
        self.wait_for_load_element(button)
        self.click_element(button)
        actual_result = self.driver.find_element(*form_title).text

        assert actual_result == expected_result, f'Ожидалось значение: "{expected_result}", получено "{actual_result}"'

    #проверка нажатия на оба лого
    def check_logo(self, locator, expected_url):
        self.click_element(locator)

        if YANDEX_URL in expected_url:
            WebDriverWait(self.driver, 5).until(lambda d: len(d.window_handles) > 1)
            self.driver.switch_to.window(self.driver.window_handles[1])

        WebDriverWait(self.driver, 10).until(lambda d: expected_url in d.current_url)

        assert expected_url in self.driver.current_url

    #заполнение формы данными
    def fill_order_form(self, data):
        self.enter_data(self.name_field, data['name'])
        self.enter_data(self.surname_field, data['surname'])
        self.enter_data(self.address_field, data['address'])
        self.click_element(self.metro_field)
        metro_input = self.driver.find_element(*self.metro_field)
        metro_input.send_keys(data["metro"])
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)
        self.wait_for_load_element(self.phone_field)
        self.enter_data(self.phone_field, data['phone'])

        self.click_element(self.next_button)

        self.enter_data(self.delivery_date_field, data['delivery_date'])
        form_title = self.driver.find_element(By.XPATH, './/div[text()="Про аренду"]')
        form_title.click()
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, 'react-datepicker__month-container')))
        self.scroll_down(self.rental_period_field)
        self.click_element(self.rental_period_field)
        rental_period_option = [By.XPATH, f'.//div[@class="Dropdown-option" and text()="{data["rental_period"]}"]']
        self.click_element(rental_period_option)
        scooter_color_option = [By.ID, f'{data["scooter_color"]}']
        self.click_element(scooter_color_option)

        self.click_element(self.complete_order_button)
        self.click_element(self.order_confirmation_button)