from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import yaml
from selenium.webdriver.common.by import By
import requests, time

conf = yaml.load(open('det.yml'))
userName = conf['lms_user']['username']
password = conf['lms_user']['password']
# url = 'http://20.20.0.1:1000/login?0076a5c596850997'
# url = 'http://172.16.222.1:1000/fgtauth?0073c8c331dae227'
url = 'https://lmsone.iiitkottayam.ac.in'
subject_url = 'https://lmsone.iiitkottayam.ac.in/course/view.php?id=282'


def login(url, uid, username, pid, password, submitid):
    notes_path = r"D:\new folder\Sem_8\Applied Predictive Analysis\Notes"
    options = webdriver.ChromeOptions()
    chrome_prefs = {
        "download.prompt_for_download": False,
        "plugins.always_open_pdf_externally": True,
        "download.open_pdf_in_system_reader": False,
        "profile.default_content_settings.popups": 0,
        "download.default_directory": notes_path
    }
    options.add_experimental_option("prefs", chrome_prefs)
    driver = webdriver.Chrome(options=options)

    # Login
    # driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, uid).send_keys(username)
    driver.find_element(By.XPATH, pid).send_keys(password)
    driver.find_element(By.XPATH, submitid).click()

    # Subject page
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@data-course-id="282"]')))
    driver.find_element(By.XPATH, '//div[@data-course-id="282"]').click()
    all_notes = driver.find_elements(By.XPATH, '//li[@id="section-1"]//a')[1:]
    notes_itr = [ i.get_attribute('href') for i in all_notes]


    # Note download
    for link in notes_itr:
        driver.get(link)
        driver.get(driver.current_url)
    


def checkNotes():
    driver = webdriver.Chrome()
    driver.get(subject_url)

    all_notes = driver.find_element(By.XPATH, '//li[@id="section-1"]')
    print(len(all_notes))


# def upDateNotes():


login(
    url,
    '//form[@class="form-inline my-2 my-lg-0"]//input[@type="text"]', userName,
    '//form[@class="form-inline my-2 my-lg-0"]//input[@type="password"]', password,
    '//form[@class="form-inline my-2 my-lg-0"]//button'
)
# checkNotes()