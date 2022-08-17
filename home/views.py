from django.shortcuts import render


# Create your views here.

def home(request):
    # this renders the home.html file to the user upon visiting the site
    return render(request, "home/index.html", {'title': "Home"})


def faq(request):
    # this view renders the faq.html file to the user
    return render(request, 'home/faq.html', {'title': "FAQs"})


def terms_and_conditions(request):
    # this view renders the Terms and Conditions page
    return render(request, 'home/t_n_c.html', {'title': "Terms and Conditions"})


def privacy_policy(request):
    # this view renders the Privacy Policy page
    return render(request, 'home/privacy_policy.html', {'title': "Privacy Policy"})


def team(request):
    # this view renders the Team page
    return render(request, 'home/team.html', {'title': "The Team"})
