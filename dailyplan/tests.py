from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from dailyplan.views import Mainpage
from django.urls import resolve
#For Models testing
from dailyplan.models import Item, User

class IndexTest(TestCase):

	def kamotes(self):
		found = resolve('/')
		self.assertEqual(found.func, Mainpage)

		
	def kamotes(self):
		request = HttpRequest()
		response = Mainpage(request)
		html = response.content.decode('UTF-8')
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'todolist.html')
		self.assertTrue(html.strip().startswith('<html>'))
		self.assertTemplateUsed(response, 'todolist.html')
		self.assertIn('<title>Daily Plans</title>', html)
		self.assertTemplateUsed(response, 'todolist.html')
		self.assertIn('<html>', html)
		self.assertIn('<body bgcolor= "khaki">', html)
		self.assertIn('<title>Daily Plans</title>', html)
		self.assertIn('<h1 style="color:white; font-size:50px; background-color:olive"> <center>Daily Plans</center> </h1>', html) 
		self.assertIn('<h2 style="color:black; font-size:15px; font-style:oblique; font-family:sans-serif; "> <center>todays must do...</center> </h2>', html)
		self.assertIn('<br>', html)		
		self.assertIn('<h3 style="color:black; font-size:25px; ">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;<center>-TASK-</center></h3>', html)
		self.assertIn('<form class ="form" action="" method="post">', html)
		self.assertIn('<center>', html)
		self.assertIn('<center>', html)
		self.assertIn('<input type="date" id="date" name="date">', html)
		self.assertIn('<br>', html)
		self.assertIn('<input bold type="text" id="Task1" name="Task1" placeholder= "1.Enter your Task">', html)
		self.assertIn('<input bold type="text" id="Task2" name="Task2" placeholder= "2.Enter your Task">', html)
		self.assertIn('<input bold type="text" id="Task3" name="Task3" placeholder= "3.Enter your Task">', html)
		self.assertIn('<input bold type="text" id="Task4" name="Task4" placeholder= "4.Enter your Task">', html)
		self.assertIn('<input bold type="text" id="Task5" name="Task5" placeholder= "5.Enter your Task">', html)
		self.assertIn('<br>', html)
		self.assertIn('<br>', html)
		self.assertIn('<input type="submit" value="submit" name="done" id="done">', html)
		self.assertIn('<br>', html)
		self.assertIn('<br>', html)
		self.assertIn('</form>', html)
		self.assertIn('</center>', html)
		self.assertIn('</center>', html)
		self.assertIn('</body>', html)
		self.assertIn('</html>', html)
		
		self.assertTrue(html.strip().endswith('</html>'))


class Patatas1(TestCase):
	def Patatas2(self):
		Item1 = Item()
		Item1.Task1 = '1'
		Item1.save()
		Item2 = Item()
		Item2.Task2 = '2'
		Item2.save()
		Item3 = Item()
		Item3.Task3 = '3'
		Item3.save()
		Item4 = Item()
		Item4.Task4 = '4'
		Item4.save()
		Item5 = Item()
		Item5.Task5 = '5'
		Item5.save()
		Item6 = Item()
		Item6.date = ''
		Item6.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 6)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		save5 = saveall[5]
		self.assertEqual(Item1.Task1, '1')
		self.assertEqual(Item2.Task2, '2')
		self.assertEqual(Item3.Task3, '3')
		self.assertEqual(Item4.Task4, '4')
		self.assertEqual(Item5.Task5, '5')
		self.assertEqual(date.date, '')
		

class Views(TestCase):
	def test_kamoteee(self):
		Item.objects.create(date='date', 
			Task1='Task1', Task2='Task2',
			Task3='Task3', Task4='Task4', Task5='Task5')
		response = self.client.get('/app/views.Mainpage/')

		
class ListViewTest(TestCase):

	def test_uses_list_template(self):
		kamote = User.objects.create()
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'todolist.html')

	def test_uses_home_template(self):
		response = self.client.get('/mais/')
		#self.assertTemplateUsed(response, 'todolist2.html')

	def test_displays_all_list_items(self):
		kamote = User.objects.create()
		Task1 = Item.objects.create(Task1='Task1')
		Task2 = Item.objects.create(Task2='Task2')
		Task3 = Item.objects.create(Task3='Task3')
		Task4 = Item.objects.create(Task4='Task4')
		Task5 = Item.objects.create(Task5='Task5')
		response = self.client.get('/')
		self.assertIn('Task1', response.content.decode())
		self.assertIn('Task2', response.content.decode())
		self.assertIn('Task3', response.content.decode())
		self.assertIn('Task4', response.content.decode())
		self.assertIn('Task5', response.content.decode())
		Task1 = Item.objects.get(Task1="Task1")
		Task2 = Item.objects.get(Task2="Task2")
		Task3 = Item.objects.get(Task3="Task3")
		Task4 = Item.objects.get(Task4="Task4")
		Task5 = Item.objects.get(Task5="Task5")
		self.assertEqual(Item.objects.count(), 5)

		
class Views(TestCase):
	def setUp(self):
		Task1 = Item.objects.create()
		Task2 = Item.objects.create()
		Task3 = Item.objects.create()
		Task4 = Item.objects.create()
		Task5 = Item.objects.create()
		
		Item.objects.create(
			Task1 = '1',
			Task2 = '2',
			Task3 = '3',
			Task4 = '4',
			Task5 = '5',
			)
		self.client.post('/mais/', name='Sambrano, Jessica Ann S.')
		
		#response = 
		self.client.post('/mais/')

		self.assertEqual(Item.objects.count(), 6)
		#self.assertRedirects(response, '/next/')

	def test_redirect_view(self):
		Task1 = Item.objects.get(Task1="1")
		Task2 = Item.objects.get(Task2="2")
		Task3 = Item.objects.get(Task3="3")
		Task4 = Item.objects.get(Task4="4")
		Task5 = Item.objects.get(Task5="5")

		response = self.client.post('/mais/')
		#self.assertRedirects(response, '/mais/')


class URL(TestCase):

	def urls(self):
		found = resolve()
		self.assertEqual(found.func, homepage)
		self.assertEqual(found.func, patyyy)

		url = reverse('todolist')
		self.assertEqual(resolve(url).func, homepage)

		url = reverse('todolist2')
		self.assertEqual(resolve(url).func, patyyy)



class Models(TestCase):

	def models1(self, 
		kamote="test1", 
		Task1="test2", 
		Task2="test3", 
		Task3="test4", 
		Task4="test5", 
		Task5="test6",):
		
		return User.objects.create()
		return Item.objects.create(
			kamote="kamote", 
			Task1="Task1", 
			Task2="Task2", 
			Task3="Task3", 
			Task4="Task4", 
			Task5="Task5", )

	def test_whatever_creation(self):
		j = self.models1()
		self.assertTrue(isinstance(j, User))
		self.assertFalse(isinstance(j, Item))