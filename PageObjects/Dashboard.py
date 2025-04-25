from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Config import TestConfig

class Dashboard:
    dashboard_header_xpath = "//h6[text()='Dashboard']"
    my_dropdown_xpath = "//li[@class='oxd-userdropdown']//span[contains(@class, 'oxd-userdropdown-tab')]"
    logout_link_xpath = "//a[text()='Logout']"
    leave_menu_xpath = "//span[text()='Leave']/ancestor::a"
    leave_tab_xpath = "//a[contains(@class,'oxd-topbar-body-nav-tab-link') and text()='My Leave']"
    leave_list_header_xpath = "//h5[text()='My Leave List']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, TestConfig.WAIT_TIME)

    def verify_dashboard_page(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.dashboard_header_xpath)))
            return True
        except TimeoutException:
            return False

    def click_leave(self):
        try:
            my_leave_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.leave_tab_xpath))
            )
            my_leave_element.click()
        except TimeoutException:
            print("My Leave tab not clickable or not found.")
        except Exception as e:
            print(f"Error while clicking 'My Leave': {str(e)}")

    def click_logout(self):
        try:
            user_dropdown = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.my_dropdown_xpath))
            )
            user_dropdown.click()
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//ul[@class='oxd-dropdown-menu']"))
            )
            logout_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.logout_link_xpath))
            )
            logout_link.click()
            self.wait.until(EC.url_contains("auth/login"))

        except Exception as e:
            print(f"Error during logout: {str(e)}")
            raise