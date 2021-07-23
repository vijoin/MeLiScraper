import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


URL = 'https://www.mercadolibre.com.uy/'
PRODUCT = 'miband 6'
SIDE_FILTERS = ['Relojes', 'Montevideo']


class MeLiScraper:

    def click_on_filters(self, filters):
        for filter in filters:
            self.driver.find_element_by_xpath(f'//a[@aria-label="{filter}"]').click()

    @staticmethod
    def convert_to_float(text):
        return float(text.replace('.', '').replace(',', '.'))

    def run(self):
        
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        self.driver.get(URL)
        input_search = self.driver.find_element_by_xpath('//input[@class="nav-search-input"]')
        input_search.send_keys(PRODUCT)
        input_search.send_keys(Keys.RETURN)
        self.driver.find_element_by_xpath('//button[@id="newCookieDisclaimerButton"]').click()
        self.click_on_filters(SIDE_FILTERS)
        input_min = self.driver.find_element_by_xpath('//input[@name="Minimum"]')
        input_min.send_keys('1000')
        input_min.send_keys(Keys.RETURN)
        items_list = self.driver.find_elements_by_xpath('//li[@class="ui-search-layout__item"]')
        
        return [{
                'currency': item.find_element_by_xpath('.//span[@class="price-tag-symbol"]').text,
                'price': self.convert_to_float(item.find_element_by_xpath('.//span[@class="price-tag-fraction"]').text),
                'url': self.driver.find_element_by_xpath('//h2[@class="ui-search-item__title"]/parent::a').get_attribute('href'),
                'title': self.driver.find_element_by_xpath('//h2[@class="ui-search-item__title"]').text,
            } for item in items_list]



if __name__ == '__main__':
    result = MeLiScraper().run()
    print(result)

    
















# Intellisense *
# Formatting
# Easy access to anything (commands palette) (Ctrl + Shift + P)
# Debugging
# Unittesting
# Git Integration
# Remote coding
# Docker integration
# Rainbow parenthesis
# Sync
# Autosave
# Workspace (easy to replicate because of json config)
# Integrated terminal
# Integrated Jupyter Notebooks
# Multiple roots
# Extensions
# Python
# Docker
# Code Runner
# Rainbow Brackets
# Rainbow CSV
# Remote - Containers
# Remote - SSH
# Todo Tree
