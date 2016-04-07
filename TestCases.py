# -*- coding:UTF-8 -*-
from unittest import TestCase
import unittest

from selenium import webdriver
from page import Page
from __init__ import data_provider


class SeleniumTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.page = Page(self.driver)
        self.page.open("http://news.ngs.ru/")

    def tearDown(self):
        self.driver.close()

    parametrs = lambda: (('', '', '', 'Представьтесь, пожалуйста'),
                         ('ppp', '', '', 'Введите пароль'),
                         ('ppp', 'ppp', '', 'Не указан текст комментария'),
                         ('ppp', 'ppp', 'ppp',
                          'Неправильный логин или пароль. Введите логин(e-mail) и пароль от единого аккаунта НГС'))

    @data_provider(parametrs)
    def test_comments_false(self, login, password, comment_text, assert_text):
        self.page.home_page.open_articles()
        self.page.all_articles.news_number(42, 'comments')
        self.page.comments.write_comment(login, password, comment_text)
        self.assertEqual(assert_text, self.page.comments.error_text())

    def test_comments_true(self):
        self.page.home_page.open_articles()
        self.page.all_articles.news_number(145, 'comments')
        comment = 'пишу автотесты, не добавляйте комментарий и простите:)'
        status = 'Комментарий добавлен. Пользователи увидят его после проверки модератором'
        self.page.comments.write_comment('ggg', 'ggg', comment)
        self.assertEqual(self.page.comments.check_comment_text(), comment)
        self.assertEqual(self.page.comments.check_comment_status(), status)

    def test_check_news(self):
        self.page.home_page.open_articles()
        head = self.page.all_articles.news_number(7, 'header_text')
        date = self.page.all_articles.news_number(7, 'date')
        self.page.all_articles.news_number(7, 'news')
        self.assertEqual(head, self.page.article.header_text())
        self.assertEqual(date, self.page.article.header_date())

    def test_mistake(self):
        self.page.home_page.open_articles()
        self.page.all_articles.news_number(7, 'news')
        self.page.article.mistake()

if __name__ == '__main__':
    unittest.main()
