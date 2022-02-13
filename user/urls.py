from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('profile/', views.profile, name = 'profile'),
    path('main/', views.index_auth, name = 'index_auth'),
    path('signup/', views.signup, name = 'signup'),
    path('logout/', views.logout_view, name = 'logout'),
]
