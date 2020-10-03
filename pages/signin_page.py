from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from pages.dashboard_page import DashboardPage
from pages.page import Page


class SignInWindow(Page):

    #TODO: extract locators
    def fill_form(self, username, password):
        user_name = self.dr.find_element(By.NAME, 'identity')
        user_name.clear()
        user_name.send_keys(username)
        password_field = self.dr.find_element(By.NAME, 'password')
        password_field.clear()
        password_field.send_keys(password)

    def submit_form(self):
        button_sign_in = self.dr.find_element(By.NAME, 'submit')
        button_sign_in.click()
        # Wait dashboard page
        self.wait.until(presence_of_element_located((By.CSS_SELECTOR, ".base_dashboard.active")),
                        message="Dashboard page doesn't open")

        return DashboardPage(self.dr)

