import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config
from POM.sixpm_main_page import SIXPMPAGE
from POM.result_page import RESULTPAGE
from Test_data import test_data
import re

def test_1(test_driver, test_logger):

    # activate Chrome browser
    open_6pm_obj = SIXPMPAGE(test_driver, test_logger)
    open_6pm_obj.go_to_page(config.URL)
    open_6pm_obj.search_text()
    test_logger.info("Search text 'classic sunglasses' is sent")
    # Navigate to result page

    result = RESULTPAGE(test_driver, test_logger)
    text = result.select_narrow_choices()

    brand_name = text.split(" - ")[0].strip()

    assert brand_name == test_data.brand_name, "Name is not same"
    test_logger.info(msg='Selected and searched names match')
    
    # match = re.search(r'On sale for \$([\d.,]+)', text)
    # if match:
    #     price = match.group(1)
