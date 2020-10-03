from selenium.webdriver.common.by import By

'''1 решение'''
def presence_of_2_elements_located(dr):
    posts = dr.find_elements(By.CSS_SELECTOR, ".ow_newsfeed_content")
    number_of_posts = len(posts)
    if len(posts) == 2:
        return posts
    else:
        return False

'''2 решение, без привязки количества постов'''
def presence_of_N_elements_located_(locator, number):
    def method(dr):
        posts = dr.find_elements(*locator)
        if len(posts) == number:
            return posts
        else:
            return False
    return method

'''это решение из документации'''
class presence_of_N_elements_located:
    def __init__(self, locator, number):
        self.locator = locator
        self.number = number

    def __call__(self, dr):
        posts = dr.find_elements(*self.locator)
        if len(posts) == self.number and posts[0].is_displayed:
            return posts
        else:
            return False


