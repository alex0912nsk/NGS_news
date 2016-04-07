from base_component import BaseComponent


class AllArticles(BaseComponent):
    selectors = {
        'self': 'nn-wrapper',
        'page': 'http://news.ngs.ru/news/articles/page/'
    }

    def news_number(self, number, type):
        if number > 20:
            page_url = 'http://news.ngs.ru/news/articles/page/' + str(number // 20 + 1)
            self.driver.get(page_url)
        xpath = "//table[@class='news-records']/tbody/tr[" + str(number % 20)

        if type == 'news':
            xpath += "]/td[2]/h2/a"
        elif type == 'comments':
            xpath += "]/td[1]/ul/li[2]/a"
        elif type == 'header_text':
            xpath += "]/td[2]/h2/a"
            return self.driver.find_element_by_xpath(xpath).text
        elif type == 'date':
            xpath += "]/td[2]/h3"
            text = self.driver.find_element_by_xpath(xpath).text
            date = text[1:6]
            return date

        article = self.driver.find_element_by_xpath(xpath).get_attribute('href')
        self.driver.get(article)
