# from oxwall_helper import OxwallSite
import time
from pages.dashboard_page import DashboardPage

def test_empty_post_create(dr, login):
    dashboard_page = DashboardPage(dr)
    dashboard_page.new_post_text.send_keys("test")

    number_of_old_posts = len(dashboard_page.posts)
    dashboard_page.create_new_post(input_text="")
    assert dashboard_page.message.text == "PLEASE FILL THE FORM PROPERLY"
    time.sleep(2)
    number_of_new_posts = len(dashboard_page.posts)
    assert number_of_new_posts == number_of_old_posts
    time.sleep(5)

def test_text_post_create_positive(dr, login):
    input_text = "New Ivanna Post7!"
    dashboard_page = DashboardPage(dr)
    number_of_posts = dashboard_page.count_posts()
    dashboard_page.create_new_post(input_text)
    posts = dashboard_page.wait_new_post(number_of_posts)
    #Verification new post
    assert posts[0].text == input_text

    # app = OxwallSite(dr)
    # input_text = "New Ivanna Post4!"
    #
    # number_of_posts = app.count_posts()
    # app.create_new_post(input_text)
    # posts = app.wait_new_post(number_of_posts)
    # #Verification new post
    # assert posts[0].text == input_text













