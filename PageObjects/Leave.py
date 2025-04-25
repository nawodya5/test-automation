from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Config import TestConfig


class Leave:
    def __init__(self, driver):
        self.driver = driver

    def verify_leave_page(self):
        try:
            time.sleep(TestConfig.SLEEP_TIME)
            WebDriverWait(self.driver, TestConfig.WAIT_TIME).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/web/index.php/leave/viewLeaveModule']"))
            ).click()
            return True
        except:
            return False
