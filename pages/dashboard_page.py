from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from custom_wait_condition import presence_of_N_elements_located
from pages.locators import DashBoardLocators
from pages.page import Page


class DashboardPage(Page):

    @property
    def new_post_text(self):
        return self.find_element(DashBoardLocators.POST_TEXT_FIELD)

    @property
    def send_button(self):
        return self.find_visible_element(DashBoardLocators.SEND_BUTTON)

    @property
    def posts(self):
        return self.find_elements(DashBoardLocators.POST_TEXT)

    def wait_new_post(self, number_of_posts):
        # Wait new post appears
        # posts = wait.until(presence_of_2_elements_located)
        posts = self.wait.until(
            presence_of_N_elements_located(DashBoardLocators.POST_TEXT, number_of_posts + 1),
            message= f"Doesn't appear {number_of_posts} elements"
        )
        # posts = dr.find_elements(By.CSS_SELECTOR, ".ow_newsfeed_content")
        # len(posts) == number_of_posts + 1
        return posts

    def create_new_post(self, input_text):
        # Create new post
        self.new_post_text.click()
        self.new_post_text.clear()
        self.new_post_text.send_keys(input_text)
        self.send_button.click()

    def count_posts(self):
        # Count posts
        number_of_posts = len(self.posts)
        return number_of_posts

    def message(self):
        message_element = self.find_visible_element(presence_of_element_located(DashBoardLocators.MESSAGE))
        return message_element.text

