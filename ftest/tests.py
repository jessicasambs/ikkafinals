from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

class PageTest(LiveServerTestCase):

	
	def setUp(self):
		self.browser = webdriver.Firefox()
		

	def test_browser_title(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Daily Plans', self.browser.title)
		iksmais = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Daily Plans', iksmais)
		iksmais = self.browser.find_element_by_tag_name('h2').text
		self.assertIn('todays must do...', iksmais)
		iksmais = self.browser.find_element_by_tag_name('h3').text
		self.assertIn('-TASK-', iksmais)
		form = self.browser.find_element_by_tag_name('form')
		input1 = self.browser.find_element_by_id('Task1')  
		self.assertEqual(input1.get_attribute('placeholder'),'1.Enter your Task')
		input1 = self.browser.find_element_by_id('Task1').send_keys("1")
		time.sleep(2)
		input2 = self.browser.find_element_by_id('Task2')  
		self.assertEqual(input2.get_attribute('placeholder'),'2.Enter your Task')
		input2 = self.browser.find_element_by_id('Task2').send_keys("2")
		time.sleep(2)
		input3 = self.browser.find_element_by_id('Task3')  
		self.assertEqual(input3.get_attribute('placeholder'),'3.Enter your Task')
		input3 = self.browser.find_element_by_id('Task3').send_keys("3")
		time.sleep(2)
		input4 = self.browser.find_element_by_id('Task4')  
		self.assertEqual(input4.get_attribute('placeholder'),'4.Enter your Task')
		input4 = self.browser.find_element_by_id('Task4').send_keys("4")
		time.sleep(2)
		input5 = self.browser.find_element_by_id('Task5')  
		self.assertEqual(input5.get_attribute('placeholder'),'5.Enter your Task')
		input5 = self.browser.find_element_by_id('Task5').send_keys("5")
		time.sleep(2)
		date = self.browser.find_element_by_id('date').click()
		time.sleep(1)
		date = self.browser.find_element_by_id('date').send_keys("")
		time.sleep(2)
		submitbutton = self.browser.find_element_by_name('done').click()
		time.sleep(2)
		self.browser.quit()


	def test_second(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Daily Plans', self.browser.title)
		input1 = self.browser.find_element_by_id('Task1')  
		self.assertEqual(input1.get_attribute('placeholder'),'1.Enter your Task')
		input1 = self.browser.find_element_by_id('Task1').send_keys("1")
		time.sleep(2)
		input2 = self.browser.find_element_by_id('Task2')  
		self.assertEqual(input2.get_attribute('placeholder'),'2.Enter your Task')
		input2 = self.browser.find_element_by_id('Task2').send_keys("2")
		time.sleep(2)
		input3 = self.browser.find_element_by_id('Task3')  
		self.assertEqual(input3.get_attribute('placeholder'),'3.Enter your Task')
		input3 = self.browser.find_element_by_id('Task3').send_keys("3")
		time.sleep(2)
		input4 = self.browser.find_element_by_id('Task4')  
		self.assertEqual(input4.get_attribute('placeholder'),'4.Enter your Task')
		input4 = self.browser.find_element_by_id('Task4').send_keys("4")
		time.sleep(2)
		input5 = self.browser.find_element_by_id('Task5')  
		self.assertEqual(input5.get_attribute('placeholder'),'5.Enter your Task')
		input5 = self.browser.find_element_by_id('Task5').send_keys("5")
		time.sleep(2)
		date = self.browser.find_element_by_id('date').click()
		time.sleep(1)
		date = self.browser.find_element_by_id('date').send_keys("")
		time.sleep(2)
		submitbutton = self.browser.find_element_by_name('done').click()
		time.sleep(2)
		self.browser.quit()
		

		
'''if __name__ == '__main__':
	unittest.main()'''