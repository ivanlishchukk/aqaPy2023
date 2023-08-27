from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import re


def test_01_cv_placement_page():
    driver = Chrome()
    driver.get('https://google.com')
    time.sleep(1)

    locator = "//textarea[@type='search']"
    element = driver.find_element(by='xpath', value=locator)
    element.send_keys('work ua')
    time.sleep(1)

    element.send_keys(Keys.ENTER)
    time.sleep(1)

    first_link = "//h3[contains(text(),'Work.ua — сайт пошуку роботи №1 в Україні')]"
    first_link = driver.find_element(by='xpath', value=first_link)
    first_link.click()
    time.sleep(1)

    place_cv_button = "//a[@id='resumeCreate']"
    place_cv = driver.find_element(by='xpath', value=place_cv_button)
    place_cv.click()
    time.sleep(1)

    label_page_cv = "//h1[@id='login']"
    label_cv = driver.find_element(by='xpath', value=label_page_cv)
    assert label_cv.text == "Створіть найкраще резюме в Україні"


def test_02_qa_job_search():
    driver = Chrome()
    driver.get('https://google.com')
    time.sleep(1)

    locator = "//textarea[@type='search']"
    element = driver.find_element(by='xpath', value=locator)
    element.send_keys('work ua')
    time.sleep(1)

    element.send_keys(Keys.ENTER)
    time.sleep(1)

    first_link = "//h3[contains(text(),'Work.ua — сайт пошуку роботи №1 в Україні')]"
    first_link = driver.find_element(by='xpath', value=first_link)
    first_link.click()
    time.sleep(1)

    search_field = "//input[@id='search']"
    search_input = driver.find_element(by='xpath', value=search_field)
    search_input.send_keys('Qa')
    time.sleep(1)

    region_field = "//input[@placeholder='Місто']"
    search_input = driver.find_element(by='xpath', value=region_field)
    search_input.click()
    action = ActionChains(driver)
    action.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
    time.sleep(2)
    action.key_down(Keys.COMMAND).send_keys('x').key_up(Keys.COMMAND).perform()
    time.sleep(2)
    search_input.send_keys('Вся Україна')
    search_input.click()
    time.sleep(1)

    find_job_button = "//button[@id='sm-but']"
    find_job = driver.find_element(by='xpath', value=find_job_button)
    find_job.click()
    time.sleep(1)

    label_page_h1 = "//h1"
    label_fender = driver.find_element(by='xpath', value=label_page_h1)
    assert label_fender.text == "Qa"
    time.sleep(5)


def test_03_qa_job_filter_by_date():
    driver = Chrome()
    driver.get('https://google.com')
    time.sleep(1)

    locator = "//textarea[@type='search']"
    element = driver.find_element(by='xpath', value=locator)
    element.send_keys('work ua')
    time.sleep(1)

    element.send_keys(Keys.ENTER)
    time.sleep(1)

    first_link = "//h3[contains(text(),'Work.ua — сайт пошуку роботи №1 в Україні')]"
    first_link = driver.find_element(by='xpath', value=first_link)
    first_link.click()
    time.sleep(1)

    search_field = "//input[@id='search']"
    search_input = driver.find_element(by='xpath', value=search_field)
    search_input.send_keys('Qa')
    time.sleep(1)

    region_field = "//input[@placeholder='Місто']"
    search_input = driver.find_element(by='xpath', value=region_field)
    search_input.click()
    action = ActionChains(driver)
    action.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
    time.sleep(2)
    action.key_down(Keys.COMMAND).send_keys('x').key_up(Keys.COMMAND).perform()
    time.sleep(2)
    search_input.send_keys('Вся Україна')
    search_input.click()
    time.sleep(1)

    find_job_button = "//button[@id='sm-but']"
    find_job = driver.find_element(by='xpath', value=find_job_button)
    find_job.click()
    time.sleep(1)

    result_for_default_filter = "//*[@id='pjax-job-list']/div[1]/div[1]/div[1]/div"
    result_1 = driver.find_element(by='xpath', value=result_for_default_filter)
    res_1 = result_1.text
    res_1 = int(re.search(r"\d+", res_1).group())
    time.sleep(1)

    filter_button = "//span[@class='glyphicon glyphicon-sort-left glyph-indent']"
    filter_button_click = driver.find_element(by='xpath', value=filter_button)
    filter_button_click.click()
    time.sleep(1)

    filter_option = "// a[contains(text(), 'За 7 днів')]"
    set_filter = driver.find_element(by='xpath', value=filter_option)
    set_filter.click()
    time.sleep(1)

    result_for_default_filter = "//*[@id='pjax-job-list']/div[1]/div[1]/div[1]/div"
    result_2 = driver.find_element(by='xpath', value=result_for_default_filter)
    res_2 = result_2.text
    res_2 = int(re.search(r"\d+", res_2).group())

    assert res_2 < res_1


