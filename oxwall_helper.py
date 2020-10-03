from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from custom_wait_condition import presence_of_N_elements_located
from pages.locators import POST_TEXT_FIELD, SEND_BUTTON


class OxwallSite:
    def __init__(self, dr):
        self.dr = dr
        self.wait = WebDriverWait (dr, 5)

    def wait_new_post(self, number_of_posts):
        # Wait new post appears
        # posts = wait.until(presence_of_2_elements_located)
        posts = self.wait.until(
            presence_of_N_elements_located((By.CSS_SELECTOR, ".ow_newsfeed_content"), number_of_posts + 1))
        # posts = dr.find_elements(By.CSS_SELECTOR, ".ow_newsfeed_content")
        # len(posts) == number_of_posts + 1
        return posts

    def create_new_post(self, input_text):
        # Create new post
        # new_post_text = dr.find_element(By.NAME, "status")
        new_post_text = self.wait.until(presence_of_element_located(POST_TEXT_FIELD), message="Post text doesn't appere")
        new_post_text.clear()
        new_post_text.send_keys(input_text)
        send_button = self.dr.find_element(*SEND_BUTTON)
        send_button.click()

    def count_posts(self):
        # Count posts
        posts = self.dr.find_elements(By.CSS_SELECTOR, ".ow_newsfeed_content")
        number_of_posts = len(posts)
        return number_of_posts

    def login_as(self, username, password):
        # Login
        sign_in_menu = self.dr.find_element(By.CLASS_NAME, 'ow_signin_label')
        sign_in_menu.click()
        user_name = self.dr.find_element(By.NAME, 'identity')
        user_name.clear()
        user_name.send_keys(username)
        password_field = self.dr.find_element(By.NAME, 'password')
        password_field.clear()
        password_field.send_keys(password)
        button_sign_in = self.dr.find_element(By.NAME, 'submit')
        button_sign_in.click()
        # Wait dashboard page
        self.wait.until(presence_of_element_located((By.CSS_SELECTOR, ".base_dashboard.active")),
                   message="Dashboard page doesn't appere")

    def logout(self):
        pass