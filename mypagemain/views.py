from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import portfolio
from QandA.models import Userqa

# Create your views here.
@login_required
def main(request):
    logined = request.user   # login한 User
    logined_user = logined.username
    user_qa = Userqa.objects.filter( reader = logined_user )[:3]
    user_qa_view = Userqa.objects.filter( reader = logined_user )
    n = user_qa_view.count()
    return render(request, 'mypage.html', {
        'userqas' : user_qa,
        'n' : n,
    })

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