def test_04_job_advanced_filters():
    driver = Chrome()
    driver.get('https://google.com')
    time.sleep(1)

    locator = "//textarea[@type='search']"
    element = driver.find_element(by='xpath', value=locator)
    element.send_keys('work ua')
    time.sleep(1)

    element.send_keys(Keys.ENTER)
    time.sleep(1)

    first_link = "//h3[contains(text(),'Work.ua — сайт пошуку роботи №1 в Україні')]"
    first_link = driver.find_element(by='xpath', value=first_link)
    first_link.click()
    time.sleep(1)

    advanced_search_button = "//a[contains(text(),'Розширений пошук')]"
    advanced_search = driver.find_element(by='xpath', value=advanced_search_button)
    advanced_search.click()
    time.sleep(1)

    cat_expand_button = "// a[ @ id = 'cat_more']"
    cat_expand = driver.find_element(by='xpath', value=cat_expand_button)
    cat_expand.click()
    time.sleep(1)

    cat_checkbox = "//*[@id='category_selection']/div[11]/label/input"
    cat_checkbox_click = driver.find_element(by='xpath', value=cat_checkbox)
    cat_checkbox_click.click()
    time.sleep(1)

    salary_from_option = "//select[@class='form-control']/option[@value='7']"
    salary_from_choose = driver.find_element(by='xpath', value=salary_from_option)
    salary_from_choose.click()
    time.sleep(1)

    clear_filters_button = "//a[@class='filter-reset']"
    clear_filters = driver.find_element(by='xpath', value=clear_filters_button)
    clear_filters.click()
    time.sleep(3)

    try:
        filter_block = "//div[@class='card filter-labels']"
        find_filter_block = driver.find_element(by='xpath', value=filter_block)
        check_filter = 'Present'
    except:
        check_filter = 'Does not exist'

    assert check_filter == 'Does not exist'


def test_05_language_change():
    driver = Chrome()
    driver.get('https://google.com')
    time.sleep(1)

    locator = "//textarea[@type='search']"
    element = driver.find_element(by='xpath', value=locator)
    element.send_keys('work ua')
    time.sleep(1)

    element.send_keys(Keys.ENTER)
    time.sleep(1)

    first_link = "//h3[contains(text(),'Work.ua — сайт пошуку роботи №1 в Україні')]"
    first_link = driver.find_element(by='xpath', value=first_link)
    first_link.click()
    time.sleep(1)

    language_dropdown = "//a[@id='dropdownMenu100-2']"
    language_dropdown_open = driver.find_element(by='xpath', value=language_dropdown)
    language_dropdown_open.click()
    time.sleep(2)

    language_en = "//ul[@id='header-language-switcher-list']//a[normalize-space()='English']"
    language_en_select = driver.find_element(by='xpath', value=language_en)
    language_en_select.click()
    time.sleep(2)

    en_h1 = "//h1"
    language_en_select = driver.find_element(by='xpath', value=en_h1)
    result = language_en_select.text
    assert result == "Ukraine's #1 job site"








