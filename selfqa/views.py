from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClassBlog

# Create your views here.
def main(request):
    return render(request,'selfqa.html')

class QaView(ListView):
    model = ClassBlog

class QaCreate(CreateView):
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class QaDetail(DetailView):
    model = ClassBlog

class QaUpdate(UpdateView):
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class QaDelete(DeleteView):
    model = ClassBlog
    success_url = reverse_lazy('list')

