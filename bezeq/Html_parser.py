"""
Auth: Oleg_A

Purpose: Parse html data to find input

Change Log:
    11\11\13 - Creation
"""

#### IMPORTS #################################
from bs4 import BeautifulSoup

#### CONSTANTS ##############################


#### CODE ###################################
class Html_parser:
    """description of class"""
    def __init__(self, html_doc):
        """
        Purpose: Initialize instance
        """
        self.soup = BeautifulSoup(html_doc)

    def update_parser_html(self, html_doc):
        """
        Purpose: Change parser html_doc
        """
        self.soup = BeautifulSoup(html_doc)

    def get_input_fields(self):
        """
        get_input_fields(int) -> list

        Purpose: Get input fields(non hidden) 
        """
        input_tags = []

        for input_tag in self.soup.find_all('input'):
            if not 'hidden' == input_tag.get('type'):
                input_tags.append(input_tag)

        return input_tags
            

    def get_login_fields(self, num_of_fields):
        """
        get_login_fields(int) -> list

        Purpose: Get the input fields needed for login        
        """
        input_fields = self.get_input_fields()

        # Find the input field wich type is password
        for index in xrange(len(input_fields)):            
            if input_fields[index].get('type') == 'password':
                break
        
        # Before password required username, and id
        login_fields = []
        for input_tag in input_fields[index - num_of_fields + 1 : index + 1]:            
            login_fields.append(input_tag.get('name'))

        return login_fields
