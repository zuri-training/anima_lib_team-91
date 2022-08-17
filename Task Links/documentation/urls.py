<<<<<<< HEAD:documentation/urls.py
from django.urls import path

from . import views


app_name = "documentation"

urlpatterns = [
    path('', views.displayDocumentation, name='documentation'),
=======
from django.urls import path

from . import views


app_name = "documentation"

urlpatterns = [
    path('', views.displayDocumentation, name='documentation'),
>>>>>>> 44bd22b8c26dcfcc942740f23a0f9f65cf382706:Task Links/documentation/urls.py
]