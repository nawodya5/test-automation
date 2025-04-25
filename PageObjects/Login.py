from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Config import TestConfig

class Login:
    txt_username_name = "username"
    txt_password_name = "password"
    btn_login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, TestConfig.WAIT_TIME)

    def set_username(self, username):
        try:
            time.sleep(2)
            username_element = self.wait.until(
                EC.visibility_of_element_located((By.NAME, self.txt_username_name))
            )
            username_element.clear()
            username_element.send_keys(username)
        except Exception as e:
            try:
                username_element = self.wait.until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
                )
                username_element.clear()
                username_element.send_keys(username)
            except Exception as e:
                print(f"Failed with alternative selector too: {str(e)}")
                raise

    def set_password(self, password):
        try:
            time.sleep(2)
            password_element = self.wait.until(
                EC.visibility_of_element_located((By.NAME, self.txt_password_name))
            )
            password_element.clear()
            password_element.send_keys(password)
        except Exception as e:
            password_element = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
            )
            password_element.clear()
            password_element.send_keys(password)

    def click_login(self):
        try:
            time.sleep(2)
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.btn_login_xpath))
            )
            login_button.click()
        except Exception as e:
            # Try alternative approach
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )
            login_button.click()

    def login(self, username, password):
        if "login" not in self.driver.current_url:
            self.driver.get(TestConfig.BASE_URL)
            time.sleep(2)

        self.set_username(username)
        self.set_password(password)
        self.click_login()
        time.sleep(2)

    def is_on_login_page(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.NAME, self.txt_username_name))
            )
            return True
        except:
            return False