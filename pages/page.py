from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, dr):
        self.dr = dr
        self.wait = WebDriverWait(dr, 5)
        self.action_chain = ActionChains(dr)

    def is_element_present(self, locator):
        try:
            self.dr.find_element(*locator)
        except NoSuchElementException:
            return
        return True

    def find_element(self, locator):
        el = self.wait.until(EC.presence_of_element_located(locator),
                             message=f'No element located by {locator}')
        return el

    def find_elements(self, locator):
        els = self.wait.until(EC.presence_of_all_elements_located(locator),
                              message=f'No any elements by {locator}')
        return els

    def find_visible_element(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator),
                             message=f'No visible element by {locator}')
        return el

    def find_clichable_element(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator),
                             message=f'No clickable element by {locator}')
        return el

    def find_all_visible_elements(self, locator):
        els = self.wait.until(EC.visibility_of_all_elements_located (locator),
                              message=f'No all elements visible by {locator}')
        return els
