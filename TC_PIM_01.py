from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService
from time import sleep


def TC_PIM_01():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    sleep(5)
    # For user login
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    sleep(3)
    l = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
    l.click();
    sleep(5)
    # To click on PIM
    m = driver.find_element(By.LINK_TEXT, 'PIM')
    m.click();
    sleep(3)
    # To click on AddEmployee and to fill the employee details
    n = driver.find_element(By.LINK_TEXT, 'Add Employee')
    n.click();
    sleep(3)
    driver.find_element(By.NAME, "firstName").send_keys("niranjan")
    driver.find_element(By.NAME, "lastName").send_keys("gg")
    # To click on save
    o = driver.find_element(By.XPATH, value="//button[@type='submit']")
    o.click();
    sleep(3)
    # Expected result
    print('added a new employee in the PIM and see a message successfully saved')


TC_PIM_01()
