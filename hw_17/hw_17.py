from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''
Оберіть будь-який сайт. повторіть зроблене на лекції для нього. 
+Реалізуйте інстанціювання драйвера через фікстуру, 
Реалізуйте пейдж обжекти, 
додайте базові елементи типу кліку миши, сенд кейс в базовому класі. 
Напишіть 5-10 тестів(можете більше)
'''


def test_01():
    driver = Chrome()
    driver.get('https://muztorg.ua/uk/')
    web_driver_wait = WebDriverWait(driver, 3)
    search_input_locator = "//input[@placeholder='Пошук товару по каталогу']"
    search_input_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_input_locator)))
    search_input_with_wait.send_keys('Fender American')
    search_1st_locator_result = "//div[@class='search-name'][1]"
    search_1st_result_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath',
                                                                                        search_1st_locator_result)))
    assert search_1st_result_with_wait.text == ('FENDER AMERICAN PERFORMER STRATOCASTER '
                                                'MN SATIN LAKE PLACID BLUE Електрогітара')

