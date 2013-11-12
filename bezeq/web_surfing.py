"""
Auth: Oleg_A

Purpose: Parse html data to find input

Change Log:
    11\11\13 - Creation
"""

#### IMPORTS #################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Html_parser import Html_parser
import time

#### CONSTANTS ##############################


#### CODE ###################################
class web_surfing(object):
    """description of class"""
    def __init__(self):
        """
        Purpose: Initialize instance
        """
        self.driver = webdriver.Firefox()
        self.html_parser = Html_parser("")

    def get_next_page(self):
        """
        Purpose: Move on the website
        """
        first_page = self.driver.page_source
        self.driver.get("https://mybill.kvish6.co.il/Login.do")
        current_page = None
        while current_page == first_page:
            time.sleep(10)
            first_page = self.driver.page_source
        

    def login(self, login_credentials):
        """
        login(list) -> 

        Purpose: Login into website
        """
        # Update html_parser html document
        self.html_parser.update_parser_html(self.driver.page_source)
        # Get login fields
        login_fields = self.html_parser.get_login_fields(len(login_credentials))
        
        # Number of login credentials can't be differnt from number of login_fields
        if len(login_credentials) != len(login_fields):            
            return 0

        # Insert Credentials
        for index in xrange(len(login_credentials)):
            element = self.driver.find_element_by_name(login_fields[index])
            element.send_keys(login_credentials[index])
            
        # Pass credentials
        element.send_keys(Keys.RETURN)
