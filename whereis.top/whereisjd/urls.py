
from django.urls import path,include
from . import views

app_name = "whereisjd"

urlpatterns = [
    path('whereis/', views.index, name='index'),
]
