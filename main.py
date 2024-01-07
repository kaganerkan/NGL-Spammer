import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import string
import time

#Target = str(input("Account to target:\n"))

def system():
    options = Options()
    options.headless = True
    driver = uc.Chrome(options=options)

    def detect_label_and_submit(driver):
        text_box = driver.find_element(By.ID, "question")
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        text_box.send_keys(random_string)
        submit_button = driver.find_element(By.CLASS_NAME, "submit")
        submit_button.click()

    driver.get("https://ngl.link/"+Target)
    driver.maximize_window()

    while True:
        try:
            detect_label_and_submit(driver)
            time.sleep(random.uniform(2, 2.5))
            send_another_link = driver.find_element(By.CLASS_NAME, "another1")
            send_another_link.click()
            time.sleep(random.uniform(2, 2.5))
        except:
            driver.close()
            time.sleep(random.uniform(25,60))
            system()

Target = input("Target:\n")
system()
