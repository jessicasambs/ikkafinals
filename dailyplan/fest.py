from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from dailyplan.views import Mainpage
from django.urls import resolve
#For Models testing
from dailyplan.models import Item

class IndexTest(TestCase):

	def html_index_root_mainpage_pwede_din_homepage_basta(self):
		found = resolve('/')
		self.assertEqual(found.func, Mainpage)

		
	def test_index_returns_correct_view(self):
		request = HttpRequest()
		response = Mainpage(request)
		html = response.content.decode('UTF-8')
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'todolist.html')

		'''self.assertTrue(html.strip().startswith('<html>'))
		self.assertTemplateUsed(response, 'todolist.html')
		self.assertIn('<title>Daily Plans</title>', html)'''

		self.assertTrue(html.strip().endswith('</html>'))