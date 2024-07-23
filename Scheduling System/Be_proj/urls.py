"""Gandhar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demoapp.views import home_page
from demoapp.views1 import timetable_view1
from demoapp.views2 import timetable_view2
from demoapp.faculty import faculty
from demoapp.lab_odd import lab_odd
from demoapp.lab_even import lab_even
from demoapp.subject_odd import subject_odd
from demoapp.subject_even import subject_even  # Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page, name='home_page'),
    path('odd/', timetable_view1, name='timetable1'),
    path('even/', timetable_view2, name='timetable2'),
    path('teachers/', faculty, name='teachers'),
    path('lab_odd/', lab_odd, name='lab_odd'),
    path('lab_even/', lab_even, name='lab_even'),
    path('subject_odd/', subject_odd, name='subject_odd'),
    path('subject_even/', subject_even, name='subject_even'),  # Correct URL path
]
