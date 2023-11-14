from django.urls import path
from .import views

urlpatterns = [
	path('todolist/landing/', views.display, name='display'),
	path('todolist/', views.update, name='update'),
]

