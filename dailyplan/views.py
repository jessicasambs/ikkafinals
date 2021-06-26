from django.shortcuts import redirect, render
from .models import Item, User

# Create your views here.
def Mainpage(request):



	
	if request.method == 'POST':


		lab = User.objects.create()
		Item.objects.create(
			Name = request.POST['Name'],
			Address = request.POST['Address'], 
			Contact_Number = request.POST['Contact_Number'],
			Email = request.POST['Email'], 
			Contact_Person = request.POST['Contact_Person'],
			)
		return redirect('mais')

		iks = Item()
		iks.date = date
		iks.Name = Name
		iks.Address  = Address 
		iks.Contact_Number = Contact_Number
		iks.Email = Email
		iks.Contact_Person = Contact_Person
		iks.save()

	return render(request, 'todolist.html')


def Submain (request):
	iks = Item.objects.all().order_by('Name')
	return render(request,'todolist2.html', {'iks': iks})

def About(request):

	return render(request, 'about.html')

def Equipments(request):
	
	return render(request, 'equipments.html')

def Delivery(request):

	return render(request, 'delivery.html')

def Payment(request):

	return render(request, 'payment.html')















