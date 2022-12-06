from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feedback
from django.core.paginator import Paginator
# Create your views here.
import datetime
from django.http import JsonResponse
import json

def index(request):
    Feedbacks = Feedback.objects.all().order_by('id')
    paginator = Paginator(Feedbacks, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
    'complaints': Feedbacks,
    'page_obj': page_obj,
    }
    return render(request, 'Feedbacks/index.html', context)




def add_feedback(request):

    context = {
        'values': request.POST
    }
    
    if request.method == 'GET':
        return render(request, 'Feedbacks/add_feedback.html', context)

    if request.method == 'POST':

        name = request.POST['name']
        description = request.POST['description']
        date = request.POST['date']
        category = request.POST['category']

        if not description:
            messages.error(request, 'description is required')
            return render(request, 'Feedback/add_feedback.html', context)

        Feedback.objects.create( name=name,date=date,
                               category=category, description=description)
        messages.success(request, 'Feedback saved successfully')

        return redirect('home')




def dashboard_view(request):
    feedbacks = Feedback.objects.all().order_by('id')
    paginator = Paginator(feedbacks, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)

    context = {
    'complaints': feedbacks,
    'page_obj': page_obj,
    }
    return render(request, 'Feedbacks/dashboard.html', context)


def search_complaints(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        complaints = Feedback.objects.filter(
            name__istartswith=search_str) | Feedback.objects.filter(
            date__istartswith=search_str) | Feedback.objects.filter(
            description__icontains=search_str) | Feedback.objects.filter(
            category__icontains=search_str) 
        data = complaints.values()
        return JsonResponse(list(data), safe=False)



def dashboard_complaint_category_summary(request):
    feedbacks = Feedback.objects.all()
    finalrep = {}

    def get_category(feedback):
        return feedback.category
    category_list = list(set(map(get_category, feedbacks)))

    def get_complaint_category_count(category):
        count = 0
        filtered_by_category = feedbacks.filter(category=category)

        for item in filtered_by_category:
            count += item.count
        return count

    for x in feedbacks:
        for y in category_list:
            finalrep[y] = get_complaint_category_count(y)

    return JsonResponse({'complaint_category_data': finalrep}, safe=False)
