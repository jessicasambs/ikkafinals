from django.db import models



APPLIANCES_CHOICES=(('Washing Machine', 'washing machine'), 
	('Dryer', 'dryer'), 
	('Washing Machine With Dryer', 'washing machine with dryer'),
	('Extension', 'extension'),
	('Automatic Washing Machine', 'automatic washing machine'))

class User(models.Model):
	pass

class Item(models.Model):

	kamote = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)
	
	Name = models.TextField(max_length=800, null=True)
	Address = models.TextField(max_length=800, null=True)
	Contact_Number = models.TextField(max_length=800, null=True)
	Email = models.TextField(max_length=800, null=True)
	Contact_Person = models.TextField(max_length=800, null=True)


	#DATE
	date = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.Name

class Equipments(models.Model):
	Washing_Machine = models.CharField(max_length=800)
	Dryer = models.CharField(max_length=800)
	Washing_Machine_With_Dryer = models.CharField(max_length=800)
	Automatic_Washing_Machine = models.CharField(max_length=800)
	Extension = models.CharField(max_length=800)
	Char = models.CharField(max_length=100, choices=APPLIANCES_CHOICES)
	description = models.TextField()

class Delivery(models.Model):
	Dels = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)
	Del = models.CharField(max_length=800, null=True)
	For_Deliver = models.CharField(max_length=800, null=True)
	For_Pickup = models.CharField(max_length=800, null=True)

class Payment(models.Model):
	stripe_charge_id = models.CharField(max_length=50)
	user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
	amount = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.user.username