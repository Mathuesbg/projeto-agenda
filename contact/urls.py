from django.urls import path
from contact import views


appname = 'contact'

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    
]
