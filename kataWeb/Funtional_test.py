from __future__ import absolute_import

import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("C:\\chromedriver.exe")
        self.browser.set_window_size(1024, 786)
        self.browser.implicitly_wait(50000)

    def tearDown(self):
        self.browser.quit()



    def test_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        self.browser.implicitly_wait(3)

        username = self.browser.find_element_by_id('username')
        username.send_keys('nombre1')

        password = self.browser.find_element_by_id('password')
        password.send_keys('Clave0000')
