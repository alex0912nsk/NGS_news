class Page:
    def __init__(self, driver):

        self.driver = driver
        self._home_page = None
        self._comments = None
        self._all_articles = None
        self._article = None

    @property
    def home_page(self):
        from home_page import HomePage

        if self._home_page is None:
            self._home_page = HomePage(self.driver,
                                       self.driver.find_element_by_class_name(HomePage.selectors['self']))
        return self._home_page

    @property
    def comments(self):
        from comments import Comments

        if self._comments is None:
            self._comments = Comments(self.driver,
                                      self.driver.find_element_by_class_name(Comments.selectors['self']))
        return self._comments

    @property
    def all_articles(self):
        from all_articles import AllArticles

        if self._all_articles is None:
            self._all_articles = AllArticles(self.driver,
                                             self.driver.find_element_by_class_name(AllArticles.selectors['self']))
        return self._all_articles

    @property
    def article(self):
        from article import Article

        if self._article is None:
            self._article = Article(self.driver, self.driver.find_element_by_class_name(Article.selectors['self']))
        return self._article

    def open(self, url):
        self.driver.get(url)
