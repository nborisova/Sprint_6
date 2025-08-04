from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

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

    #клик на блок с ответом 
    def click_dropdown_with_anwser(self, locator):
        self.wait_for_clickable(locator)
        self.driver.find_element(*locator).click()
       
    #шаг для разворота вопроса  
    def open_answer(self, locator):
        self.scroll_down(locator)
        self.wait_for_load_element(locator)
        self.click_dropdown_with_anwser(locator)   

    #проверка текста ответа в дропдауне
    def check_anwser(self, locator, expected_result):
        actual_result = self.driver.find_element(*locator).text
        assert expected_result == actual_result, f'Ожидалось значение: "{expected_result}", получено "{actual_result}"'
    