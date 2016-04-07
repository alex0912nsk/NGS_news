from base_component import BaseComponent


class Comments(BaseComponent):
    selectors = {
        'self': 'nn-wrapper',
        'add_comment': 'extended_comment-action__link',
        'login': 'login',
        'password': 'passwd',
        'comment': 'text',
        'comment_submit': 'extended_comment-submit',
        'error_message': '//*[@id="123add_error-user-0"]',
        'new_comment': '//*[@id="sub-preview-0"]'
    }

    def write_comment(self, login, password, comment_text):
        self.driver.find_element_by_class_name(self.selectors['add_comment']).click()
        self.driver.find_element_by_name(self.selectors['login']).send_keys(login)
        self.driver.find_element_by_name(self.selectors['password']).send_keys(password)
        self.driver.find_element_by_name(self.selectors['comment']).send_keys(comment_text)
        self.driver.find_element_by_class_name(self.selectors['comment_submit']).click()

    def error_text(self):
        return self.driver.find_element_by_xpath(self.selectors['error_message']).text

    def check_comment_text(self):
        xpath = self.selectors['new_comment'] + "/div/div[2]"
        return self.driver.find_element_by_xpath(xpath).text

    def check_comment_status(self):
        xpath = self.selectors['new_comment'] + "/div/div[3]/div"
        return self.driver.find_element_by_xpath(xpath).text
