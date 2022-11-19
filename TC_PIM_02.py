from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService
from time import sleep


def TC_PIM_02():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(5)
    # For user login
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    sleep(3)
    l = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
    l.click();
    sleep(5)
    m = driver.find_element(By.LINK_TEXT, 'PIM')
    m.click();
    sleep(2)
    # To edit the employee information
    p = driver.find_element(By.XPATH, value="//*[@class='oxd-icon-button oxd-table-cell-action-space'][2]")
    p.click();
    sleep(2)
    driver.find_element(By.NAME, "middleName").send_keys("bala")
    # To click on save
    q = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
    q.click();
    sleep(3)
    # Expected result
    print('edited an existing employee information in the PIM and see a message successfully updated')


TC_PIM_02()
