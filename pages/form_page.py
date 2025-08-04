from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
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

