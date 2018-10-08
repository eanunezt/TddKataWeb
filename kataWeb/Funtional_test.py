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

    def test_1_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('BuscoAyuda', self.browser.title)
