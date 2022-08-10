from django.urls import path
from django.contrib.auth import views as auth_views


from . import views


app_name = 'user_auth'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='user_auth/signin.html'), name='signin'),
    path('signup/',views.signup, name='signup' ),
    path('signout/', auth_views.LogoutView.as_view(template_name='user_auth/signout.html'), name='signout'),
]