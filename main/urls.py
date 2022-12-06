from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin

urlpatterns = [
    path('', views.index, name="home"),
    path('add-feedback', views.add_feedback, name="add-feedback"),
    path('dashboard', views.dashboard_view, name="dashbord"),
    path('search-complaints', csrf_exempt(views.search_complaints),name="search_complaints"),
    path('dashboard_complaint_category_summary', views.dashboard_complaint_category_summary,name="dashboard_complaint_category_summary"),

]