# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestRemoveError():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_removeError(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1552, 840)
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"password\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"error\"]")))
    self.driver.find_element(By.CSS_SELECTOR, ".fa-times").click()
  
