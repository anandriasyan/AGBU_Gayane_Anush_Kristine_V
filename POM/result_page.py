from selenium.webdriver.common.by import By
from Helper.helper import Helper
from conftest import test_logger


class RESULTPAGE(Helper):

    # locators

    brand_checkbox = (By.XPATH, '//*[@id="brandNameFacet"]')
    brand_name = (By.XPATH, '//li[a//span[text()="RAEN Optics"]]')
    price_checkbox = (By.XPATH, '//*[@id="priceFacet"]')
    price = (By.XPATH, '//a//span[text()="$200.00 and Under"]')
    color_checkbox = (By.XPATH, '//*[@id="colorFacet"]')
    orange = (By.XPATH, '//a//span[text()="Orange"]')
    result_item_count = (By.XPATH, '//span[@class="wt-z"]')
    item_title = (By.XPATH, '//*[@id="products"]//article/a')

    def select_narrow_choices(self):

        self.hover_and_click(self.brand_checkbox)
        self.find_and_click(self.brand_name)
        self.hover_and_click(self.price_checkbox)
        self.find_and_click(self.price)
        self.hover_and_click(self.color_checkbox)
        self.find_and_click(self.orange)
        result_count = self.find_elm(self.result_item_count, get_text=True)
        self.test_logger.info(f'Find result couint is {result_count}')
        get_search_elm_text = self.find_elm(self.item_title, get_text=True)
        return get_search_elm_text
      
