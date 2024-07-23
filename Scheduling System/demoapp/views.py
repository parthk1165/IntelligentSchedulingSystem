from django.shortcuts import render

def home_page(request):

    return render(request, 'demoapp/home.html')
