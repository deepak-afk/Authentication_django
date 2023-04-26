from django.urls import path
from .views import signup_process, login_process, dashboard, logout

urlpatterns = [
    path('signup/', signup_process, name='signup_process'),
    path('login/', login_process, name='login_process'),
    path('dashboard/', dashboard, name='dashboard'),
    
]