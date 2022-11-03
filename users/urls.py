from django.urls import path
from .views import login_view, user_registration, logout_view

app_name = 'user'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', user_registration, name='register'),
    path('logout/', logout_view, name='logout')
]
