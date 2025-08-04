from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def close_cookie_banner(self):
        try:
            self.driver.find_element(By.ID, 'rcc-confirm-button').click()
        except Exception:
            pass  

    #скролл до элемента
    def scroll_down(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)   

    #дождаться загрузки блока 
    def wait_for_load_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    #дождаться кликабельности элемента 
    def wait_for_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))     
    
    #клик на элемент 
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    #заполнение полей данными
    def enter_data(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)

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