from django.urls import path
from . import views
urlpatterns = [
    path('', views.budget_home, name='budget_home'),
]