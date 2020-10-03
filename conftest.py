import pytest
from selenium import webdriver
#from oxwall_helper import OxwallSite
from pages.main_page import MainPage


@pytest.fixture()
def dr():
    dr = webdriver.Chrome()
    # dr.implicitly_wait(5)
    dr.get("http://127.0.0.1:88/oxwall/")
    yield dr
    dr.quit()


@pytest.fixture()
def login(dr):
    main_page = MainPage(dr)
    sign_in_page = main_page.sign_in_initiate()
    sign_in_page.fill_form('admin', 'pass')
    dashboard_page = sign_in_page.submit_form()

    # app = OxwallSite(dr)
    # app.login_as('admin', 'pass')
    yield
    # app.logout()




