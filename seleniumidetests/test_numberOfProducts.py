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

class TestNumberOfProducts():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_numberOfProducts(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1552, 840)
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"password\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#item_4_title_link > .inventory_item_name")))
    assert self.driver.find_element(By.CSS_SELECTOR, "#item_4_title_link > .inventory_item_name").text == "Sauce Labs Backpack"
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#item_0_title_link > .inventory_item_name")))
    assert self.driver.find_element(By.CSS_SELECTOR, "#item_0_title_link > .inventory_item_name").text == "Sauce Labs Bike Light"
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#item_1_title_link > .inventory_item_name")))
    assert self.driver.find_element(By.CSS_SELECTOR, "#item_1_title_link > .inventory_item_name").text == "Sauce Labs Bolt T-Shirt"
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#item_5_title_link > .inventory_item_name")))
    assert self.driver.find_element(By.CSS_SELECTOR, "#item_5_title_link > .inventory_item_name").text == "Sauce Labs Fleece Jacket"
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#item_2_title_link > .inventory_item_name")))
    assert self.driver.find_element(By.CSS_SELECTOR, "#item_2_title_link > .inventory_item_name").text == "Sauce Labs Onesie"
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#item_3_title_link > .inventory_item_name")))
    assert self.driver.find_element(By.CSS_SELECTOR, "#item_3_title_link > .inventory_item_name").text == "Test.allTheThings() T-Shirt (Red)"
  