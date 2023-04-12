from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(
    "https://learn.microsoft.com/es-es/training/modules/use-automated-machine-learning/")


driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


# main = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, ''))
# )
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       'a.docs-sign-in.auth-status-determined.not-authenticated')))\
    .click()

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.ID,
                                       'otherTileText')))\
    .click()

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.ID,
                                       'i0116')))\
    .send_keys('camsanir@gmail.com')

input("Esperando que no se cierre webdriver: ")
