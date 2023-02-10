import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class SampleTestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get('http://localhost:3000')

    def test_signup_click(self):
        signup_link = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/p[1]/a')
        signup_link.click()
        self.assertEqual(self.driver.current_url, 'http://localhost:3000/auth')
        
    def test_email_field(self):
        signup_link = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/p[1]/a')
        signup_link.click()
        emailField = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div/div/input')
        emailField.send_keys('toobaahrabi@gmail.com')
        self.assertEqual(emailField.get_attribute('value'), 'toobaahrabi@gmail.com')
        
    def test_btn_click(self):
        signup_link = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/p[1]/a')
        signup_link.click()
        emailField = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div/div/input')
        emailField.send_keys('toobaahrabi@gmail.com')
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div/div/button')
        submit_button.click()
        self.assertEqual(emailField.is_enabled(), False)
        
    def test_btn_loading_class(self):
        signup_link = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/p[1]/a')
        signup_link.click()
        emailField = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div/div/input')
        emailField.send_keys('toobaahrabi@gmail.com')
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div/div/button')
        submit_button.click()
        self.assertEqual('loading' in submit_button.get_attribute('class'), True)
        
    def test_empty_field(self):
        signup_link = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/p[1]/a')
        signup_link.click()
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div/div/button')
        submit_button.click()
        self.assertEqual('loading' in submit_button.get_attribute('class'), False)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()