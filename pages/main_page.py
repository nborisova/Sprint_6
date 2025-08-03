from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:

    question_cost = [By.ID, 'accordion__heading-0']
    answer_cost = [By.XPATH, './/div[@id="accordion__panel-0"]/p']

    question_get_several_scooters = [By.ID, 'accordion__heading-1']
    answer_get_several_scooters = [By.XPATH, './/div[@id="accordion__panel-1"]/p']

    question_time_for_rent = [By.ID, 'accordion__heading-2']
    answer_time_for_rent = [By.XPATH, './/div[@id="accordion__panel-2"]/p']

    question_order_today = [By.ID, 'accordion__heading-3']
    answer_order_today  = [By.XPATH, './/div[@id="accordion__panel-3"]/p']

    question_extend_or_return_scooter = [By.ID, 'accordion__heading-4']
    answer_extend_or_return_scooter = [By.XPATH, './/div[@id="accordion__panel-4"]/p']

    question_get_charger = [By.ID, 'accordion__heading-5']
    answer_get_charger  = [By.XPATH, './/div[@id="accordion__panel-5"]/p']

    question_cancel_order = [By.ID, 'accordion__heading-6']
    answer_cancel_order = [By.XPATH, './/div[@id="accordion__panel-6"]/p']

    question_delivery_out_of_city = [By.ID, 'accordion__heading-7']
    answer_delivery_out_of_city = [By.XPATH, './/div[@id="accordion__panel-7"]/p']

    def __init__(self, driver):
        self.driver = driver

    #закрытие баннера с куками
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
    def wait_for_load_questions_block(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    #дождаться кликабельности элемента 
    def wait_for_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))    
        
    #клик на блок с ответом 
    def click_dropdown_with_anwser(self, locator):
        self.wait_for_clickable(locator)
        self.driver.find_element(*locator).click()
       
    #шаг для разворота вопроса  
    def open_answer(self, locator):
        self.scroll_down(locator)
        self.wait_for_load_questions_block(locator)
        self.click_dropdown_with_anwser(locator)   

    #проверка текста ответа в дропдауне
    def check_anwser(self, locator, expected_result):
        actual_result = self.driver.find_element(*locator).text
        assert expected_result == actual_result, f'Ожидалось значение: "{expected_result}", получено "{actual_result}"'
    