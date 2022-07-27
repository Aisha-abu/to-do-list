from django.shortcuts import render
from.models import Task
from django.views.generic import ListView, DetailView, UpdateView


def home(request):
    return render(request, 'base.html')
class home(ListView):
    model = Task
    template_name = 'base.html'
