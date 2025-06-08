from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from Helper.helper import Helper
from Test_data import test_data


class SIXPMPAGE(Helper):

    # locators
    search_field = (By.XPATH, '//*[@id="searchAll"]')
    searc_icon = (By.XPATH, '//*[@id="searchForm"]/button')

    def search_text(self):
        self.find_and_send_keys(self.search_field, test_data.search_text)
        self.find_and_click(self.searc_icon)
