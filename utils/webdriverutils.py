from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def wait_for_element_class_name(driver, name):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, name)))
        return element

    except:
        print("The element was not found")
        driver.quit()

def wait_for_element_xpath(driver, xpath):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        return element

    except:
        print("The element was not found")
        driver.quit()

def wait_for_element_id(driver, id):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, id)))
        return element

    except:
        print("The element was not found")
        driver.quit()
