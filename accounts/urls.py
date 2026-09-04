# pyrefly: ignore [missing-import]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add/', views.add,name='add'),
    path('subtract/', views.subtract,name='subtract'),
    path('division/',views.division,name='division'),
    path('multiplication/',views.multiplication,name='multiplication'),
    path('modulus/',views.modulus,name='modulus'),
    path('power/',views.power,name='power'),
]