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

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('nombre1 nombre2')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('apellido1 apellido2')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('2')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollo Python']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3101234567')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('algo@algo.com')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('C:\\avatar.jpeg')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('nombre123')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('Clave0000')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(10)

        span = self.browser.find_element(By.XPATH, '//span[text()="nombre1 nombre2 apellido1 apellido2"]')

        self.assertIn('nombre1 nombre2 apellido1 apellido2', span.text)
