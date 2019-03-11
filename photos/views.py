from django.shortcuts import render
from django.contrib.auth.decorators import login_required.

# Create your views here.
def welcome(request):
    return HttpResponse( 'welcome.html')

@login_required(login_url='/accounts/login/')

