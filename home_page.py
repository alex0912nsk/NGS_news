from base_component import BaseComponent


class HomePage(BaseComponent):
    selectors = {
        'self': 'nn-wrapper',
        'all_article': 'nn-more-box__button',
        'profile': 'nn-top-nav__authentication',
        'nick': 'nn-profile__nick',
        'logout': "//div[@class='nn-top-nav__authentication']/ul/li[3]"
    }

    def open_articles(self):
        self.driver.find_element_by_class_name(self.selectors['all_article']).click()
