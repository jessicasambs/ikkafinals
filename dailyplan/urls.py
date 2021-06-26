from django.urls import path
from . import views

urlpatterns = [
	path('', views.Mainpage),
	path('mais', views.Submain, name="mais"),
	path('about', views.About, name="second"),
	path('equipments', views.Equipments, name="third"),
	path('delivery', views.Delivery, name="fourth"),
	path('payment', views.Payment, name="fifth")
]