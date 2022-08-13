from django.shortcuts import render


# Create your views here.

def home(request):
    # this renders the home.html file to the user upon visiting the site
    return render(request, "home/index.html", {'title': "Home"})


def faq(request):
    # this view renders the faq.html file to the user
    return render(request, 'home/faq.html', {'title': "FAQs"})