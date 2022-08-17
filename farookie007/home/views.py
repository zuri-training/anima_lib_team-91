from django.shortcuts import render


# Create your views here.

def home(request):
    # this renders the home.html file to the user upon visiting the site
<<<<<<< HEAD:home/views.py
    return render(request, "home/index.html", {'title': "Home"})


def faq(request):
    # this view renders the faq.html file to the user
    return render(request, 'home/faq.html', {'title': "FAQs"})
=======
    return render(request, "home/index.html")
>>>>>>> 44bd22b8c26dcfcc942740f23a0f9f65cf382706:farookie007/home/views.py
