from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('book/', views.book, name = 'book'),
    path('appoints/', views.appoints, name = 'appoints'),
    path('<str:username>', views.reserve, name = 'reserve'),
]
