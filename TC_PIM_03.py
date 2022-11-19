from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService
from time import sleep


def TC_PIM_03():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(5)
    # For user login
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    l = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
    l.click();
    sleep(3)
    # To go to PIM
    m = driver.find_element(By.LINK_TEXT, 'PIM')
    m.click();
    sleep(2)
    # To delete an existing employee
    p = driver.find_element(By.XPATH, value="//*[@class='oxd-icon-button oxd-table-cell-action-space'][1]")
    p.click();
    sleep(2)
    # Final confirmation to delete an existing employee
    q = driver.find_element(By.XPATH, value="//*[@class='oxd-button oxd-button--medium oxd-button--label-danger "
                                            "orangehrm-button-margin']")

    q.click();
    sleep(3)
    print('deleted an existing employee in the PIM and see a message successfully deleted')


TC_PIM_03()
