from base_component import BaseComponent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Article(BaseComponent):
    selectors = {
        'self': 'nn-wrapper',
        'header': '//*[@class="nn-article-header"]/h1',
        'date': '//*[@class="nn-article-header"]/h2/time',
        'first_paragraph': '/html/body/div[1]/div[3]/div[1]/div/article/header/h2/span'

    }

    def header_text(self):
        return self.driver.find_element_by_xpath(self.selectors['header']).text

    def header_date(self):
        date = self.driver.find_element_by_xpath(self.selectors['date']).text
        date = date[:5]
        return date

    def mistake(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath(self.selectors['first_paragraph'])
        action.click_and_hold(element)
        action.move_by_offset(0, -20)
        action.perform()
        element.send_keys(Keys.CONTROL + Keys.ENTER)

        """nn-article-header    '//*[@class="nn-article-header"]'"""
