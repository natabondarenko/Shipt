
import unittest
from time import sleep
from selenium import webdriver



class MyTestCase(unittest.TestCase):

    def setUp(self):
        browser = webdriver.Chrome(executable_path='./chromedriver')
        browser.get('https://www.shipt.com')

        self.driver = browser

    def tearDown(self):
        self.driver.quit()


    def test_empty_email(self):
        warning_text = "Please fill out this field."
        browser = self.driver
        # Find Zip Code form
        zip_check_form = browser.find_element_by_css_selector("form#zip-check-form")
        # Enter ZIP Code where Shipt is not available
        zip_check_form.find_element_by_css_selector('input[name="zip"').send_keys('99950')
        # Submit ZIP Code
        zip_check_form.find_element_by_css_selector('button[type="submit"').click()

        sleep(2)
        # Find Email form
        zip_not_found_modal = browser.find_element_by_css_selector("article#zip-not-found-modal")
        # Submit empty Email
        zip_not_found_modal.find_element_by_css_selector('input[type="submit"').click()
        sleep(1)
        # Get validation message
        email_input = zip_not_found_modal.find_element_by_css_selector('input[name="email"')
        validationMessage = email_input.get_attribute("validationMessage")

        self.assertEqual(warning_text, validationMessage)

if __name__ == '__main__':
    unittest.main()
