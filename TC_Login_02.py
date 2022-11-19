from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService
from time import sleep


def TC_Login_02():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    sleep(5)
    # To enter username and password
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("Invalid password")
    sleep(3)
    # To click on login button
    l = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
    l.click();
    sleep(4)
    # A valid error message for invalid credentials
    print('Invalid credentials,login with correct credentials')


TC_Login_02()
