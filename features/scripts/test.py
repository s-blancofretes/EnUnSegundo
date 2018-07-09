from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utils import webdriverutils as utils


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
utils.wait_for_element_id(driver, "pane-side")
print("Whatsapp main page is loaded")

running = True
while running:
    print("Running program loop")
    contact_pane = driver.find_element_by_id("pane-side")
    contacts = contact_pane.find_elements_by_class_name("_3j7s9")
    print("Number of obtained contacts: " + str(len(contacts)))
    for contact in contacts:
        title = str(contact.find_element_by_class_name("_1wjpf").get_attribute("title"))
        print(title)
        contact.click()
        utils.wait_for_element_xpath(driver, "//header[@class='_3AwwN']//span[contains(text(),'" + title + "')]")

    running = False



