from django.urls import path

from . import views


app_name = 'home' 

urlpatterns = [
    path('', views.home, name='home'),                      # the website's homepage
    path('faq/', views.faq, name='faq'),                    # the FAQ page
    path('team/', views.team, name='team'),                 # the team page
    path('terms-and-conditions/', views.terms_and_conditions, name='t_n_c'),        # the terms and conditions page
    path('privacy-policy', views.privacy_policy, name='privacy_policy'),            # the privacy policy page
]