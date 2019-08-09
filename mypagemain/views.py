from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import portfolio

# Create your views here.
@login_required
def main(request):
    return render(request,'mypage.html')

@login_required
def timeline(request):
    return render(request, 'timeline.html')

class PfView(ListView):
    model = portfolio
    fields = ['title', 'content_type', 'start_date', 'end_date', 'content']
    success_url = reverse_lazy('timeline')

class PfCreate(CreateView):
    model = portfolio
    fields = ['user', 'title', 'content_type', 'start_date', 'end_date', 'content']
    success_url = reverse_lazy('timeline')

class PfDetail(DetailView):
    model = portfolio
    fields = ['title', 'content_type', 'start_date', 'end_date', 'content']

class PfUpdate(UpdateView):
    model = portfolio
    fields = ['title', 'content_type', 'start_date', 'end_date', 'content']
    success_url = reverse_lazy('timeline')

class PfDelete(DeleteView):
    model = portfolio
    success_url = reverse_lazy('timeline')

