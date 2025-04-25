import os
import pytest
import time
from datetime import datetime

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.Login import Login
from PageObjects.Dashboard import Dashboard
from PageObjects.Leave import Leave
from Utilities.Logger import LogGen
from Config import TestConfig


@pytest.mark.usefixtures("setup")
class TestOrangeHRM:
    logger = LogGen.loggen()
    run_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def setUp(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.screenshots_dir = os.path.join(base_dir, "Screenshots", f"test_run_{self.run_timestamp}")
        if not os.path.exists(self.screenshots_dir):
            os.makedirs(self.screenshots_dir)
        self.logger.info(f"Screenshots will be saved in: {self.screenshots_dir}")

    def save_screenshot(self, test_name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if not hasattr(self, 'screenshots_dir'):
            self.setUp()

        path = os.path.join(self.screenshots_dir, f"{test_name}_{timestamp}.png")
        self.driver.save_screenshot(path)
        self.logger.info(f"Screenshot saved: {path}")

    def log_success(self, message):
        self.logger.info(f"SUCCESS: {message} [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")

    def test_01_login_page_title(self):
        self.logger.info("Starting test_01_login_page_title")
        self.driver.get(TestConfig.BASE_URL)
        time.sleep(TestConfig.SLEEP_TIME)
        actual_title = self.driver.title
        expected_title = "OrangeHRM"

        if actual_title == expected_title:
            self.log_success(f"Login page title is correct: {actual_title}")
            self.save_screenshot("test_01_login_page_title")
            assert True
        else:
            self.logger.error(f"❌ Incorrect login page title. Expected: {expected_title}, Got: {actual_title}")
            self.save_screenshot("test_01_login_page_title_failed")
            assert False, f"Expected title: {expected_title}, but got: {actual_title}"

    def test_02_login(self):
        self.logger.info("Starting test_02_login")
        self.driver.get(TestConfig.BASE_URL)
        time.sleep(TestConfig.SLEEP_TIME)

        login_page = Login(self.driver)
        dashboard_page = Dashboard(self.driver)
        login_page.login(TestConfig.USERNAME, TestConfig.PASSWORD)

        if dashboard_page.verify_dashboard_page():
            self.log_success("Login successful and dashboard loaded")
            self.save_screenshot("test_02_login")
            assert True
        else:
            self.logger.error("❌ Dashboard not loaded after login")
            self.save_screenshot("test_02_login_failed")
            assert False, "Dashboard not loaded after login"

    def test_03_leave_functionality(self):
        self.logger.info("Starting test_03_leave_functionality")
        self.driver.get(TestConfig.BASE_URL)

        login_page = Login(self.driver)
        dashboard_page = Dashboard(self.driver)
        leave_page = Leave(self.driver)

        try:
            if login_page.is_on_login_page():
                login_page.login(TestConfig.USERNAME, TestConfig.PASSWORD)
                self.logger.info("Logged in for leave functionality")

            if not dashboard_page.verify_dashboard_page():
                self.logger.error("❌ Dashboard not loaded in leave functionality test")
                self.save_screenshot("test_03_dashboard_not_loaded")
                assert False, "Dashboard not loaded"

            leave_sidebar_item = WebDriverWait(self.driver, TestConfig.WAIT_TIME).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Leave']"))
            )
            leave_sidebar_item.click()
            self.logger.info("Clicked on Leave menu")

            my_leave_tab = WebDriverWait(self.driver, TestConfig.WAIT_TIME).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='My Leave']"))
            )
            my_leave_tab.click()
            self.logger.info("Clicked on My Leave tab")

            WebDriverWait(self.driver, TestConfig.WAIT_TIME).until(
                EC.visibility_of_element_located((By.XPATH, "//h5[text()='My Leave List']"))
            )
            self.logger.info("My Leave page loaded")

            WebDriverWait(self.driver, TestConfig.WAIT_TIME).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-table')]"))
            )

            self.logger.info("Leave page fully loaded")
            self.save_screenshot("test_03_leave_functionality")

            if leave_page.verify_leave_page():
                self.log_success("Leave page loaded and verified")
                assert True
            else:
                self.logger.error("❌ Leave page verification failed")
                self.save_screenshot("test_03_leave_page_verification_failed")
                assert False, "Leave page not verified"

        except TimeoutException as e:
            self.logger.error(f"Timeout in leave functionality test: {str(e)}")
            self.save_screenshot("test_03_leave_functionality_timeout")
            assert False, f"Timeout occurred: {str(e)}"

        except Exception as e:
            self.logger.error(f"Unexpected error in leave functionality test: {str(e)}")
            self.save_screenshot("test_03_leave_functionality_error")
            assert False, f"Unexpected error occurred: {str(e)}"

    def test_04_logout(self):
        self.logger.info("Starting test_04_logout")
        self.driver.get(TestConfig.BASE_URL)

        login_page = Login(self.driver)
        dashboard_page = Dashboard(self.driver)

        try:
            if login_page.is_on_login_page():
                login_page.login(TestConfig.USERNAME, TestConfig.PASSWORD)

            if not dashboard_page.verify_dashboard_page():
                self.logger.error("Dashboard not loaded before logout")
                self.save_screenshot("test_04_dashboard_not_loaded")
                assert False, "Dashboard not loaded"

            time.sleep(TestConfig.SLEEP_TIME)
            dashboard_page.click_logout()

            WebDriverWait(self.driver, TestConfig.WAIT_TIME).until(
                EC.visibility_of_element_located((By.NAME, login_page.txt_username_name))
            )

            assert self.driver.find_element(By.NAME, login_page.txt_username_name).is_displayed(), \
                "Login field not displayed after logout"

            self.log_success("Logout successful and login page displayed")
            self.save_screenshot("test_04_logout")

        except Exception as e:
            self.logger.error(f"Logout test encountered an error: {str(e)}")
            self.save_screenshot("test_04_logout_error")
            assert False, f"Logout test failed: {str(e)}"