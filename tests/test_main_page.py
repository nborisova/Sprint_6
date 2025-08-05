from selenium import webdriver
from pages.main_page import MainPage
import allure
from utils.constants import BASE_URL

class TestMainPage:

    @allure.title('Проверка текста в выпадающем списке')
    @allure.description('Вопрос о стоимости и оплате')
    def test_answer_to_question_cost(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(BASE_URL)
        main_page.close_cookie_banner()
        locator_question_cost = main_page.question_cost
        locator_answer_cost = main_page.answer_cost
        main_page.open_answer(locator_question_cost)
        main_page.check_anwser(locator_answer_cost, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')

    @allure.title('Проверка текста в выпадающем списке')
    @allure.description('Вопрос о возможности проката нескольких самокатов')
    def test_answer_to_question_get_several_scooters (self, driver):
        main_page = MainPage(driver)
        main_page.open_page(BASE_URL)
        main_page.close_cookie_banner()
        locator_question_get_several_scooters = main_page.question_get_several_scooters
        locator_answer_get_several_scooters = main_page.answer_get_several_scooters
        main_page.open_answer(locator_question_get_several_scooters)
        main_page.check_anwser(locator_answer_get_several_scooters, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься ' \
        'с друзьями, можете просто сделать несколько заказов — один за другим.')

    @allure.title('Проверка текста в выпадающем списке')
    @allure.description('Вопрос о времени аренды')
    def test_answer_to_question_time_for_rent (self, driver):
        main_page = MainPage(driver)
        main_page.open_page(BASE_URL)
        main_page.close_cookie_banner()
        locator_question_time_for_rent = main_page.question_time_for_rent
        locator_answer_time_for_rent = main_page.answer_time_for_rent
        main_page.open_answer(locator_question_time_for_rent)
        main_page.check_anwser(locator_answer_time_for_rent, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. ' \
        'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, ' \
        'суточная аренда закончится 9 мая в 20:30.')

    @allure.title('Проверка текста в выпадающем списке')
    @allure.description('Вопрос о заказе на сегодня')
    def test_answer_to_question_order_today (self, driver):
        main_page = MainPage(driver)
        main_page.open_page(BASE_URL)
        main_page.close_cookie_banner()
        locator_question_order_today = main_page.question_order_today
        locator_answer_order_today = main_page.answer_order_today
        main_page.open_answer(locator_question_order_today)
        main_page.check_anwser(locator_answer_order_today, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')

    @allure.title('Проверка текста в выпадающем списке')
    @allure.description('Вопрос о продлении заказа и возврате')
    def test_answer_to_question_extend_or_return_scooter (self, driver):
        main_page = MainPage(driver)
        main_page.open_page(BASE_URL)
        main_page.close_cookie_banner()
        locator_question_extend_or_return_scooter = main_page.question_extend_or_return_scooter
        locator_answer_extend_or_return_scooter = main_page.answer_extend_or_return_scooter
        main_page.open_answer(locator_question_extend_or_return_scooter)
        main_page.check_anwser(locator_answer_extend_or_return_scooter, 'Пока что нет! Но если что-то срочное — всегда можно позвонить ' \
        'в поддержку по красивому номеру 1010.')

    @allure.title('Проверка текста в выпадающем списке')
    @allure.description('Вопрос о зарядке для самоката')
    def test_answer_to_question_get_charger (self, driver):
        main_page = MainPage(driver)
        main_page.open_page(BASE_URL)
        main_page.close_cookie_banner()
        locator_question_get_charger = main_page.question_get_charger
        locator_answer_get_charger = main_page.answer_get_charger
        main_page.open_answer(locator_question_get_charger)
        main_page.check_anwser(locator_answer_get_charger, 'Самокат приезжает к вам с полной зарядкой. ' \
        'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.') 

    @allure.title('Проверка текста в выпадающем списке')
    @allure.description('Вопрос об отмене заказа')
    def test_answer_to_question_cancel_order (self, driver):
        main_page = MainPage(driver)
        main_page.open_page(BASE_URL)
        main_page.close_cookie_banner()
        locator_question_cancel_order = main_page.question_cancel_order
        locator_answer_cancel_order = main_page.answer_cancel_order
        main_page.open_answer(locator_question_cancel_order)
        main_page.check_anwser(locator_answer_cancel_order, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. ' \
        'Все же свои.')

    @allure.title('Проверка текста в выпадающем списке')
    @allure.description('Вопрос о доставке за МКАД')
    def test_answer_to_question_delivery_out_of_city (self, driver):
        main_page = MainPage(driver)
        main_page.open_page(BASE_URL)
        main_page.close_cookie_banner()
        locator_question_delivery_out_of_city = main_page.question_delivery_out_of_city
        locator_answer_delivery_out_of_city = main_page.answer_delivery_out_of_city
        main_page.open_answer(locator_question_delivery_out_of_city)
        main_page.check_anwser(locator_answer_delivery_out_of_city, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
