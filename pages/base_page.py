from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


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
