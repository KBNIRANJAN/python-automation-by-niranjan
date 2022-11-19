from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService
from time import sleep


def TC_Login_01():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(5)
    # To enter username and password
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    sleep(3)
    # To click on login button
    l = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
    l.click();
    sleep(5)
    # Expected result
    print('The user is logged in successfully.')


TC_Login_01()
