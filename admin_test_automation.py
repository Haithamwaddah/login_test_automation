import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

# Valid Test Scenarios

try:

    url = "https://qa-test-frontend-ce07bae316f3.herokuapp.com/"
    driver.get(url)
    driver.maximize_window()

    # Fill in the username and password fields
    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    username_field.send_keys("blinktester")
    password_field.send_keys("BLink#qA@23")

    # Click the Login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Wait for the "Skip" button to be clickable
    wait = WebDriverWait(driver, 10)
    skip_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[5]/main/div/div/form/div/div[3]/button')))
    skip_button.click()

    home_url = "https://qa-test-frontend-ce07bae316f3.herokuapp.com/"
    driver.get(home_url)

    time.sleep(10)

    blinktester_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[5]/header/div/div[3]/div[2]/div/button/div/span')
    blinktester_button.click()

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[5]/header/div/div[3]/div[2]/div/div/div/div/button/div')))

    logout_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[5]/header/div/div[3]/div[2]/div/div/div/div/button/div')
    logout_button.click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))

except Exception as e:
    print("An error occurred:", str(e))

    driver.quit()

    exit()

# Negative Test Scenarios
try:
    invalid_login_url = "https://qa-test-frontend-ce07bae316f3.herokuapp.com/"
    driver.get(invalid_login_url)

    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))

    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    username_field.send_keys("invalidusername")
    password_field.send_keys("invalidpassword")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # ASSERTION: Verify error message for invalid login
    error_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='MuiAlert-message']")))
    assert "Invalid" in error_message.text, "Error message for invalid login not displayed"

    print("All test cases passed!")

    time.sleep(5)

except Exception as e:
    print("An error occurred:", str(e))

finally:
    driver.quit()
