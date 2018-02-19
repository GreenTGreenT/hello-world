#First thing he saw is title. the title name is "Welearn".
#
#
#
#
#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    time.sleep(15)
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):

    # Nut enters to website Welearn
    self.browser.get('http://localhost:8000')

    # He sees the title be named "Welearn" 
    self.assertEqual('Welearn', self.browser.title)
                                            
    # He sees the button be named "Tutor"
    check_button_tutor = self.browser.find_element_by_name('name_tutor')
    self.assertEqual(check_button_tutor.get_attribute('value'), 'Tutor')

    # He click that button, so it change to new url   
    check_button_tutor.click()
    check_url_tutor = self.browser.current_url
    self.assertRegex(check_url_tutor, '/WelearnApp/tutor')

    """check_button_examination = self.browser.find_element_by_name('name_examination')
    self.assertEqual(check_button_examination.get_attribute('value'), 'Examination')

    check_button_problem = self.browser.find_element_by_name('name_problem')
    self.assertEqual(check_button_problem.get_attribute('value'), 'Problem')"""
   
    
    self.fail('Finish the test!')
    
   
    

if __name__ == '__main__':  
   unittest.main(warnings='ignore')
