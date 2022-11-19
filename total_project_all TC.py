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
